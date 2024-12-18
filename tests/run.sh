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

python3 ../hdlconv/slog2vlog.py --output conv7.v --top Counter \
  hdl/slog/counter.sv

python3 ../hdlconv/slog2vlog.py --output conv8.v \
  --include hdl/slog/include1 --include hdl/slog/include2 \
  --define DEFINE1 1 --define DEFINE2 1 \
  --param FREQ 10000000 --param SECS 1 \
  --top Top hdl/slog/blink.sv hdl/slog/top.sv

python3 ../hdlconv/slog2vlog.py --frontend synlig --output conv9.v --top Counter \
   hdl/slog/counter.sv

# python3 ../hdlconv/slog2vlog.py --frontend synlig --output convA.v \
#   --include hdl/slog/include1 --include hdl/slog/include2 \
#   --define DEFINE1 1 --define DEFINE2 1 \
#   --param FREQ 10000000 --param SECS 1 \
#   --top Top hdl/slog/blink.sv hdl/slog/top.sv

python3 ../hdlconv/slog2vlog.py --frontend yosys --output convB.v --top Counter \
  hdl/slog/counter.sv

python3 ../hdlconv/slog2vlog.py --frontend yosys --output convC.v \
  --include hdl/slog/include1 --include hdl/slog/include2 \
  --define DEFINE1 1 --define DEFINE2 1 \
  --param FREQ 10000000 --param SECS 1 \
  --top Top hdl/slog/blink.sv hdl/slog/top.sv
