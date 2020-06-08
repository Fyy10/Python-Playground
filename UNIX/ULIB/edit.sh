#! /bin/bash
# EDIT Menu

# functions
# 添加记录
ADD()
{
    # 清空变量
    unset TITLE AUTHOR CATEGORY STATUS BNAME DATE
    DATE=`date +%D`
    # 是否继续循环
    ANSWER=y
    while [ "$ANSWER" = y ]; do
        tput clear
        tput cup 5 10; echo "UNIX Library - ${BOLD}ADD MODE${NORMAL}"
        tput cup 7 20; echo "Title: "
        tput cup 9 20; echo "Author: "
        tput cup 11 20; echo "Category: "
        tput cup 12 20; echo "sys: system, ref: reference, tb: textbook"

        tput cup 7 30; read TITLE
        tput cup 9 30; read AUTHOR
        tput cup 11 30; read CATEGORY
        STATUS="in"
        echo ":$TITLE:$AUTHOR:$CATEGORY:$STATUS:$BNAME:$DATE" >> library
        tput cup 14 10; printf "Any more to add? (Y)es or (N)o > "
        read ANSWER
        case $ANSWER in
            [Yy])ANSWER=y;;
            *)ANSWER=n;;
        esac
    done
    return 0
}

# 更新记录
UPDATE()
{
    # save original IFS
    ORI_IFS="$IFS"

    # 清空变量
    unset TITLE AUTHOR CATEGORY STATUS BNAME DATE
    unset NEW_STATUS

    # 是否继续循环
    ANSWER=y
    while [ "$ANSWER" = y ]; do
        tput clear
        tput cup 3 5; printf "Enter the title> "
        read bookinfo
        grep -i ":$bookinfo:" library > TMP
        if [ -s TMP ]; then
            IFS=":"
            read tmp TITLE AUTHOR CATEGORY STATUS BNAME DATE < TMP
            tput cup 5 10; echo "UNIX Library - ${BOLD}UPDATE STATUS MODE${NORMAL}"
            tput cup 7 20; echo "Title: "
            tput cup 8 20; echo "Author: "
            tput cup 9 20; echo "Category: "
            tput cup 10 20; echo "Status: "

            # expand category
            case $CATEGORY in
                [Ss][Yy][Ss])word=textbook;;
                [Rr][Ee][Ff])word=reference;;
                [Tt][Bb])word=textbook;;
                *)word=unknown;;
            esac

            tput cup 7 30; echo $TITLE
            tput cup 8 30; echo $AUTHOR
            tput cup 9 30; echo $word
            tput cup 10 30; echo $STATUS

            # new status
            if [ "$STATUS" = "in" ]; then
                NEW_STATUS="out"
                DATE=`date +%D`
                tput cup 11 15; echo "New status: "
                tput cup 11 30; echo $NEW_STATUS
                tput cup 12 10; printf "Checked out by: "
                tput cup 12 30; read BNAME
                tput cup 12 30; echo $BNAME
                tput cup 13 20; echo "Date: "
                tput cup 13 30; echo $DATE

                # any more to update
                tput cup 15 10
            else
                NEW_STATUS="in"
                tput cup 11 10; echo "Checked out by: "
                tput cup 11 30; echo $BNAME
                tput cup 12 20; echo "Date: "
                tput cup 12 30; echo $DATE
                tput cup 14 15; echo "New status: "
                tput cup 14 30; echo $NEW_STATUS
                unset BNAME DATE

                # any more to update
                tput cup 15 10
            fi

            # update
            grep -vi ":$bookinfo:" library > TMP_DELETE
            mv TMP_DELETE library
            echo ":$TITLE:$AUTHOR:$CATEGORY:$NEW_STATUS:$BNAME:$DATE" >> library

        else
            tput cup 7 10
            echo "$bookinfo notfound"

            # any more to update
            tput cup 9 10
        fi
        rm TMP

        printf "Any more to update? (Y)es or (N)o> "
        read ANSWER
        case $ANSWER in
            [Yy])ANSWER=y;;
            *)ANSWER=n;;
        esac
    done
    IFS="$ORI_IFS"
    return 0
}

# 显示
DISPLAY()
{
    # save original IFS
    ORI_IFS="$IFS"

    unset TITLE AUTHOR
    ANSWER=y
    while [ "$ANSWER" = y ]; do
        tput clear
        tput cup 3 5; printf "Enter the title> "
        read bookinfo
        grep -i ":$bookinfo:" library > TMP
        if [ -s TMP ]; then
            IFS=":"
            read tmp TITLE AUTHOR CATEGORY STATUS BNAME DATE < TMP
            tput cup 5 10; echo "UNIX Library - ${BOLD}DISPLAY MODE${NORMAL}"
            tput cup 7 20; echo "Title: "
            tput cup 8 20; echo "Author: "
            tput cup 9 20; echo "Category: "
            tput cup 10 20; echo "Status: "

            # expand category
            case $CATEGORY in
                [Ss][Yy][Ss])word=textbook;;
                [Rr][Ee][Ff])word=reference;;
                [Tt][Bb])word=textbook;;
                *)word=unknown;;
            esac

            tput cup 7 30; echo $TITLE
            tput cup 8 30; echo $AUTHOR
            tput cup 9 30; echo $word
            tput cup 10 30; echo $STATUS

            # any more to display
            tput cup 12 10
        else
            tput cup 7 10
            echo "$bookinfo notfound"

            # any more to display
            tput cup 9 10
        fi

        rm TMP

        # 在下一次循环前清空bookinfo变量
        unset bookinfo
        printf "Any more to display? (Y)es or (N)o> "
        read ANSWER
        case $ANSWER in
            [Yy])ANSWER=y;;
            *)ANSWER=n;;
        esac
    done

    IFS="$ORI_IFS"
    return 0
}

# 删除
DELETE()
{
    # save original IFS
    ORI_IFS="$IFS"

    unset TITLE AUTHOR
    ANSWER=y
    while [ "$ANSWER" = y ]; do
        tput clear
        tput cup 3 5; printf "Enter the author/title> "
        read bookinfo
        grep -i ":$bookinfo:" library > TMP
        if [ -s TMP ]; then
            IFS=":"
            read tmp TITLE AUTHOR CATEGORY STATUS BNAME DATE < TMP
            tput cup 5 10; echo "UNIX Library - ${BOLD}DELETE MODE${NORMAL}"
            tput cup 7 20; echo "Title: "
            tput cup 8 20; echo "Author: "
            tput cup 9 20; echo "Category: "
            tput cup 10 20; echo "Status: "

            # expand category
            case $CATEGORY in
                [Ss][Yy][Ss])word=textbook;;
                [Rr][Ee][Ff])word=reference;;
                [Tt][Bb])word=textbook;;
                *)word=unknown;;
            esac

            tput cup 7 30; echo $TITLE
            tput cup 8 30; echo $AUTHOR
            tput cup 9 30; echo $word
            tput cup 10 30; echo $STATUS

            tput cup 12 20; printf "Delete this book? (Y)es or (N)o> "
            read confirm
            if [ "$confirm" = Y -o "$confirm" = y ]; then
                grep -vi ":$bookinfo:" library > TMP
                mv TMP library
            fi
            # any more to delete
            tput cup 14 10
        else
            tput cup 7 10
            echo "$bookinfo not found"
            # any more to delete
            tput cup 9 10
        fi
        [ -s "./TMP" ] && rm TMP

        # 在下次循环前清空bookinfo变量
        unset bookinfo
        printf "Any more to delete? (Y)es or (N)o> "
        read ANSWER
        case $ANSWER in
            [Yy])ANSWER=y;;
            *)ANSWER=n;;
        esac
    done

    IFS="$ORI_IFS"
    return 0
}


# menu
while true; do
    tput clear
    tput cup 5 10
    printf "UNIX Library - ${BOLD}EDIT MENU${NORMAL}\n"
    tput cup 7 20
    printf "0: ${BOLD}RETURN${NORMAL} to the main menu\n"
    tput cup 9 20
    printf "1: ${BOLD}ADD${NORMAL}\n"
    tput cup 11 20
    printf "2: ${BOLD}UPDATE STATUS${NORMAL}\n"
    tput cup 13 20
    printf "3: ${BOLD}DISPLAY${NORMAL}\n"
    tput cup 15 20
    printf "4: ${BOLD}DELETE${NORMAL}\n"

    tput cup 17 10
    printf "Enter your choice> "
    read CHOICE

    case $CHOICE in
        0)tput clear; exit 0;;
        1)ADD;;
        2)UPDATE;;
        3)DISPLAY;;
        4)DELETE;;
        *)./error.sh 20 10;;
    esac
done

