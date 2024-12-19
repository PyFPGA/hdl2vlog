#!/bin/bash

file="README.md"
pattern="# Documentation"

lines=()

while IFS= read -r line; do
    if [[ "$line" =~ $pattern ]]; then
        break
    fi
    lines+=("$line")
done < "$file"

result=$(IFS=$'\n'; echo "${lines[*]}")
echo "$result" > $file

vhdl2vhdl=$(python3 hdlconv/vhdl2vhdl.py -h)
vhdl2vlog=$(python3 hdlconv/vhdl2vlog.py -h)
slog2vlog=$(python3 hdlconv/slog2vlog.py -h)

echo ""           >> $file
echo "$pattern"   >> $file
echo ""           >> $file

echo '```'        >> $file
echo "$vhdl2vhdl" >> $file
echo '```'        >> $file
echo ""           >> $file
echo '```'        >> $file
echo "$vhdl2vlog" >> $file
echo '```'        >> $file
echo ""           >> $file
echo '```'        >> $file
echo "$slog2vlog" >> $file
echo '```'        >> $file

#vhdl2vhdl=$(printf '%s' "$vhdl2vhdl" | sed 's/\[/\\[/g' | sed 's/\]/\\]/g' | sed 's/\(/\\(/g' | sed 's/\)/\\)/g')
#vhdl2vlog=$(printf '%s' "$vhdl2vlog" | sed 's/\[/\\[/g' | sed 's/\]/\\]/g' | sed 's/\(/\\(/g' | sed 's/\)/\\)/g')
#slog2vlog=$(printf '%s' "$slog2vlog" | sed 's/\[/\\[/g' | sed 's/\]/\\]/g' | sed 's/\(/\\(/g' | sed 's/\)/\\)/g')

#echo "$vhdl2vhdl"
#echo "$vhdl2vlog"
#echo "$slog2vlog"

#sed -i '/^```vhdl2vhdl/,/^```$/c\```vhdl2vhdl\n'"$vhdl2vhdl"'\n```' README.md
#sed -i '/^```vhdl2vlog/,/^```$/c\```vhdl2vlog\n'"$vhdl2vlog"'\n```' README.md
#sed -i '/^```slog2vlog/,/^```$/c\```slog2vlog\n'"$slog2vlog"'\n```' README.md
