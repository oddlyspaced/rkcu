#!/bin/bash

for index in {0..255..15}
do
    echo $index
    python gen_seq.py "L_$index.txt"
    sleep 0.1
done

for index in {0..255..15}
do
    echo $index
    python gen_seq.py "O_$index.txt"
    sleep 0.1
done

for index in {0..255..15}
do
    echo $index
    python gen_seq.py "D_$index.txt"
    sleep 0.1
done

for index in {0..255..15}
do
    echo $index
    python gen_seq.py "U_$index.txt"
    sleep 0.1
done