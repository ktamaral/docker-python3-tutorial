# docker-python3-tutorial

## Introduction

A simple tutorial on how to build a dockerized python environment

## Technology Stack
##### Scripting
Python

##### Development Operations
Docker Compose

## Local Development Environment Setup Instructions

### 1: Clone the repository to a local directory
git clone git@github.huit.harvard.edu:LTS/nrs-resolver-test-client.git

### 2: Create a config file

##### Create config
- Make a copy of the config example file `./app/config-example.txt`
- Rename the file and move it to the config directory `./app/config/config.py`
- Replace placeholder values as necessary

The config file is imported into the main file `run.py` to make the config values accessible.

```
# Append config directory to path
sys.path.append('./config')
# Import config
from config import *
```

*Note: The config file is specifically excluded in .gitignore and .dockerignore, since it may contain hostnames and credentials it should NOT ever be committed to a repository*

### 3: Start Docker Compose

##### START

This command builds all images and runs all containers specified in the docker-compose-local.yml configuration.

```
docker-compose -f docker-compose-local.yml up -d
```

##### Check running containers
Run docker ps to view a list of currently running containers

```
docker ps
```

The terminal output should display the config values and a new log file should be created in the `./logs` directory on the local machine.

```
EXAMPLE CLASS FUNCTION
2020-08-04 16:51:56,747 [INFO]: example_class.py(example_class_function:29) >> HOSTNAME: test.example.com
2020-08-04 16:51:56,748 [INFO]: example_class.py(example_class_function:30) >> MAX ROWS: 100
```

##### Run docker exec to execute a shell in the container by name

Open a shell using the exec command to access the docker-python3-tutorial container.

```
docker exec -it docker-python3-tutorial bash
```

### 4: Run script

Run the main python script runner inside the container.

```
appuser@37cdfcc27cd5:~$ python run.py
```

### 5: Open logs

##### Open reports and logs
- Open the `./logs/` directory to view the script logs.
- Read [Docker volumes](#docker-volumes) for more information on the volume configuration.

A custom logger configuration for the logging module is in the utils directory. The provided example configuration writes output to a directory inside the container at a set interval with a specified format and filename.

- `./utils/logger.py`.

The custom logger is imported and initialized in the main file `run.py`.

```
# Import custom logger configuration
from utils import logger as loggerutils
# Initialize custom logger
logger = loggerutils.setup_custom_logger('root')
```

The custom logger is imported and called in the example_class file.

```
import logging
logger = logging.getLogger('root')
```

```
logger.info('HOSTNAME: {}'.format(self.hostname))
logger.info('MAX ROWS: {} '.format(self.max_rows))
```

### 6: Stop Docker Compose

##### STOP

This command stops all containers specified in the docker-compose-local.yml configuration.

```
docker-compose -f docker-compose-local.yml stop
```

##### REMOVE

This command removes all stopped containers specified in the docker-compose-local.yml configuration. This is recommended to run each time after stopping to remove stopped containers.

```
docker-compose -f docker-compose-local.yml rm -f
```

## Docker Compose

### Docker volumes
The docker-compose-local.yml file is configured to mount local host directories (the local computer filesystem) into the container (the container filesystem). Any changes written to files inside mounted directories on the host system will be updated inside the container and vise versa. The Docker Compose configuration property is `volumes:` and is written as `'${HOST_PATH}:${CONTAINER_PATH}'`.

```
volumes:
  - './app/:/home/appuser/'
  - './logs/:/home/logs/'
```

The `./app/` directory on the local host filesystem is mounted to `/home/appuser/` inside the container. Any updates made to files inside the `./app/` directory on the local host will be updated inside the container immediately and vise versa. A common use case is to update the app code on the local host computer using a code editing program and the updates will be applied inside the container automatically. That makes is easy to make changes to the code and run the script quickly.

```
- './app/:/home/appuser/'
```

The `./logs/` directory on the local filesystem is mounted to `/home/logs/` inside the container. The script runs and writes the output to the `/home/logs/` directory inside the container, and the updates appear in the `./logs/` directory on the local host.

```
- './logs/:/home/logs/'
```