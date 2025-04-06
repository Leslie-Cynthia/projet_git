#!/bin/bash

echo " Stopping any running Gunicorn servers..."

# Find and kill all gunicorn processes
PIDS=$(ps aux | grep gunicorn | grep -v grep | awk '{print $2}')

if [ -z "$PIDS" ]; then
    echo "No gunicorn processes found."
else
    kill $PIDS
    echo "Gunicorn processes killed: $PIDS"
fi
