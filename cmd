docker build -t cph1c06/flask-env .
docker run -d -p 5000:5000 -e USER=hermanchan cph1c06/flask-env
