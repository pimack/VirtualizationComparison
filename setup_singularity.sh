wget https://github.com/sylabs/singularity/releases/download/2.4/singularity-2.4.tar.gz                        
tar zxvf singularity-2.4.tar.gz                                   
cd singularity-2.4                                               
./autogen.sh
./configure --prefix=/usr/local
make
sudo make install
. etc/bash_completion.d/singularity
sudo cp etc/bash_completion.d/singularity /etc/bash_completion.d/
sudo apt-get update && sudo apt-get install squashfs-tools 
