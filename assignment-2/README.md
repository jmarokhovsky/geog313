# Assignment 2

This folder contains the necessary components to make the graph for Assignment 2.

## Installation

Steps:
1. Pull this entire directory, make sure it contains the `Dockerfile`, the `environment.yml` file, and `a2_final.ipynb`
2. Build the container with the command:
```
> docker build -t assignment-2 .
```
3. Start the container with the command:
```
> docker run -it -p 8888:8888 assignment-2
```
4. Go to the supplied link once jupyter notebooks has started on the container, and run the first step in `a2_final.ipynb`

