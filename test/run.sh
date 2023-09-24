IMAGE=pyfpga/synthesis

mkdir -p results

docker run --rm -v $PWD/..:$PWD/.. -w $PWD $IMAGE yosys -Q -p "
plugin -i systemverilog
read_systemverilog ../hdl/slog/counter.sv
write_verilog -noattr results/counter.v
"

docker run --rm -v $PWD/..:$PWD/.. -w $PWD $IMAGE rm -fr slpp_all
