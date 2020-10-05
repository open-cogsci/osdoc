#!/bin/bash
BRANCH=`git rev-parse --abbrev-ref HEAD`
echo "Building documentation for $BRANCH"
rm -Rf output/$BRANCH
mkdir output/$BRANCH
cp -R static/* output/$BRANCH
python3 build-menu.py --publish
pelican -s publishconf.py
cp output/$BRANCH/index/index.html output/$BRANCH/index.html
python3 parse-theme.py
