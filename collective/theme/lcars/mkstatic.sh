#!/bin/bash

mkdir lcars
cd lcars
cp -r ../static/* .
find -name .svn -exec rm -rf {} \;
cd ..
zip -r lcars.zip lcars
rm -rf  lcars/
