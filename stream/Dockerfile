FROM ubuntu

RUN apt-get update
RUN apt-get install -y libgomp1 numactl
ADD bin /
CMD numactl --physcpubind=all --localalloc /stream.exe
