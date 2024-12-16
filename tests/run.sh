#!/bin/bash

set -e

python3 ../hdlconv/vhdl2vhdl.py --output conv1.vhdl --top Counter hdl/vhdl/counter.vhdl

python3 ../hdlconv/vhdl2vhdl.py --output conv2.vhdl \
  --generic FREQ 10000000 --generic SECS 1 --arch Arch --top Top \
  hdl/vhdl/blink.vhdl,blink_lib hdl/vhdl/blink_pkg.vhdl,blink_lib hdl/vhdl/top.vhdl

python3 ../hdlconv/vhdl2vlog.py --output conv3.v --top Counter hdl/vhdl/counter.vhdl

python3 ../hdlconv/vhdl2vlog.py --output conv4.v \
  --generic FREQ 10000000 --generic SECS 1 --arch Arch --top Top \
  hdl/vhdl/blink.vhdl,blink_lib hdl/vhdl/blink_pkg.vhdl,blink_lib hdl/vhdl/top.vhdl

python3 ../hdlconv/vhdl2vlog.py --backend yosys --output conv5.v --top Counter \
   hdl/vhdl/counter.vhdl

python3 ../hdlconv/vhdl2vlog.py --backend yosys --output conv6.v \
  --generic FREQ 10000000 --generic SECS 1 --arch Arch --top Top \
  hdl/vhdl/blink.vhdl,blink_lib hdl/vhdl/blink_pkg.vhdl,blink_lib hdl/vhdl/top.vhdl
