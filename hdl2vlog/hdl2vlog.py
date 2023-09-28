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
import errno
import logging
import sys

from __version__ import __version__ as version


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
        version=f'v{version}'
    )

    parser.add_argument(
        '-o', '--output',
        metavar='PATH/FILE.v',
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
            metavar=('NAME', 'VALUE'),
            action='append',
            nargs=2,
            help=f'specify a top-level Generic {_MULTIPLE}'
        )

        parser.add_argument(
            '--arch',
            metavar='NAME',
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
            metavar=('NAME', 'VALUE'),
            action='append',
            nargs=2,
            help=f'specify a top-level Parameter {_MULTIPLE}'
        )

        parser.add_argument(
            '--define',
            metavar=('NAME', 'VALUE'),
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


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--vhdl', action='store_true')
    args = parser.parse_args()
    if args.vhdl:
        print(get_args(True))
    else:
        print(get_args(False))
