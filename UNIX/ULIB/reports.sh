#! /bin/bash
# REPORTS Menu

# functions
# 把REPORT_TMP文件转换成指定的格式
CONVERT()
{
    # save original IFS
    ORI_IFS="$IFS"
    for line in `cat REPORT_TMP`; do
        # 在使用echo输出line时，需要保留":"，所以暂时替换为原来的IFS
        IFS="$ORI_IFS"
        echo $line > line_TMP

        # 从line_TMP中读取TITLE等信息时，需要以":"作为分隔符
        IFS=":"
        read tmp TITLE AUTHOR CATEGORY STATUS BNAME DATE < line_TMP
        rm line_TMP

        # 按格式输出到文件
        echo "Title: $TITLE" >> NEW_REPORT_TMP
        echo "Author: $AUTHOR" >> NEW_REPORT_TMP
        echo "Category: $CATEGORY" >> NEW_REPORT_TMP
        echo "Status: $STATUS" >> NEW_REPORT_TMP

        # status为out时输出BNAME和DATE
        if [ "$STATUS" = "out" ]; then
            printf "\n" >> NEW_REPORT_TMP
            echo "Checked out by: $BNAME" >> NEW_REPORT_TMP
            echo "Date: $DATE" >> NEW_REPORT_TMP
        fi

        printf "\n\n" >> NEW_REPORT_TMP
    done
    mv NEW_REPORT_TMP REPORT_TMP

    # 还原原先的IFS
    IFS="$ORI_IFS"
    return 0
}

# sort by titles
SORT_TITLE()
{
    sort -t: -k2 library -o REPORT_TMP
    tput clear
    CONVERT
    more REPORT_TMP
    rm REPORT_TMP
    return 0
}

# sort by author
SORT_AUTHOR()
{
    sort -t: -k3 library -o REPORT_TMP
    tput clear
    CONVERT
    more REPORT_TMP
    rm REPORT_TMP
    return 0
}

# sort by category
SORT_CATEGORY()
{
    sort -t: -k4 library -o REPORT_TMP
    tput clear
    CONVERT
    more REPORT_TMP
    rm REPORT_TMP
    return 0
}

# menu
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
# 当library文件中记录数较少时，通过sleep保持文件内容正常显示（等待5s）
sleep 5
exit 0

