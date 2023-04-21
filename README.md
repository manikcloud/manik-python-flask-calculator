# Manik Python Flask Calculator

Manik Python Flask Calculator is a simple web application that allows users to perform basic arithmetic operations such as addition, subtraction, multiplication, and division. The application is built using Python and Flask, and it can be easily deployed using Docker.

## Features

- Perform addition, subtraction, multiplication, and division operations
- Responsive web interface using Bootstrap
- Error handling for invalid inputs
- Docker support for easy deployment
- Kenkins Job 
- Docker hub 
- Somoke Test 

## Installation

### Prerequisites

- Docker installed on your system

### Steps

0. Add the Ubuntu user to the Docker group by running the following command:

```
sudo usermod -aG docker ubuntu
```
- This will grant the Ubuntu user permission to run Docker commands without using sudo.

1. Clone the repository:

```
git clone https://github.com/yourusername/manik-python-flask-calculator.git

```
* Navigate to the project directory:


```
cd manik-python-flask-calculator
```
Build the Docker image & Run the Docker container::
```
docker build -t manik-flask-calculator .

docker run -d -p 5000:5000 --name manik-flask-calculator-container 
manik-flask-calculator

```
* Access the application in your browser at http://localhost:5000 (replace localhost with the appropriate IP address if you're running the Docker container on a remote server).

## Most common error and resolution 

Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Get "http://%2Fvar%2Frun%2Fdocker.sock/v1.24/containers/json": dial unix /var/run/docker.sock: connect: permission denied
```
sudo chmod 777 /var/run/docker.sock
```

Add the Ubuntu user to the Docker group by running the following command:

```
sudo usermod -aG docker ubuntu
```
This will grant the Ubuntu user permission to run Docker commands without using sudo.

# More info manik-python-flask-calculator


To create a virtual environment for your Flask application, follow these steps:

## Install virtualenv if you haven't already:

```
sudo apt-get install python3-virtualenv

```
Navigate to the project directory (the folder containing app.py).
## Create a new virtual environment:


```
python3 -m venv venv
```
Activate the virtual environment:

```
source venv/bin/activate
```
Install the required packages:

```
pip install Flask
```
Run the Flask application:

```
python app.py
```

Now your Flask application is running in a virtual environment on your Ubuntu machine.

To deactivate the virtual environment, simply run:


```
deactivate
```


# Docker 

To create a Dockerfile for your Flask application, follow these steps:

First, create a new file named Dockerfile in the root directory of your Flask application (same directory as your app.py file).

* Open the Dockerfile in a text editor and add the following content:

Dockerfile
```
# Use the official Python image as the base image
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files into the container
COPY . .

# Expose the port the app runs on
EXPOSE 5000

# Start the application
CMD ["python", "app.py"]

```

Create a requirements.txt file in the root directory of your Flask application, and add the following content:
```
Flask==2.1.1

```
* Make sure to replace the version number with the version of Flask you are using in your application.

Now, navigate to the root directory of your Flask application in the terminal or command prompt, and build the Docker image using the following command:

```
docker build -t your-image-name .

docker build -t manik-flask-calculator .

```

* Replace your-image-name with a name of your choice for the Docker image.

* Once the Docker image is built, you can run the application in a Docker container using the following command:

```

docker run -d -p 5000:5000 --name your-container-name your-image-name

```

* Replace your-container-name with a name of your choice for the Docker container, and your-image-name with the name you used in the previous step.

* Your Flask application should now be running in a Docker container, and you can access it at http://localhost:5000.

Note: If you're using Docker Toolbox on Windows, you'll need to use the IP address of the Docker Toolbox VM instead of localhost. You can find this IP address by running docker-machine ip in the Docker Toolbox terminal.


# Docker on Public IP 


If you want to access your Flask application using a public IP instead of localhost, you need to make a small change to your app.py file and update the Docker run command.

Update your app.py file:

Change the line:

```
app.run(host='0.0.0.0', port=5000)

```
to:

```
app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

```

Also, add the following import statement at the beginning of the app.py file:

```

import os

```
* This change will allow you to set the port number from an environment variable when running the Docker container.

* Build the Docker image as described in the previous response.

* Run the Docker container with the following command:


```

docker run -d -p :5000:5000 --name your-container-name your-image-name

```

* Replace your-public-ip with your public IP address, your-container-name with a name of your choice for the Docker container, and your-image-name with the name you used when building the Docker image.

* Now, your Flask application should be running in a Docker container, and you can access it using your public IP address and the specified port (e.g., http://your-public-ip:5000).

# Jenkins Freestyle Job for Docker Build and Deployment for Manik-Flask-Calculator

This readme provides a step-by-step guide for setting up a Jenkins Freestyle job for Docker build and deployment for the Manik-Flask-Calculator project.

## Prerequisites

Ensure that you have the following installed on your system:
- Jenkins
- Docker

## Job Configuration

1. Open Jenkins and navigate to the dashboard.

2. Click on "New Item" to create a new job and enter a name for the job.

3. Select "Freestyle project" and click "OK".

4. In the "Source Code Management" section, select "Git" and enter the URL of the GitHub repository for the Manik-Flask-Calculator project: https://github.com/manikcloud/manik-python-flask-calculator.git

5. Set the branch to "main" in the "Branches to build" field.

6. In the "Build" section, click "Add build step" and select "Execute shell".

7. In the "Command" field, enter the following command to log in to Docker Hub:

```
docker login -u <your_dockerhub_username> -p <your_dockerhub_password>
```

- Replace `<your_dockerhub_username>` and `<your_dockerhub_password>` with your actual Docker Hub credentials.

8. Add another "Execute shell" build step to build and deploy the Docker container:

```
sudo docker build -t manik-flask-calculator:$BUILD_ID .
sudo docker rm flask-calculator -f
sudo docker run -d -p 5000:5000 --name flask-calculator manik-flask-calculator:$BUILD_ID

```
# Smoke test

```sleep 10
curl http://localhost:5000/health
```
This command will build the Docker container, remove any existing container with the same name, run the new container, and perform a smoke test by checking the `/health` endpoint.

9. Click "Save" to save the job configuration.

10. Run the Jenkins job to trigger a build and deploy the Docker container.

11. Verify that the Docker container is deployed and working correctly by checking the logs or accessing the application.

This setup creates a simple CI/CD pipeline for the Manik-Flask-Calculator project that automates the build, testing, and deployment process using Jenkins and Docker Hub. Whenever new code is pushed to the GitHub repository, Jenkins automatically triggers a build and test cycle, and if everything passes, it builds and deploys a Docker container. The smoke test helps to ensure that the container is running correctly and the application is working as expected.
