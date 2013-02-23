#!/bin/bash

# This script should install all dependencies for the project


# must be run as root
if [ `whoami` != "root" ]; then
  echo "This installation must be run as root."
  exit 1
fi

LOG=$PWD/_install.log
echo -n "" > $LOG

pip install -r requirements.txt

