# penHouse
Penhouse is a comprehensive blogging platform that revolutionizes the way people engage with written content. With Penhouse, users can seamlessly read and post blogs while enjoying a range of powerful features. These include the ability to follow other users, express appreciation through post likes, track views for valuable analytics insights, bookmark articles as favorites, and actively participate in the community through comments and ratings for both authors and articles.

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
- React & Redux-toolkit
## Setup
# Prerequisites
Before you can run the project, you need to have the following installed on your machine:

- Docker
- Docker Compose

## Installation
Clone the repository and cd into the project directory:

### Copy code
```git clone https://github.com/VinneyJ/penHouse.git```
cd penHouse
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




