#!/bin/bash

# Load environment variables from the .env file
if [ -f .env ]; then
    export $(cat .env | grep -v '^#' | xargs)
fi

python3 src/main.py