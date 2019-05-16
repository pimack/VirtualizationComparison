set -x

sudo apt-get update
sudo apt-get install -y qemu-kvm libvirt-bin ubuntu-vm-builder bridge-utils virt-manager libosinfo-bin libguestfs-tools virt-top
sudo adduser `id -un` libvirtd
sudo wget http://releases.ubuntu.com/16.04/ubuntu-16.04.6-server-amd64.iso
sudo qemu-img create -f qcow2 ubuntu.qcow2 20G
sudo git clone https://github.com/pmackevicius/VirtualizationComparison
sudo virt-install --name test \
--connect qemu:///system \
--ram 16384 \
--disk path=ubuntu.qcow2,format=qcow2,bus=virtio,size=8 \
--vcpus 4 \
--os-type linux \
--network network=default \
--graphics none \
--console pty,target_type=serial \
--location=ubuntu-16.04.6-server-amd64.iso \
--extra-args 'console=ttyS0'
