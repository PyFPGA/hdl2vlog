IMAGE=pyfpga/synthesis
DOCKER="docker run --rm -v $PWD/..:$PWD/.. -w $PWD --user $(id -u):$(id -g) $IMAGE"

mkdir -p results

$DOCKER yosys -Q -p "
plugin -i systemverilog
read_systemverilog ../hdl/slog/counter.sv
write_verilog -noattr results/counter_from_sv.v
"

$DOCKER yosys -Q -m ghdl -p "
ghdl ../hdl/vhdl/counter.vhdl -e;
write_verilog -noattr results/counter_from_vhdl.v
"

rm -fr slpp_all
