# Container image that runs your code
FROM alpine:3.10

# Set workdir
WORKDIR /usr/src

# Copies your code file from your action repository to the filesystem path `/` of the container
COPY entrypoint.sh .

# Set entrypoint.sh to executable
RUN chmod +x /usr/src/entrypoint.sh

# Code file to execute when the docker container starts up (`entrypoint.sh`)
ENTRYPOINT ["/usr/src/entrypoint.sh"]
