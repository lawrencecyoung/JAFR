#!/bin/bash
HOME=/home/tests/test_users/noah
export HOME
USER=noah
export USER

for path in test_cases/noah/* 
do
    python3 /home/jafr.py passwd < $path/test.in > $path/actual
    diff $path/test.out $path/actual
done

