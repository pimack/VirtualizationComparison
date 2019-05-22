set -x

sudo apt-get update
sudo apt-get install -y qemu-kvm libvirt-bin ubuntu-vm-builder bridge-utils virt-manager libosinfo-bin libguestfs-tools virt-top
sudo adduser $USER libvirtd
sudo wget http://centos.mirrors.hoobly.com/7.6.1810/isos/x86_64/CentOS-7-x86_64-Minimal-1810.iso
sudo qemu-img create -f qcow2 ubuntu.qcow2 20G
sudo git clone https://github.com/pimack/VirtualizationComparison
sudo virt-install --name test \
--connect qemu:///system \
--ram 16384 \
--disk path=ubuntu.qcow2,format=qcow2,bus=virtio,size=8 \
--vcpus 8 \
--os-variant=centos7.0 \
--network network=default \
--graphics none \
--console pty,target_type=serial \
--location=CentOS-7-x86_64-Minimal-1810.iso \
--initrd-inject VirtualizationComparison/Kickstarter.cfg \
--extra-args 'ks=file:/Kickstarter.cfg console=tty0 console=ttyS0' 
