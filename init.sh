#!/bin/sh
for i in {1..25}
do
    mkdir Day$i
    cd Day$i
    touch input.txt
    touch test_input.txt
    for h in {1..2}
    do
    echo "# f = open(\"input.txt\", 'r')
f = open(\"test_input.txt\", 'r')
input = f.read()

for line in input:
    " > part$h.py
    done
    cd ..
done