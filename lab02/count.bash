#!/bin/bash
#Geun Jeon
#CS265 lab2 Q10

for i in *;do
wcOutput=$(wc -l -w "$i");
echo ""$i" "${wcOutput%%"$i"};
done
