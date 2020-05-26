#! /bin/bash
# 将用户输入添加到指定的文件中
# 如果文件不存在则创建，如果存在则追加
# 以空行表示输入结束，运行结束时显示文件内容

# 判断输入参数的个数
if [ ! "$#" = 1 ]; then
    echo "Usage: $0 filename"
    exit 1
fi

INPUT="emmm"

# 提示信息
echo "请输入任意一行文本，空行表示输入结束："

# 当输入不是空行时（INPUT非空时）
while [ -n "$INPUT" ]; do
    read INPUT
    [ -z "$INPUT" ] && break
    echo $INPUT >> $1
done

cat $1
exit 0
