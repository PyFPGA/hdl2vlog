set -e

SLOG2VLOG=../hdl2vlog/slog2vlog.py
FILES=../hdl/slog
OUTDIR=results

python3 $SLOG2VLOG --top counter --output $OUTDIR/slog.v $FILES/counter.sv
