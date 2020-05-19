#! /bin/bash
# 程序的主目录，用于选择分支程序

# bold, normal settings 粗体、正常设置（实际上是突出显示与不突出显示）
BOLD=`tput smso`
NORMAL=`tput rmso`
export BOLD NORMAL

# main page 主页
tput clear
tput cup 4 10
printf "${BOLD}Super Duper UNIX Library\n"
tput cup 8 10
printf "${NORMAL}This is the UNIX Library application\n"
tput cup 10 10
printf "Please enter any key to continue..."
read ANSWER

# 提示信息
while true; do
    tput clear
    tput cup 5 10
    printf "UNIX Library - ${BOLD}MAIN MENU${NORMAL}\n"
    tput cup 7 20
    printf "0. ${BOLD}EXIT${NORMAL} this program\n"
    tput cup 9 20
    printf "1. ${BOLD}EDIT${NORMAL} Menu\n"
    tput cup 11 20
    printf "2. ${BOLD}REPORTS${NORMAL} Menu\n"
    tput cup 13 10
    printf "Enter your choice> "
    read CHOICE

    case $CHOICE in
        0) tput clear; exit 0;;
        1) ./edit.sh;;
        2) ./reports.sh;;
        *) ./error.sh 16 10;;
    esac
done

