# Use Ubuntu as the base image
FROM ubuntu:latest

# Update ubuntu and install curl
RUN apt-get update
RUN apt-get install curl -y

# Install web file browswer
RUN curl -fsSL https://raw.githubusercontent.com/filebrowser/get/master/get.sh | bash

# Create a directory to share
RUN mkdir /shared

# Expose the Filebrowser port
EXPOSE 8080

# Start Samba
CMD ["filebrowser", "-a", "0.0.0.0", "-r", "/shared"]
