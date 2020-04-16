#!/bin/dash

# adding with for loop

# sol 1
s=0
cnt=0
for i in $@; do
    cnt=$(($cnt + 1))
    s=$(($s + $i))
    if [ "$cnt" -eq "$#" ]; then
        printf "$i = "
    else
        printf "$i + "
    fi
done

printf "$s\n"

# sol 2
s=0
for i in `seq 1 $#`; do
    eval tmp="\$$i"
    s=$(($s + $tmp))
    if [ "$i" -eq "$#" ]; then
        printf "$tmp = "
    else
        printf "$tmp + "
    fi
done

printf "$s\n"
