# manik-python-flask-calculator


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
```Flask==2.1.1

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

