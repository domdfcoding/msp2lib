#!/bin/bash

docker run \
  -it \
  --name=lib2nist-wine \
  --rm \
  -v ".:/input" \
  -v ".:/output" \
  --env USER_UID=$UID \
 domdfcoding/lib2nist-wine \
 /make_nistlib.sh
