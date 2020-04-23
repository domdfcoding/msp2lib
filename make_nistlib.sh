#!/bin/bash

echo "Running Lib2NIST"

# Run lib2nist
xvfb-run wine cmd /C "z:\lib2nist\lib2nist.exe /log1 z:\lib2nist.log z:\convert.ini z:\input\input.msp z:\output\ "

# Change ownership of output lib
chown -R $USER_UID:$USER_UID /output/input

echo "Lib2NIST Log:"
cat /lib2nist.log

echo "\nDone!"

