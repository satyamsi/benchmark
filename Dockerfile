# Source 
FROM ubuntu:14.04

# Maintainer 
MAINTAINER Satyam Sinha <satyam@gmail.com>

# Add local directory 
ADD workspace/benchmark/code aporeto-benchmark/
ADD workspace/benchmark/files aporeto-benchmark/files 

# Install pip's dependency: setuptools:
RUN apt-get install -y python
