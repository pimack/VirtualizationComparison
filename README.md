# Comparison of Virtual Machine and Container Performance using CloudLab Infrastructure

This is a repository for automatic installation and benchmark testing for virtualization technologies using CloudLab, a cloud provider for academic research purposes.
This repository aims to provide tools to explore the performance differences of containers and virtual machines using the same hardware.
To realize the contents of this repository to their full potential, using CloudLab is recommended (www.cloudlab.us).

## Getting Started

Create a CloudLab profile at www.cloudlab.us, if you do not have one already ("Request an Account").

- If you do not wish to use CloudLab, you can use the code available without CloudLab deployment - you may manually install Singularity, Docker, and KVM, and use the code in 'linpack' and 'stream' folders on your local machine.

### Prerequisites

If you are using CloudLab, you must be in a project profile that allows creation of new experiments.

If you do not have a project manager who can approve you to join an existing project, during your profile creation, select "Start a New Project". Note that you will need to be approved before being able to start experiments.

### Installing

After creating a profile and gaining access to starting new experiments,

- Create an experiment profile on Cloudlab, using the Git Repo option and copy-pasting the link to this repository (https://github.com/pimack/VirtualizationComparison)
- On the profile screen, at the bottom, click "Instantiate" on the Master branch.
- Continue instantiating and select the "CloudLab Wisconsin" cluster. This cluster contains the hardware nodes used in this profile.
- Upon deployment (this will take a while), click on a node you wish to operate on and open the shell.

**Note: the node setup uses c220g2 hardware specified in http://docs.cloudlab.us/hardware.html under "11.2 CloudLab Wisconsin". Depending on the server load, these nodes might be unavailable.
To fix this issue, in the file 'profile.py' of this repository, change every appearance of the line**

> x.hardware_type = "c220g2"
 
**to a different hardware type. You can find all available nodes and server load at https://www.cloudlab.us/resinfo.php (login required)**

On subsequent runs after the profile is created, to run the experiment again, click "Start Experiment", select the created profile, and then press "Show Profile" to get back to step 2, then proceed as normal.

This setup creates three nodes, "KVM", "Singularity", and "Docker", each with their own implementation installed inside an ubuntu image. The KVM installation uses CentOS-7 operating system.

Linpack and Stream benchmarks are available to test. These benchmarks are used to measure the performance of computers. The linpack benchmark measures how fast a computer can solve a system of dense linear equations, denoted in FLOPS.
Stream benchmark measures the memory bandwidth of the computer, using 'Copy', 'Scale', 'Add' and 'Triad' parameters to evaluate the bandwidth in MB/s.

## Running The Tests

The benchmark code functions even without the CloudLab deployment; if needed, the code can be taken and implemented using a different infrastructure.

When running linpack, the parameters have to be manually inputted. 
In order to achieve the maximum capabilities of the test machine, it is recommended to work with large numbers. The recommended setup is:

* Equations to Solve: 45000
* Leading Array: 45000
* Trials to run: 10
* Data alignment: 1

### Docker 

Docker is automatically installed right after node deployment. Access the shell of the node labeled "Docker".

To run linpack on Docker, execute the following in the shell:

> sudo docker run -it --rm --privileged linpack
 
To run stream on Docker, execute the following in the shell:

> sudo docker run -it --rm --privileged stream
 
### Singularity

Singularity is automatically installed right after node deployment. Access the shell of the node labeled "Singularity".

To run linpack on Singularity, execute the following in the shell:

> sudo singularity run /VirtualizationComparison/linpack/linpack.img
 
To run stream on Singularity, execute the following in the shell:

> sudo singularity run /VirtualizationComparison/stream/stream.img
 
### KVM

KVM is automatically installed right after node deployment using a kickstarter file. Access the shell of the node labeled "KVM". However, CloudLab does not add the KVM service (execute the install scripts) until after the node is deployed.
This is not a problem with Singularity or Docker, as the installation is quick; KVM installation may take up to 30 minutes, and it is not visible in the shell. If you instead would prefer seeing the KVM installation, do the following:

 * In the file python.py, comment out (or remove) the following line before deployment: 
  
> node1.addService(pg.Execute(shell="sh", command="sudo bash /local/repository/setup_kvm.sh"))

 * Execute the following command in the shell:
 
> sudo bash /local/repository/setup_kvm.sh

If you opted out of observing the installation, you can check the status of the virtual machine with 

> sudo virsh list
 
After the installation, run

> sudo virsh console test
 
and login into the VM using username: user & password: root. Run the following inside the KVM:
    
> sudo yum update
 
> sudo yum install git
 
> sudo git clone https://github.com/pimack/VirtualizationComparison
 
> sudo VirtualizationComparison/inside_kvm.sh
 
This will run the script to install the remaining materials.

To run stream on KVM, execute the following:

> sudo VirtualizationComparison/stream/stream.exe
 
To run linpack on KVM, execute the following:

> sudo VirtualizationComparison/stream/linpack_10.3.4/benchmarks/linpack/xlinpack_xeon64
 
## Built With

* CloudLab - Cloud provider for academic research
* Docker - PaaS and SaaS OS-level virtualization software
* Singularity - OS-level virtualization sofware#
* Python and Shell - scripts for CloudLab deployment and installation


## Acknowledgments

 * Motivation paper - IBM's "An updated performance comparison of virtual machines and Linux containers"
 * Modified code for stream - https://github.com/thewmf/kvm-docker-comparison (Motivation paper code repository)
