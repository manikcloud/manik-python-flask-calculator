# #!/bin/bash

# # Build the Docker image
# sudo docker build -t varunmanik/manik-flask-calculator:$BUILD_ID .

# # Remove any existing containers
# sudo docker rm flask-calculator -f

# # # Log in to Docker Hub
# # sudo docker login -u varunmanik -p $DOCKER_HUB_PASSWORD

# # # Push the Docker image to Docker Hub
# # sudo docker push varunmanik/manik-flask-calculator:$BUILD_ID

# # Run the Docker container
# sudo docker run -d -p 5000:5000 --name flask-calculator varunmanik/manik-flask-calculator:$BUILD_ID

# Smoke test
echo "# Smoke test"

sleep 10

curl http://localhost:5000/health 
# Smoke test
response=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:5000/)
if [ $response -eq 200 ]; then
  echo "Smoke test passed!"
else
  echo "Smoke test failed!"
  exit 1
fi
