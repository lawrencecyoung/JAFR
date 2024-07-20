#!/bin/bash
HOME=/home/tests/test_users/oliver
export HOME
USER=oliver
export USER

for path in test_cases/oliver/* 
do
    python3 /home/jafr.py passwd < $path/test.in > $path/actual
    diff $path/test.out $path/actual
done


HOME=/home/tests/test_users/peter
export HOME
USER=peter
export USER

for path in test_cases/peter/* 
do
    python3 /home/jafr.py passwd < $path/test.in > $path/actual
    diff $path/test.out $path/actual
done

HOME=/home/tests/test_users/rebecca
export HOME
USER=rebecca
export USER

for path in test_cases/rebecca/* 
do
    python3 /home/jafr.py passwd < $path/test.in > $path/actual
    diff $path/test.out $path/actual
done




