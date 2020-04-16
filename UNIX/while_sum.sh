#!/bin/dash

# adding with while loop

# sol 1
s=0
cnt=0
while [ "$cnt" != "$#" ]; do
    cnt=$(($cnt + 1))
    eval tmp="\$$cnt"
    s=$(($s + $tmp))
    if [ "$cnt" != "$#" ]; then
        printf "$tmp + "
    else
        printf "$tmp = "
    fi
done

printf "$s\n"

# sol 2
s=0
while [ "$#" != 0 ]; do
    s=$(($s + $1))
    if [ "$#" -eq 1 ]; then
        printf "$1 = "
    else
        printf "$1 + "
    fi
    shift
done

printf "$s\n"
