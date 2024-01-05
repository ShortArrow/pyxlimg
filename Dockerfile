FROM mcr.microsoft.com/vscode/devcontainers/python:3.10

# create a user
RUN useradd -ms /bin/bash who
RUN echo "who ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
WORKDIR /home/who
RUN cp /root/.bashrc /home/who/.bashrc
USER who

RUN pip install --upgrade pip && pip install poetry
