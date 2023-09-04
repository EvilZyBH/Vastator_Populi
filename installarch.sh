#!/bin/bash
sudo pacman -Syuu
sudo pacman -S python -y
unzip phonia.zip
rm phonia.zip
rm installdebian.sh
rm installarch.sh