set -x
sudo git clone https://github.com/pmackevicius/VirtualizationComparison
cd VirtualizationComparison/stream
sudo make
sudo docker build -t stream .
