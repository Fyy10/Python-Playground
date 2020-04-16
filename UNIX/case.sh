#!/bin/dash

case $1 in
    -d)
        printf "debug\n"
        ;;
    -v)
        printf "verbose\n"
        ;;
    *)
        printf "usage $0 -d|-v\n"
        ;;
esac
