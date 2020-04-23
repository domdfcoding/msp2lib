#!/bin/bash

# Script to make the manpage
# Currently it only calls sphinx (via make), but if any additional
# formatting is required it can be done through here.
cd manpage-builder || exit
make man

# Finally copy manpage out of build directory
cp build/man/* ../