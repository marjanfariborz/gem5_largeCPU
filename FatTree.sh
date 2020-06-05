#!/bin/bash 



count="0.1"
limit="1"
increment="0.1"

while [ "$(bc <<< "$count < $limit")" == "1"  ]; do
    echo "Start!"
    ./build/NULL/gem5.opt \
         -e -r --outdir ~/fattree_tornado/injectionrate_0$count \
        configs/example/garnet_synth_traffic.py  \
        --num-cpus=512 \
        --num-dirs=512 \
        --network=garnet2.0 \
        --topology=FatTree_sc20 \
        --sim-cycles=100000 \
        --garnet-deadlock-threshold=1000000 \
        --synthetic=tornado \
        --injectionrate=$count \
        --router-latency=1 \
        --link-latency=16 \
        --link-width-bits=512 &
    echo $count
    count=$(bc <<< "$count+$increment")
done


count="0.1"
limit="1"
increment="0.1"

while [ "$(bc <<< "$count < $limit")" == "1"  ]; do
    echo "Start!"
    ./build/NULL/gem5.opt \
         -e -r --outdir ~/fattree_tornado/injectionrate_0$count \
        configs/example/garnet_synth_traffic.py  \
        --num-cpus=512 \
        --num-dirs=512 \
        --network=garnet2.0 \
        --topology=FatTree_sc20 \
        --sim-cycles=100000 \
        --garnet-deadlock-threshold=1000000 \
        --synthetic=tornado \
        --injectionrate=$count \
        --router-latency=1 \
        --link-latency=16 \
        --link-width-bits=512 &
    echo $count
    count=$(bc <<< "$count+$increment")
done



count="0.1"
limit="1"
increment="0.1"

while [ "$(bc <<< "$count < $limit")" == "1"  ]; do
    echo "Start!"
    ./build/NULL/gem5.opt \
         -e -r --outdir ~/fattree_uniform/injectionrate_0$count \
        configs/example/garnet_synth_traffic.py  \
        --num-cpus=512 \
        --num-dirs=512 \
        --network=garnet2.0 \
        --topology=FatTree_sc20 \
        --sim-cycles=100000 \
        --garnet-deadlock-threshold=1000000 \
        --synthetic=uniform \
        --injectionrate=$count \
        --router-latency=1 \
        --link-latency=16 \
        --link-width-bits=512 &
    echo $count
    count=$(bc <<< "$count+$increment")
done
