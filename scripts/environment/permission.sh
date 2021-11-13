#!/bin/bash -x

PROJECT_DIR=../..

cd `dirname $0`
cd $PROJECT_DIR

if [ "$#" = 0 ]; then
    exit 1
fi

path="$1"

sudo chown -vR itk:itk "$path"
sudo find "$path" -type f -print | xargs chmod 664
sudo find "$path" -type d -print | xargs chmod 775

exit 0
