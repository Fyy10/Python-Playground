#! /bin/bash

# ingnore the listed signals
trap "echo I refuse to die!" 2 3

# disable echo
stty -echo

# clear
tput clear
tput cup 5 10; printf "Enter your password: "
read pswd
tput cup 7 10
${pswd:?"Please enter a valid password."}

tput clear
tput cup 5 10; printf "SYSTEM LOCKED"
tput cup 7 10

pswd_in=""
until [ "$pswd" = "$pswd_in" ]; do
    # printf "Your password: "
    read pswd_in
done

# enable echo
stty echo

clear
exit 0
