
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
    node = request.RawPC("KVM")
    node.hardware_type = "c220g2"
    node.routable_control_ip = "true"
    node.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU16-64-STD"
    iface = node.addInterface("if" + str(i))
    iface.component_id = "eth1"
    iface.addAddress(pg.IPv4Address(prefixForIP + str(i + 1), "255.255.255.0"))
    link.addInterface(iface)
    
    
    #node.addService(pg.Execute(shell="sh", command="sudo bash /local/repository/setup_kvm.sh"))
    
  elif i == 1:
    node = request.RawPC("Docker")
    node.hardware_type = "c220g2"
    node.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU16-64-STD"
    node.routable_control_ip = "true"
    
    iface = node.addInterface("if" + str(i))
    iface.component_id = "eth1"
    iface.addAddress(pg.IPv4Address(prefixForIP + str(i + 1), "255.255.255.0"))
    link.addInterface(iface)
    
    
    node.addService(pg.Execute(shell="sh", command="sudo bash /local/repository/setup_docker.sh"))
    node.addService(pg.Execute(shell="sh", command="sudo bash /local/repository/linpack/docker_linpack.sh"))
  
  elif i == 2:
    node = request.RawPC("Singularity")
    node.hardware_type = "c220g2"
    node.routable_control_ip = "true"
    
    node.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU16-64-STD"
    iface = node.addInterface("if" + str(i))
    iface.component_id = "eth1"
    iface.addAddress(pg.IPv4Address(prefixForIP + str(i + 1), "255.255.255.0"))
    link.addInterface(iface)
    
    
    node.addService(pg.Execute(shell="sh", command="sudo bash /local/repository/setup_singularity.sh"))
    node.addService(pg.Execute(shell="sh", command="sudo bash /local/repository/linpack/singularity_linpack.sh"))

    
  
pc.printRequestRSpec(request)
