# HDLconv

HDL converter (between VHDL, SystemVerilog and/or Verilog), based on [GHDL](https://github.com/ghdl/ghdl), [Yosys](https://github.com/YosysHQ/yosys), [Synlig](https://github.com/chipsalliance/synlig) and the plugins [ghdl-yosys-plugin](https://github.com/ghdl/ghdl-yosys-plugin) and [yosys-slang](https://github.com/povik/yosys-slang).
It relies on [Docker](https://docs.docker.com/get-docker) and [PyFPGA containers](https://github.com/PyFPGA/containers).

* `vhdl2vhdl`: converts from a newer VHDL to VHDL'93 (using GHDL).
* `vhdl2vlog`: converts from VHDL to Verilog (using GHDL or Yosys).
* `slog2vlog`: converts from SystemVerilog to Verilog (using yosys-slang, synlig or Yosys).

# Documentation

```
usage: vhdl2vhdl [-h] [-v] [--debug] [--generic GENERIC VALUE] [--arch ARCH]
                 [-t NAME] [-o PATH]
                 FILE[,LIBRARY] [FILE[,LIBRARY] ...]

VHDL to VHDL

positional arguments:
  FILE[,LIBRARY]        VHDL file/s (with an optional LIBRARY specification)

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  --debug               Enables debug mode
  --generic GENERIC VALUE
                        specify a top-level Generic (can be specified multiple
                        times)
  --arch ARCH           specify a top-level Architecture
  -t NAME, --top NAME   specify the top-level of the design
  -o PATH, --output PATH
                        output file [converted.vhdl]
```

```
usage: vhdl2vlog [-h] [-v] [--debug] [--backend TOOL]
                 [--generic GENERIC VALUE] [--arch ARCH] [-t NAME] [-o PATH]
                 FILE[,LIBRARY] [FILE[,LIBRARY] ...]

VHDL to Verilog

positional arguments:
  FILE[,LIBRARY]        VHDL file/s (with an optional LIBRARY specification)

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  --debug               Enables debug mode
  --backend TOOL        backend tool [ghdl]
  --generic GENERIC VALUE
                        specify a top-level Generic (can be specified multiple
                        times)
  --arch ARCH           specify a top-level Architecture
  -t NAME, --top NAME   specify the top-level of the design
  -o PATH, --output PATH
                        output file [converted.v]
```

```
usage: slog2vlog [-h] [-v] [--debug] [--frontend TOOL] [--param PARAM VALUE]
                 [--define DEFINE VALUE] [--include PATH] [-t NAME] [-o PATH]
                 FILE [FILE ...]

SystemVerilog to Verilog

positional arguments:
  FILE                  System Verilog file/s

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  --debug               Enables debug mode
  --frontend TOOL       backend tool [slang]
  --param PARAM VALUE   specify a top-level Parameter (can be specified
                        multiple times)
  --define DEFINE VALUE
                        specify a Define (can be specified multiple times)
  --include PATH        specify an Include Path (can be specified multiple
                        times)
  -t NAME, --top NAME   specify the top-level of the design
  -o PATH, --output PATH
                        output file [converted.v]
```
