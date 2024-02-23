# MetricInsights Backend

[![License](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

This is the Backend for MetricInsights. 
It is a flask application that is used to monitor the data from the computer and to send the data to the frontend.

You can find the frontend of the application [here](https://github.com/JamesWebb17/MetricInsight_FrontEnd)

This project is made by : Faucher Simon

Version : 1.0

## Summary

- [MetricInsights Backend](#metricinsights-frontend)
- [Summary](#summary)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Dependencies](#dependencies)
  - [Set up your environment](#Set-up-your-environment)
  - [Running the project](#running-the-project)
- [Organization](#organization)
  - [Directory structure](#directory-structure)
  - [Files](#files)
- [Docker](#docker)
  - [Build the image](#build-the-image)
  - [Run the container](#run-the-container)
  - [Stop the container](#stop-the-container)
  - [Remove the container](#remove-the-container)
  - [Remove the image](#remove-the-image)
- [Documentation](#documentation)
  - [Doxygen](#doxygen)
  - [API](#api)
- [License](#license)
- [Contact](#contact)
- [Acknowledgements](#acknowledgements)

## Installation

### Prerequisites

To install the project, you need to have Node.js installed on your computer.

### Dependencies

This is the list of the dependencies used in the project:

- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
- [Flask-Cors](https://flask-cors.readthedocs.io/en/latest/)
- [flask_sse](https://flask-sse.readthedocs.io/en/latest/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [Blueprint](https://flask.palletsprojects.com/en/2.0.x/blueprints/)
- [matplotlib](https://matplotlib.org/)

Version of the dependencies are specified in the [requirements.txt](./requirements.txt) file.

To install the dependencies, you need to run the following command in the [root](./) directory of the project:

```bash 
pip install -r requirements.txt
```

### Set up your environment

To set the project, you need to change the [.env](./.env) file in the [root](./) directory of the project.

The .env file should look like this:

```env
# File to store environment variables

# Server
PORT=
BACKEND_IP=
```

You have to write the IP and the port of the backend in the [.env](./.env) file.

Per default, the backend is running on the port 3001,
and the IP is set to localhost.

This is an example of the [.env](./.env) file:

```env
# File to store environment variables

# Server
PORT=3001
BACKEND_IP=10.10.10.11
```

### Running the project

To run the project, you have 2 options:

- Run the project with python3 with the command line in the [root](./) directory of the project.

  ```bash
  sudo python3 ./app.py
  ```
  
  You should see the following message in the console:
  
  ```bash
  BACKEND_IP: [Your IP]
  PORT: [Your Port]
   * Serving Flask app 'app'
     * Debug mode: on
  WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
     * Running on http://[Your IP]:[Your Port]/ 
  Press CTRL+C to quit
     * Restarting with stat
  BACKEND_IP: [Your IP]
  PORT: [Your Port]
     * Debugger is active!
     * Debugger PIN: 621-764-549
  ```
  
  This option will run with the parameters set in the [.env](./.env) file.
  
- Run the project with flask with the command line in the [root](./) directory of the project.
    
  ```bash
  sudo flask run --host [Your IP] --port [Your Port]
  ```

  You should see the following message in the console:
  
  ```bash
  BACKEND_IP: [Your IP]
  PORT: [Your Port]
   * Serving Flask app 'app.py'
     * Debug mode: off
  WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
     * Running on http://[Your IP]:[Your Port]/
  Press CTRL+C to quit
  ```
  
  This option will run with the parameters set in the command line.


## Organization

### Directory structure

This is the directory structure of the project:

```
.
├── Documentation
│   ├── html
│   └── latex
├── MetricInsights
│   └── Arguments
│   │   ├── __init__.py
│   │   └── Arguments.py
│   └── CPU
│   │   ├── __init__.py
│   │   └── utilisation.py
│   └── GPU
│   │   ├── __init__.py
│   │   └── utilisation.py
│   └── Memory
│   │   ├── __init__.py
│   │   └── utilisation.py
│   └── Power
│   │   ├── __init__.py
│   │   └── utilisation.py
│   └── Read_File
│   │   ├── PID
│   │   │   ├── __init__.py
│   │   │   ├── gpu.py
│   │   │   ├── stat.py
│   │   │   └── statm.py
│   │   ├── __init__.py
│   │   ├── hwmon.py
│   │   ├── meminfo.py
│   │   ├── stat.py
│   │   └── uptime.py
│   └── Shared
│   │   ├── __init__.py
│   │   ├── flags.py
│   │   └── result.py
│   └── __init__.py
│   └── MetricInsights.py
│   └── README.md
├── routes
│   ├── __init__.py
│   ├── api.py
│   ├── contact.py
│   └── metricInsights.py
├── .env
├── .gitignore
├── app.py
├── Dockerfile
├── Doxyfile
├── LICENSE
├── README.md
└── requirements.txt
```

### Files

This is the list of the files in the project:

- [MetricInsights](./MetricInsights) : This folder contains the classes that are used to monitor the data from the computer.
- [routes](./routes) : This folder contains the routes of the api.
- [.env](./.env) : This file contains the environment variables of the project.
- [.gitignore](./.gitignore) : This file contains the files that are ignored by git.
- [app.py](./app.py) : This is the main file of the project.
- [Dockerfile](./Dockerfile) : This is the file to build the image of the project.
- [Doxyfile](./Doxyfile) : This is the file to generate the documentation of the project.
- [LICENSE](./LICENSE) : This is the license file of the project.
- [README.md](./README.md) : This is the file you are reading.

## Docker

### Build the image

To build the image, you need to run the following command in the [root](./) directory of the project:

```bash
docker build -t metricinsights-backend .
```

### Run the container

To run the container, you need to run the following command in the [root](./) directory of the project:

```bash
docker run -p 3001:3001 -d metricinsights-backend
```

### Stop the container

To stop the container, you need to run the following command in the [root](./) directory of the project:

```bash
docker stop [container_id]
```

### Remove the container

To remove the container, you need to run the following command in the [root](./) directory of the project:

```bash
docker rm [container_id]
```

## Remove the image

To remove the image, you need to run the following command in the [root](./) directory of the project:

```bash
docker rmi metricinsights-backend
```

## Documentation

### Doxygen

To generate the doxygen, you need to run the following command in the [root](./) directory of the project:

```bash
doxygen Doxyfile
```

The documentation will be generated in the [public/Documentation](./public/Documentation/Frontend) directory of the project.

### API

The API documentation is available in the [public/Documentation](./public/Documentation/Backend) directory of the project.

## License

This project is licensed under the CC License - see the [LICENSE](LICENSE) file for details.

## Contact

- Email : simon.faucher@etudiant.univ-rennes1.fr

## Acknowledgements


Thank to [Robin Gerzaguet](https://perso.univ-rennes1.fr/robin.gerzaguet/) whose enlightened advice helped me
to guide me through this project. Her expertise was a beacon throughout the process.

Thank to [Paul Bazerque](https://fr.linkedin.com/in/paul-bazerque) for its commitment to the project, as well as
his help with technical and directional choices.

Finally, I would also like to thank [Matthieu Gautier](https://people.irisa.fr/Matthieu.Gautier/), [Alice Chillet](https://www.linkedin.com/in/alice-chillet/) and [Emma Bothereau](https://www.linkedin.com/in/emma-bothereau/) for their contributions to this project.
