#!/bin/bash
 if [ "$(id -u)" != "0" ]; then
    echo "This script must be run as root" 1>&2
    exit 1
fi
if [ -z  "$1" ]; then
   PREFIX=/usr
else
    PREFIX=$1
fi

caja_git=$PREFIX/share/caja-git/
caja_git_file=$PREFIX/share/caja-python/extensions/git.py
icon_file=$PREFIX/share/icons/hicolor/scalable/status/caja-git-symbolic.svg

echo "Uninstalling caja-git"
for index in ${!files[*]}
do
    file=${files[$index]}
    if [ -f $file ]; then
        echo "${file} was removed successfully"
        rm -f $file
    fi
done
if [ -d $caja_git ]; then
    rm -rf $caja_git
    echo "${caja_git} was removed successfully"
fi
