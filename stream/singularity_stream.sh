sudo git clone https://github.com/pmackevicius/VirtualizationComparison
cd VirtualizationComparison/stream
make
sudo singularity build stream.img Singularity.recipe
