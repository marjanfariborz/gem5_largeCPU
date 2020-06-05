#!/bin/bash 



count="0.1"
limit="1"
increment="0.1"

while [ "$(bc <<< "$count < $limit")" == "1"  ]; do
    echo "Start!"
    ./build/NULL/gem5.opt \
        -e -r --outdir ~/HyperLIONS_shuffle/injectionrate_0$count \
        configs/example/garnet_synth_traffic.py  \
        --num-cpus=128 \
        --num-dirs=128 \
        --network=garnet2.0 \
        --topology=HyperLIONS \
        --sim-cycles=100000 \
        --garnet-deadlock-threshold=1000000 \
        --synthetic=shuffle \
        --injectionrate=$count \
        --router-latency=1 \
        --link-latency=16 \
        --link-width-bits=1024 &
    echo $count
    count=$(bc <<< "$count+$increment")
done



count="0.1"
limit="1"
increment="0.1"

while [ "$(bc <<< "$count < $limit")" == "1"  ]; do
    echo "Start!"
    ./build/NULL/gem5.opt \
        -e -r --outdir ~/HyperLIONS_tornado/injectionrate_0$count \
        configs/example/garnet_synth_traffic.py  \
        --num-cpus=128 \
        --num-dirs=128 \
        --network=garnet2.0 \
        --topology=HyperLIONS \
        --sim-cycles=100000 \
        --garnet-deadlock-threshold=1000000 \
        --synthetic=tornado \
        --injectionrate=$count \
        --router-latency=1 \
        --link-latency=16 \
        --link-width-bits=1024 &
    echo $count
    count=$(bc <<< "$count+$increment")
done


count="0.1"
limit="1"
increment="0.1"

while [ "$(bc <<< "$count < $limit")" == "1"  ]; do
    echo "Start!"
    ./build/NULL/gem5.opt \
        -e -r --outdir ~/HyperLIONS_uniform/injectionrate_0$count \
        configs/example/garnet_synth_traffic.py  \
        --num-cpus=128 \
        --num-dirs=128 \
        --network=garnet2.0 \
        --topology=HyperLIONS \
        --sim-cycles=100000 \
        --garnet-deadlock-threshold=1000000 \
        --synthetic=uniform_random \
        --injectionrate=$count \
        --router-latency=1 \
        --link-latency=16 \
        --link-width-bits=1024 &
    echo $count
    count=$(bc <<< "$count+$increment")
done
