#! /bin/bash
# REPORTS Menu

# functions
# sort by titles
SORT_TITLE()
{
    return 0
}

# sort by author
SORT_AUTHOR()
{
    return 0
}

# sort by category
SORT_CATEGORY()
{
    return 0
}

# menu
while true; do
    tput clear
    tput cup 5 10
    printf "UNIX Library - ${BOLD}REPORTS MENU${NORMAL}\n"
    tput cup 7 20
    printf "0: ${BOLD}RETURN${NORMAL}\n"
    tput cup 9 20
    printf "1: Sorted by ${BOLD}TITLES${NORMAL}\n"
    tput cup 11 20
    printf "2: Sorted by ${BOLD}AUTHOR${NORMAL}\n"
    tput cup 13 20
    printf "3: Sorted by ${BOLD}CATEGORY${NORMAL}\n"

    tput cup 15 10
    printf "Enter your choice> "
    read CHOICE

    case $CHOICE in
        0)tput clear; exit 0;;
        1)SORT_TITLE;;
        2)SORT_AUTHOR;;
        3)SORT_CATEGORY;;
        *)./error.sh 18 10;;
    esac
done

