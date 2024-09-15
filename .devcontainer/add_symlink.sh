#!/bin/bash

# Makes the device available in the container with the same name
ln -s /dev/ttyUSB0 /dev/arduino &&
echo "Symlink created for arduino device"
exec "$@"