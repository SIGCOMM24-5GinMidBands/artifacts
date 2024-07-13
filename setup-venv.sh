#!/bin/bash

set -x

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
cd $SCRIPT_DIR

sudo apt-get update
sudo apt-get install -y python3-pip
sudo pip3 install virtualenv --break-system-packages
virtualenv venv