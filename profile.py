import geni.portal as portal
import geni.rspec.pg as pg
import geni.rspec.igext as IG

pc = portal.Context()

request = pc.makeRequestRSpec()

tourDescription = \
"""
This profile provides nodes for virtualization (VMs) and containerization (container-based) technology testing with benchmarks.
Currently supports Singularity, Docker, and KVM technologies.
Currently supporting Linpack and RandomAccess benchmarks.
"""

tour = IG.Tour()
tour.Description(IG.Tour.TEXT,tourDescription)
request.addTour(tour)

prefixForIP = "192.168.1."

# Setup KVM node

node1 = request.RawPC("KVM")
node1.hardware_type = "c220g2"
node1.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU16-64-STD"

iface1 = node1.addInterface("if" + str(1))
iface1.component_id = "eth1"
iface1.addAddress(pg.IPv4Address(prefixForIP + str(1), "255.255.255.0"))

node1.addService(pg.Execute(shell="sh", command="sudo bash /local/repository/setup_kvm.sh"))

# Setup Docker node

node2 = request.RawPC("Docker")
node2.hardware_type = "c220g2"
node2.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU16-64-STD"

iface2 = node2.addInterface("if" + str(2))
iface2.component_id = "eth2"
iface2.addAddress(pg.IPv4Address(prefixForIP + str(2), "255.255.255.0"))

node2.addService(pg.Execute(shell="sh", command="sudo bash /local/repository/setup_docker.sh"))
node2.addService(pg.Execute(shell="sh", command="sudo bash /local/repository/linpack/docker_linpack.sh"))
node2.addService(pg.Execute(shell="sh", command="sudo bash /local/repository/stream/docker_stream.sh"))

# Setup Singularity node

node3 = request.RawPC("Singularity")
node3.hardware_type = "c220g2"
node3.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU16-64-STD"

iface3 = node3.addInterface("if" + str(3))
iface3.component_id = "eth3"
iface3.addAddress(pg.IPv4Address(prefixForIP + str(3), "255.255.255.0"))

node3.addService(pg.Execute(shell="sh", command="sudo bash /local/repository/setup_singularity.sh"))
node3.addService(pg.Execute(shell="sh", command="sudo bash /local/repository/linpack/singularity_linpack.sh"))
node3.addService(pg.Execute(shell="sh", command="sudo bash /local/repository/stream/singularity_stream.sh"))

link = request.LAN("lan")

#Interfaces are disabled due to instability of provisioning

#link.addInterface(iface1)
#link.addInterface(iface2)
#link.addInterface(iface3)
    
pc.printRequestRSpec(request)