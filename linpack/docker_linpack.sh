set -x

sudo git clone https://github.com/pimack/VirtualizationComparison
cd VirtualizationComparison/linpack
sudo wget http://registrationcenter-download.intel.com/akdlm/irc_nas/2169/l_lpk_p_10.3.4.007.tgz
sudo tar zxvf l_lpk_p_10.3.4.007.tgz
sudo docker build -t linpack .
