#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2020-2024 PyFPGA Project
#
# SPDX-License-Identifier: GPL-3.0-or-later
#

"""HDLconv: HDL converter"""

import argparse
import logging
import shutil
import subprocess
import time

from pathlib import Path
from jinja2 import Environment, FileSystemLoader


from __version__ import __version__ as version
from pathlib import Path


_log = logging.getLogger(__name__)
_log.level = logging.INFO
_log.addHandler(logging.NullHandler())


def get_args(is_vhdl=False):
    """Get arguments from the CLI"""

    _MULTIPLE = '(can be specified multiple times)'

    prog= 'vhdl2vlog' if is_vhdl else 'slog2vlog'
    lang = 'VHDL' if is_vhdl else 'System Verilog'
    description = f'{lang} to Verilog compiler'
    parser = argparse.ArgumentParser(prog=prog, description=description)

    parser.add_argument(
        '-v', '--version',
        action='version',
        version=f'HDLconv: - v{version}'
    )
    parser.add_argument(
        '-o', '--output',
        metavar='PATH',
        default='converted.v',
        help='output file [converted.v]'
    )
    parser.add_argument(
        '-t', '--top',
        metavar='NAME',
        help='specify the top-level of the design'
    )

    if is_vhdl:
        parser.add_argument(
            '--generic',
            metavar=('GENERIC', 'VALUE'),
            action='append',
            nargs=2,
            help=f'specify a top-level Generic {_MULTIPLE}'
        )
        parser.add_argument(
            '--arch',
            metavar='ARCH',
            help='specify a top-level Architecture'
        )
        parser.add_argument(
            'files',
            metavar='FILE[,LIBRARY]',
            nargs='+',
            help='VHDL file/s (with an optional LIBRARY specification)'
        )
    else:
        parser.add_argument(
            '--param',
            metavar=('PARAM', 'VALUE'),
            action='append',
            nargs=2,
            help=f'specify a top-level Parameter {_MULTIPLE}'
        )
        parser.add_argument(
            '--define',
            metavar=('DEFINE', 'VALUE'),
            action='append',
            nargs=2,
            help=f'specify a Define {_MULTIPLE}'
        )
        parser.add_argument(
            '--include',
            metavar='PATH',
            action='append',
            help=f'specify an Include Path {_MULTIPLE}'
        )
        parser.add_argument(
            'files',
            metavar='FILE',
            nargs='+',
            help='System Verilog file/s'
        )

    return parser.parse_args()

def run(command):
    start = time.time()
    if not shutil.which('docker'):
        _log.error('docker is not available')
    try:
        subprocess.run(
            command, shell=True, check=True, universal_newlines=True,
        )
    finally:
        end = time.time()
        _log.info('executed in %.3f seconds', end-start)

def create_script(hdl, data):
    tempdir = Path(__file__).parent.joinpath('templates')
    jinja_file_loader = FileSystemLoader(str(tempdir))
    jinja_env = Environment(loader=jinja_file_loader)
    jinja_template = jinja_env.get_template(f'{hdl}.jinja')
    content = jinja_template.render(data)
    directory = Path(data['odir'])
    directory.mkdir(parents=True, exist_ok=True)
    with open(directory / f'{hdl}.sh', 'w', encoding='utf-8') as file:
        file.write(content)


def slog2vlog():
    args = get_args(is_vhdl=False)
    files = []
    for file in args.files:
        files.append(file)
    cmd = get_template('yosys').format(
        includes='',
        defines='',
        files=f'read_systemverilog {" ".join(files)}',
        params='',
        top=args.top,
        output=args.output
    )
    run(cmd)

def vhdl2vlog():
    args = get_args(is_vhdl=True)
    file = args.files[0]
    data = {
        'top': args.top,
        'arch': args.arch,
        'output': args.output
    }
    for file in args.files:
        aux = file.split(',')
        file = aux[0]
        lib = aux[1] if len(aux) > 1 else None
        data.setdefault('files', {})[file] = lib
    if args.generic is not None:
        for generic in args.generic:
            data.setdefault('generics', {})[generic[0]] = generic[1]
    print(data)
    exit(1)
    create_script('vhdl', data)
    run(cmd)
