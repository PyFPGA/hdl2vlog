#!/bin/bash

set -e

python3 ../hdlconv/vhdl2vhdl.py \
  --generic FREQ 10000000 --generic SECS 1 --arch Arch --top Top \
  hdl/vhdl/blink.vhdl,blink_lib hdl/vhdl/blink_pkg.vhdl,blink_lib hdl/vhdl/top.vhdl

python3 ../hdlconv/vhdl2vlog.py \
  --generic FREQ 10000000 --generic SECS 1 --arch Arch --top Top \
  hdl/vhdl/blink.vhdl,blink_lib hdl/vhdl/blink_pkg.vhdl,blink_lib hdl/vhdl/top.vhdl
