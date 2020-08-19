Based on the gem5 repository in google source with commit: "9fc9c67b4242c03f165951775be5cd0812f2a705"

```sh
git clone https://gem5.googlesource.com/public/gem5
git checkout 9fc9c67b4242c03f165951775be5cd0812f2a705
```

## Build
```scons build/NULL/gem5.debug PROTOCOL=Garnet_standalone```
## Topology
Our implementation of Fat-Tree, 3D-Hyper-LIONS, and 3D-Hyper-FlexLIONS topologies are located in: ``configs/topologies/`` directory
## Run
Using FatTree.sh, HyperLION.sh, and HyperflexLION.sh

----------------------------------------
This is the gem5 simulator.

The main website can be found at http://www.gem5.org

A good starting point is http://www.gem5.org/about, and for
more information about building the simulator and getting started
please see http://www.gem5.org/documentation and
http://www.gem5.org/documentation/learning_gem5/introduction.

To build gem5, you will need the following software: g++ or clang,
Python (gem5 links in the Python interpreter), SCons, SWIG, zlib, m4,
and lastly protobuf if you want trace capture and playback
support. Please see http://www.gem5.org/documentation/general_docs/building
for more details concerning the minimum versions of the aforementioned tools.

Once you have all dependencies resolved, type 'scons
build/<ARCH>/gem5.opt' where ARCH is one of ALPHA, ARM, NULL, MIPS,
POWER, SPARC, or X86. This will build an optimized version of the gem5
binary (gem5.opt) for the the specified architecture. See
http://www.gem5.org/documentation/general_docs/building for more details and
options.

The basic source release includes these subdirectories:
   - configs: example simulation configuration scripts
   - ext: less-common external packages needed to build gem5
   - src: source code of the gem5 simulator
   - system: source for some optional system software for simulated systems
   - tests: regression tests
   - util: useful utility programs and files

