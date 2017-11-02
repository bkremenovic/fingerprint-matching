#!/bin/sh

sudo cp $(dirname "$0")/libs/libsgfdu03.so /usr/local/lib
sudo cp $(dirname "$0")/libs/libsgfpamx.so /usr/local/lib
sudo cp $(dirname "$0")/libs/libsgfplib.so /usr/local/lib
sudo cp $(dirname "$0")/libs/libsgnfiq.so /usr/local/lib
sudo cp $(dirname "$0")/libs/libpysgfplib.so /usr/local/lib
sudo cp $(dirname "$0")/libs/libsgfdu06.so /usr/local/lib

sudo ldconfig /usr/local/lib
