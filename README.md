# penHouse
This is a clone of the Medium like backend API built using Django and Django Rest Framework (DRF). It is a fully-featured API that allows users to register, login, create articles, rate articles, upvote or downvote articles, add articles to their favourites, comment on articles and search the API. The API also tracks the number of views on each article.

## Technologies Used
- Django
- Django Rest Framework (DRF)
- Celery
- Flower
- Docker
- Redis
- Nginx
- Proxy Managers
- RabbitMQ
- Haystack & Whoosh
- Portainer
## Setup
# Prerequisites
Before you can run the project, you need to have the following installed on your machine:

- Docker
- Docker Compose

## Installation
Clone the repository and cd into the project directory:

### Copy code
```git clone https://github.com/VinneyJ/medium-api-clone.git```
cd medium-backend-api-clone
Create a .env file in the root directory and add the following environment variables:

```
replace the data in .envs/.local with your environment variables
```

Also, replace your-secret-key with a random string that you choose as your secret key.

## Build and run the Docker containers:

Run the command below to build the containers:
```
make build
```
To shutdown the containers run:
```
make down
```

To spin them up again:
```
make up
```
You can check the logs if all the containers are running well with this command:

```
make logs
```

Run migrations:
```
make makemigrations

make migrate
```

Create Superuser:
```
make superuser
```
- You can however explore the make files for the available commands.





Usage
The API can be accessed at http://localhost:80/.

To access the admin panel, go to http://localhost:80/secrets/ and login with your superuser account.

API Endpoints
All the API Endpoint are available in a Redoc documentaion. Once you have the project running navigate to http://localhost:80/redoc/ to find all the Endpoints.

Incase you might have any questions don't hesitate to reach out.




