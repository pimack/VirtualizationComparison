# Comparison of Virtual Machine and Container Performance using CloudLab Infrastructure

This is a repository for automatic installation and benchmark testing for virtualization technologies using CloudLab, a cloud provider for academic research purposes. To realize the contents of this repository to their full potential, CloudLab is recommended (www.cloudlab.us).

How to use:
- Create an experiment profile on Cloudlab, using the Git Repo option and copy-pasting the link to this repository
- On the profile screen, at the bottom, click "Instantiate" on the Master branch.
- Continue instantiating and select the "CloudLab Wisconsin" cluster.
- Upon deployment (this will take a while), click on a node you wish to operate on and open the shell.

On subsequent runs after the profile is created, to run the experiment again, click "Start Experiment", select the created profile, and then press "Show Profile" to get back to step 2, then proceed as normal.

This set up creates three nodes, "KVM", "Singularity", and "Docker", each with their own implementation installed inside an ubuntu image.

Linpack and Stream benchmarks are available to test. These benchmarks are used to measure the performance of computers. This repository aims to explore the performance differences of containers and virtual machines using the same hardware.

To run benchmarks of choice, see the readme of the folders of each benchmark.

The benchmark code functions even without the CloudLab deployment; if needed, the code can be taken and implemented using a different infrastructure.

- KVM is currently not working due to installation issues.
