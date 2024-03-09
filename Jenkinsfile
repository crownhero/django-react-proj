# Use the latest Jenkins image as the base image
FROM jenkins/jenkins:latest

# Switch to root user for installation
USER root

# Install required dependencies
RUN apt-get update && \
    apt-get install -y unzip rsync nano python3-pip && \
    apt-get install -y curl && \
    apt-get clean

# Install AWS CLI
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
    unzip awscliv2.zip && \
    ./aws/install

# Install pip for Python
RUN apt install -y  pipx

# Install and upgrade awsebcli
#RUN pip install awsebcli --upgrade --user --break-system-packages

ENV PATH="/var/jenkins_home/.local/bin:$PATH"

# Switch back to the Jenkins user
USER jenkins

RUN pipx install awsebcli

#this should be installed by the Jenkins user
