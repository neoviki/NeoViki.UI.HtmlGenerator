#!/bin/bash
chmod +x ./examples/button/run.sh
cp ./examples/button/run.sh run.sh
for d in examples/* ; do
    echo "copy run.sh $d/run.sh"
    cp run.sh $d/run.sh
done 
rm run.sh
rm src/*.pyc 2> /dev/null 1> /dev/null
