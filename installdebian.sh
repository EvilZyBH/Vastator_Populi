#!/bin/bash
sudo apt-get update && apt-get upgrade -y
sudo apt-get install python -y
unzip phonia.zip
rm phonia.zip
rm installdebian.sh
rm installarch.sh