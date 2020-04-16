#!/bin/dash

maxnum=0

# for loop
for i in $@; do
    [ "$i" -gt "$maxnum" ] && maxnum=$i
done

printf "The largest number is: $maxnum\n"

# while loop
i=1
maxnum=0
while [ "$i" -lt $(($# + 1)) ]; do
    eval tmp=\$$i
    [ "$tmp" -gt "$maxnum" ] && maxnum=$tmp
    i=$(($i + 1))
done

printf "The largest number is: $maxnum\n"

# until loop
i=1
maxnum=0
until [ "$i" -gt "$#" ]; do
    eval tmp=\$$i
    [ "$tmp" -gt "$maxnum" ] && maxnum=$tmp
    i=$(($i + 1))
done

printf "The largest number is: $maxnum\n"
