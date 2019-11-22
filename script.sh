#!/bin/bash
PYTHON="python3 main.py -m test compare"
for i in $(seq 1 10);
do
    $PYTHON
done