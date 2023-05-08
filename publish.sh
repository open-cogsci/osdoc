#!/bin/bash
BRANCH=`git rev-parse --abbrev-ref HEAD`
echo "Building documentation for $BRANCH"
rm -Rf output/$BRANCH
mkdir output/$BRANCH
python build-menu.py --publish
cp -R static/* output/$BRANCH
pelican -s publishconf.py
cp output/$BRANCH/index/index.html output/$BRANCH/index.html
cp output/$BRANCH/fr/index/index.html output/$BRANCH/fr/index.html
cp output/$BRANCH/zh/index/index.html output/$BRANCH/zh/index.html
cp output/$BRANCH/de/index/index.html output/$BRANCH/de/index.html
cp output/$BRANCH/es/index/index.html output/$BRANCH/es/index.html
python parse-theme.py
