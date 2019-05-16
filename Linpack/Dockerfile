FROM ubuntu

RUN apt-get update
RUN apt-get install -y libgomp1 numactl
ADD linpack_10.3.4/benchmarks/linpack /
CMD numactl --physcpubind=all --localalloc /xlinpack_xeon64
