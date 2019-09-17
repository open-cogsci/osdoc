#!/bin/bash
BRANCH=3.2
rm -Rf output/*
mkdir output
mkdir output/$BRANCH
cp -R static/* output/$BRANCH
python3 build-menu.py --publish
pelican -s publishconf.py
cp output/$BRANCH/index/index.html output/$BRANCH/index.html
python3 parse-theme.py
