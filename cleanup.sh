#!/bin/bash

# Perform cleanup after non-graceful shutdown
docker stop lib2nist-wine
docker container rm lib2nist-wine
docker system prune
