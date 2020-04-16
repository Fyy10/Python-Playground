#!/bin/dash

# adding with until loop

# sol 1
s=0
cnt=0
until [ "$cnt" -eq "$#" ]; do
    cnt=$(($cnt + 1))
    eval tmp="\$$cnt"
    if [ "$cnt" -eq "$#" ]; then
        printf "$tmp = "
    else
        printf "$tmp + "
    fi
    s=$(($s + $tmp))
done

printf "$s\n"

# sol 2
s=0
until [ "$#" -eq 0 ]; do
    s=$(($s + $1))
    if [ "$#" -eq 1 ]; then
        printf "$1 = "
    else
        printf "$1 + "
    fi
    shift
done

printf "$s\n"
