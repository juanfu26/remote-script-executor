# Remote Script Executor
Utility to Execute scripts remotely through a ssh connection

# :clipboard: Requirements
- Docker

# :rocket: How to use


## Update env.list 
Update the env.list file with your prefered values. For example:

- IP of the remote host. Use host.docker.internal for execute on the host
  - `SSH_IP=host.docker.internal`

- Port of the ssh server service on the remote host.
  - `SSH_PORT=22`

- Credentials for the ssh connection.
  - `SSH_USERNAME=root`
  - `SSH_PASSWORD=pass`

- Set of environment for activations of the scripts. 
  - `GET_IPS=true`

> **_NOTE:_** I plan to expand the list of available scripts as I find them useful.


##  Build the docker image
The ci.sh script is prepared for doing a cross-compilation in order to make the docker image available for amd64 and arm64 environments. 

You can pulled directly from DockerHub: [juanfu26/remote-script-executor](https://hub.docker.com/r/juanfu26/remote-script-executor)


## Run it
Using th docker-compose yaml file:
~~~
docker-compose --env-file env.list up
~~~

Running the container directly with the env file. 
~~~
docker run --env-file ./env.list --name=remote-script-executor --add-host "host.docker.internal:host-gateway" juanfu26/remote-script-executor:latest 
~~~

> **_NOTE:_** Nake sure to update the values of the environment variables defined in the env.list file.