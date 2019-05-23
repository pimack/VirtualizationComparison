yum update
yum install -y numactl wget gcc libgomp1
cd VirtualizationComparison/Stream
make
wget http://registrationcenter-download.intel.com/akdlm/irc_nas/2169/l_lpk_p_10.3.4.007.tgz
tar zxvf l_lpk_p_10.3.4.007.tg
