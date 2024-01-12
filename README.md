# CompTools

handy tools for making my life easier.

## 1. run 
Purpose: This script facilitates the submission of Gaussian jobs on Expanse, a supercomputer cluster supported by XSEDE.

### Setup Instructions:
**Placement:** Place the script in your /home/bin directory. \
**Permission:** Grant execution permissions using the command:
```
chmod 755 ~/home/bin/run
```

After this, the command `run` will be ready for use.

### Submitting a Gaussian Job:
**Basic Submission:** To run a Gaussian job (e.g., test.gjf), use:
```
run test.gjf
```
This command auto-generates a `test.job` file based on the number of cores and memory specified in the Gaussian input file and executes it. The required allocations will be displayed on the screen. Note that the `%mem` in the input file has to be specified based on the unit of GB but not MB.

**Handling Memory Issues:**
Sometimes, simply submitting a job based on your Gaussian input requirements may be insufficient, as an "out of memory" error could occur. This error typically arises from the additional memory usage by the Gaussian software itself, especially in cases where your system is large and complex. To prevent this issue, use
```
run test.gjf l
```
For instance, if %mem=15GB is specified in test.gjf, the job file will request 15+1=16GB memory for task submission.

**Selecting Batch Groups:**
The default batch group is shared.
For debugging purposes, submit to the debug batch group using:
```
run test.gjf def debug
```
Refer to the [Expanse User Guide](https://www.sdsc.edu/support/user_guides/expanse.html) for more details. Note: Typically, the debug group is not used for Gaussian tasks.

When submitting a job on Expanse, it's often a good practice to consider setting the memory allocation about the number of cores required. A general guideline could be to **allocate twice the amount of memory in GB as the number of cores needed**. For example, if you need 8 cores, consider allocating 16GB of memory in your **job** file. 
