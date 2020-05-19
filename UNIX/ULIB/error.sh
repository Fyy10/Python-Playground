#! /bin/bash
# ERROR

tput cup $1 $2
echo "Wrong Input. Try again."
tput cup $(($1+2)) $2
printf "Press any key to continue..."
read ANSWER
exit 0
