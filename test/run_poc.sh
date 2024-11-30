set -e

IMAGE=ghcr.io/pyfpga/synthesis
DOCKER="docker run --rm -v $PWD/..:$PWD/.. -w $PWD --user $(id -u):$(id -g) $IMAGE"
OUTDIR=results/poc

mkdir -p $OUTDIR

$DOCKER yosys -Q -m ghdl -p "
ghdl ../hdl/vhdl/counter.vhdl -e
hierarchy -top counter
write_verilog -noattr $OUTDIR/vhdl-counter.v
"

$DOCKER synlig -Q -p "
read_systemverilog ../hdl/slog/counter.sv
hierarchy -top counter
write_verilog -noattr $OUTDIR/slog-counter.v
"

rm -fr slpp_all
