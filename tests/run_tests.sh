set -e

SLOG2VLOG=../hdl2vlog/slog2vlog.py
VHDL2VLOG=../hdl2vlog/vhdl2vlog.py
SFILES=../hdl/slog
SFILES=../hdl/vlog
OUTDIR=results

python3 $SLOG2VLOG --top counter --output $OUTDIR/slog-counter.v $SFILES/counter.sv
python3 $VHDL2VLOG --top counter --output $OUTDIR/vhdl-counter.v $VFILES/counter.vhdl
