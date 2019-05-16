
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

link = request.LAN("lan")

for i in range(3):
  if i == 0:
    node = request.rawPC("KVM")
    node.hardware_type = "c220g2"
    node.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU16-64-STD"
    iface = node.addInterface("if" + str(i))
    iface.component_id = "eth1"
    iface.addAddress(pg.IPv4Address(prefixForIP + str(i + 1), "255.255.255.0"))
    link.addInterface(iface)
    node.routable_control_ip = "true"
    #node.addService(pg.Execute(shell="sh", command="sudo bash /local/repository/setup_kvm.sh"))
    
  elif i == 1:
    node = request.rawPC("Docker")
    node.hardware_type = "c220g2"
    node.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU16-64-STD"
    
    iface = node.addInterface("if" + str(i))
    iface.component_id = "eth1"
    iface.addAddress(pg.IPv4Address(prefixForIP + str(i + 1), "255.255.255.0"))
    link.addInterface(iface)
    node.routable_control_ip = "true"
    
    node.addService(pg.Execute(shell="sh", command="sudo bash /local/repository/setup_docker.sh"))
  elif i == 2:
    node = request.rawPC("Singularity")
    node.hardware_type = "c220g2"
    node.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU16-64-STD"
    iface = node.addInterface("if" + str(i))
    iface.component_id = "eth1"
    iface.addAddress(pg.IPv4Address(prefixForIP + str(i + 1), "255.255.255.0"))
    link.addInterface(iface)
    node.routable_control_ip = "true"
    
    node.addService(pg.Execute(shell="sh", command="sudo bash /local/repository/setup_singularity.sh"))

    
  
pc.printRequestRSpec(request)