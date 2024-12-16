#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2023 HDLconv Project
#
# SPDX-License-Identifier: GPL-3.0-or-later
#

"""HDLconv: HDL converter"""

import argparse
import os
import subprocess


from jinja2 import Environment, FileSystemLoader
from os import chdir
from pathlib import Path
from __init__ import __version__ as version


LANGS = {
    'vhdl': 'VHDL',
    'vlog': 'Verilog',
    'slog': 'SystemVerilog'
}

def get_args(src, dst):
    """Get arguments from the CLI"""
    MULTIMSG = '(can be specified multiple times)'
    prog = f'{src}2{dst}'
    description = f'{LANGS[src]} to {LANGS[dst]}'
    parser = argparse.ArgumentParser(prog=prog, description=description)
    if src == 'vhdl':
        metavar = 'FILE[,LIBRARY]'
        help = 'VHDL file/s (with an optional LIBRARY specification)'
    else:
        metavar = 'FILE'
        help = 'System Verilog file/s'
    output = 'converted.vhdl' if dst == 'vhdl' else 'converted.v'
    parser.add_argument(
        '-v', '--version',
        action='version',
        version=f'HDLconv - v{version}'
    )
    parser.add_argument(
        '--debug',
        action='store_true',
        help='Enables debug mode'
    )
    if src == 'vhdl' and dst == 'vlog':
        parser.add_argument(
            '--backend',
            metavar='TOOL',
            default='ghdl',
            choices=['ghdl', 'yosys'],
            help='backend tool [ghdl]'
        )
    if src == 'vhdl':
        parser.add_argument(
            '--generic',
            metavar=('GENERIC', 'VALUE'),
            action='append',
            nargs=2,
            help=f'specify a top-level Generic {MULTIMSG}'
        )
        parser.add_argument(
            '--arch',
            metavar='ARCH',
            help='specify a top-level Architecture'
        )
    else:
        parser.add_argument(
            '--param',
            metavar=('PARAM', 'VALUE'),
            action='append',
            nargs=2,
            help=f'specify a top-level Parameter {MULTIMSG}'
        )
        parser.add_argument(
            '--define',
            metavar=('DEFINE', 'VALUE'),
            action='append',
            nargs=2,
            help=f'specify a Define {MULTIMSG}'
        )
        parser.add_argument(
            '--include',
            metavar='PATH',
            action='append',
            help=f'specify an Include Path {MULTIMSG}'
        )
    parser.add_argument(
        '-t', '--top',
        metavar='NAME',
        help='specify the top-level of the design'
    )
    parser.add_argument(
        '-o', '--output',
        metavar='PATH',
        default=output,
        help=f'output file [{output}]'
    )
    parser.add_argument(
        'files',
        metavar=metavar,
        nargs='+',
        help=help
    )
    return parser.parse_args()

def get_data(src, dst, args):
    """Get data from arguments.

    :raises NotADirectoryError: when a directory is not found
    :raises FileNotFoundError: when a file is not found
    """
    data = {}
    data['hdl'] = 'raw-vhdl' if dst == 'vhdl' else 'verilog'
    data['top'] = args.top
    data['output'] = args.output
    if 'arch' in args:
        data['arch'] = args.arch
    if 'generic' in args:
        for generic in args.generic:
            data.setdefault('generics', {})[generic[0]] = generic[1]
    if 'param' in args:
        for param in args.param:
            data.setdefault('params', {})[param[0]] = param[1]
    if 'define' in args:
        for define in args.define:
            data.setdefault('defines', {})[define[0]] = define[1]
    if 'include' in args:
        for include in args.include:
            include = Path(include).resolve()
            if not include.is_dir():
                raise NotADirectoryError(include)
            data.setdefault('includes', {}).append(include)
    for file in args.files:
        if src == 'vhdl':
            aux = file.split(',')
            file = Path(aux[0]).resolve()
            if not file.exists():
                raise FileNotFoundError(file)
            lib = aux[1] if len(aux) > 1 else None
            data.setdefault('files', {})[file] = lib
        else:
            file = Path(aux[0]).resolve()
            if not file.exists():
                raise FileNotFoundError(file)
            data.setdefault('files', {}).append(file)
    return data

def get_template(src, dst, args):
    template = 'ghdl'
    if src == 'slog':
        template = 'slang-yosys'
    if src == 'vhdl' and dst == 'vlog' and args.backend == 'yosys':
        template = 'ghdl-yosys'
    return template

def get_content(tempname, tempdata):
    """Get script to run."""
    tempdir = Path(__file__).parent.joinpath('templates')
    jinja_file_loader = FileSystemLoader(str(tempdir))
    jinja_env = Environment(loader=jinja_file_loader)
    jinja_template = jinja_env.get_template(f'{tempname}.jinja')
    return jinja_template.render(tempdata)

def run_tool(content):
    old_dir = Path.cwd()
    new_dir = Path('temp')
    new_dir.mkdir(parents=True, exist_ok=True)
    chdir(new_dir)
    filename = 'script.sh'
    with open(filename, 'w', encoding='utf-8') as fhandler:
        fhandler.write(content)
    command = f'bash {filename}'
    try:
        subprocess.run(command, shell=True, check=True, text=True)
    finally:
        os.chdir(old_dir)

def HDLconv(src, dst):
    args = get_args(src, dst)
    data = get_data(src, dst, args)
    template = get_template(src, dst, args)
    content = get_content(template, data)
    if args.debug:
        print(content)
    run_tool(content)
