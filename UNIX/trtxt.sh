#!/bin/sh
files=`find /exam -name "*.txt"`

for file in $files; do
    cat $file > "$file.bak"
    tr -s "\r\n" "\n" < $file > $file
done
