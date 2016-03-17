#!/bin/bash

#set mode to output
for i in 0 1 2 3 4 5 6 7;
do gpio mode $i out;
done;

#turn GPIO off
for i in 0 1 2 3 4 5 6 7;
do gpio write $i 0;
done;
