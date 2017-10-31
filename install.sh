#!/bin/sh

sudo cp libs/libsgfdu03.so /usr/local/lib
sudo cp libs/libsgfpamx.so /usr/local/lib
sudo cp libs/libsgfplib.so /usr/local/lib
sudo cp libs/libsgnfiq.so /usr/local/lib
sudo cp libs/libpysgfplib.so /usr/local/lib
sudo cp libs/libsgfdu06.so /usr/local/lib

sudo ldconfig /usr/local/lib