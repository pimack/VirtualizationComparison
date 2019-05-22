To use linpack in Singularity, execute the following in the shell:
 - sudo singularity run /VirtualizationComparison/linpack/linpack.img
 
 To use linpack in Docker, execute the following in the shell:
 - sudo docker run -it --rm --privileged linpack
 
 The data is manually inputted. In order to achieve the maximum capabilities of the test machine, it is recommended to work with large numbers.
 The recommended setup is
 - Equations to solve: 45000
 - Leading Array: 45000
 - Trials to run: 10
 - Data Alignment: 1
 
 This can take up to 40 minutes to compute.
