set -x

sudo git clone -b docker --single-branch https://github.com/AS805456/cluster-template/
cd cluster-template/linpack
sudo wget http://registrationcenter-download.intel.com/akdlm/irc_nas/2169/l_lpk_p_10.3.4.007.tgz
sudo tar zxvf l_lpk_p_10.3.4.007.tgz
sudo docker build -t linpack .
