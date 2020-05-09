# Simba

Simba is an e-commerce shipment management tool. This is built as example project to showcase Django ecosystem. Primary skills required for complete development of this tool are:

1. Knowledge about following tools
   1. Django + MySQL
   2. Django Rest Framework + Django Rest Auth
   3. Celery + RabbitMQ
2. System design
   1. Knowledge about how to design REST APIs
   2. Knowledge about how to write a crawler

This project is designed in such a way that it can scale easily and doesn't block resources by running on single thread.

## Running locally

1. Ensure that you have installed all the dependencies by running the following commands:

   ```bash
   pip install -r requirements.txt
   pip install -r requirements_dev.txt
   ```

   `requirements_dev.txt` has the dependencies which are required for local development of project and not while deploying the project

2. Start a MySQL instance. This can be done by running the [official Docker image of MySQL](https://hub.docker.com/_/mysql).

   ```bash
   mkdir -p ~/dummy/mysql_8
   docker pull mysql:8.0.20
   docker run --name some-mysql -v ~/dummy/mysql_8:/var/lib/mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=my-secret-pw -d mysql:8.0.20
   ```

3. Update the MySQL connection details by creating a file at `configs/sqldb.cnf` with following content

   ```yaml
    [client]
    HOST = 127.0.0.1
    database = simba
    user = root
    password = my-secret-pw
    default-character-set = utf8
   ```

4. Run following command to start the server. This will start the server in a continuously running process

   ```bash
   python manage.py migrate --settings=settings.base
   python manage.py runserver --settings=settings.base
   ```

   We are using custom settings override by specifying a new file using `--settings` argument.

5. To start the Celery workers, start a RabbitMQ instance using [official image at Docker](https://hub.docker.com/_/rabbitmq) by running the following command

   ```bash
   docker pull rabbitmq:3
   docker run -d -p 5672:5672 --hostname my-rabbit --name rabbit-mq rabbitmq:3
   ```

6. Start the worker by running the following command

   ```bash
   celery worker -A simba -l info
   ```

   This will start the instance and set the log level at `INFO`.

7. Use the following [API Documentation, written with Postman](https://documenter.getpostman.com/view/5352730/SzmZe21E?version=latest). This will detail you about the API endpoints available. You need to replace `baseURL` in collection variable to `http://localhost:8000`.

## Deployment

1. This project is deployed with the help of `Heroku` at [https://simba-kv.herokuapp.com/](https://simba-kv.herokuapp.com/).

2. We are using Postgres instead of MySQL provided by [Heroku-Postgres](https://www.heroku.com/postgres) and RabbitMQ provided by [CloudAMQP](https://www.cloudamqp.com/).

3. Follow the guidelines mentioned [at heroku documentation](https://devcenter.heroku.com/articles/celery-heroku) to deploy a Django + Celery app on Heroku. `Procfile` at the root of folder is used to denote all the processed to be run.

4. Update the following config vars, which are passed to your processes as environment variables

   ```bash
   SECRET_KEY='<Django secret key to handle CSRF>'
   BROKER_URL='Rabbit MQ connection string'
   DATABASE_URL='Postgres connection string'
   ALLOWED_HOSTS='Host of your Heroku deployment'
   DJANGO_SETTINGS_MODULE='settings.production'
   DISABLE_COLLECTSTATIC=1
   ```

   `DATABASE_URL` will be added automatically if you use `Heroku-Postgres`

5. Deploy your app and use the following [API Documentation, written with Postman](https://documenter.getpostman.com/view/5352730/SzmZe21E?version=latest). This will detail you about the API endpoints available. You need to replace `baseURL` in collection variable to URL of your app.

## What is implemented

1. Application API should be developed using Django rest framework. With following APIs.
   1. CRUD APIs for adding seller shop credential
   2. API to list the shipments which are saved in the database.
   3. API to start the initial sync for the shop which will sync all shipments of the shop.
2. Application should be able to handle the rate limiting in such a way so that we are not making any extra API calls.
3. Application code should be clean, properly commented and should use the OOPs concepts.
4. Application should handle all corner cases.
5. Application should be scalable and should handle the large number of shipments in such manner where the thread is not blocked. For eg: if there are 1000 shipments and you sync all in a single thread of python, then it is a wastage of whole resources and thread will be blocked until the process is completed or exited.

## What is remaining

1. Better Rate limiting
2. Refreshing after token expiration in single crawling job
3. Automatic trigger of new shipment sync
4. Unit test cases in project
5. E2E test cases in Postman
