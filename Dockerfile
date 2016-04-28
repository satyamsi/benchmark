# Source 
FROM ubuntu:14.04

# Maintainer 
MAINTAINER Satyam Sinha <satyam@gmail.com>

# Add local directory 
ADD code aporeto-benchmark/
ADD files aporeto-benchmark/files 

# Install pip's dependency: setuptools:
RUN apt-get install -y python

