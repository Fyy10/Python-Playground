#!/bin/dash

a=0
b=1

if [ "$1" -lt 0 ]; then
    printf "Error Range!\n"
    exit 1
fi

case $1 in
    0)
        printf "$a\n"
        ;;
    1)
        printf "$a $b\n"
        ;;
    *)
        printf "$a $b "
        for i in `seq 2 $1`; do
            tmp=$(($a + $b))
            [ "$i" -eq "$1" ] && printf "$tmp\n" || printf "$tmp "
            a=$b
            b=$tmp
        done
        ;;
esac
