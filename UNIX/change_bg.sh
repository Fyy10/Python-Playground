#! /bin/sh
# 以"作为cut的分隔符
bgLink=`curl cn.bing.com | grep -e "link id=\"bgLink\"" | cut -f6 -d\"`
wget "https://cn.bing.com$bgLink"

# change wallpaper
# filename = bgLink
gsettings set org.gnome.desktop.background picture-uri "$PWD/$bgLink"
