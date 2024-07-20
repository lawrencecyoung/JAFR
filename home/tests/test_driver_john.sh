#!/bin/bash
HOME=/home/tests/test_users/john
export HOME
USER=john
export USER

for path in test_cases/john/* 
do
    python3 /home/jafr.py passwd < $path/test.in > $path/actual
    diff $path/test.out $path/actual
done

