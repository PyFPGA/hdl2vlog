# HDLconv

> **WARNING:** this is a WIP project in its early stages (as of Dec 2024).

HDL converter (between VHDL, SystemVerilog and/or Verilog), based on [GHDL](https://github.com/ghdl/ghdl), [Yosys](https://github.com/YosysHQ/yosys), and the plugins [ghdl-yosys-plugin](https://github.com/ghdl/ghdl-yosys-plugin) and [yosys-slang](https://github.com/povik/yosys-slang).
It relies on [Docker](https://docs.docker.com/get-docker) and [PyFPGA containers](https://github.com/PyFPGA/containers).

* `vhdl2vhdl`: converts from a newer VHDL to VHDL'93.
* `vhdl2vlog`: converts from VHDL to Verilog.
* `slog2vlog`: converts from SystemVerilog to Verilog.
