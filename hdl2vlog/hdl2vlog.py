#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2020-2023 Rodrigo A. Melo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""hdl2vlog: VHDL/SV to Verilog converter"""

import argparse

from __version__ import __version__ as version
from pathlib import Path


def get_args(is_vhdl=False):
    """Get arguments from the CLI"""

    _MULTIPLE = '(can be specified multiple times)'

    prog= 'vhdl2vlog' if is_vhdl else 'slog2vlog'
    lang = 'VHDL' if is_vhdl else 'System Verilog'
    description = f'{lang} to Verilog converter'
    parser = argparse.ArgumentParser(prog=prog, description=description)

    parser.add_argument(
        '-v', '--version',
        action='version',
        version=f'hdl2vlog - v{version}'
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

def get_template(name):
    template = Path(__file__).parent / 'templates' / name
    with template.open('r', encoding='utf-8') as fp:
        return fp.read().strip()

def slog2vlog():
    args = get_args(is_vhdl=False)
    print(args)
    cmd = get_template('yosys').format(
        includes='',
        defines='',
        files='FILES',
        params='',
        top='TOP',
        output=args.output
    )
    print(cmd)


def vhdl2vlog():
    args = get_args(is_vhdl=True)
    print(args)
    cmd = get_template('yosys').format(
        includes='',
        defines='',
        files='FILES',
        params='',
        top='TOP',
        output=args.output
    )
    print(cmd)
