# Sentiment Analyzer for **ucreate** 

Since, one of the requirements there in assignment was to be easy to install, I decided to create it using "Docker".
So, we have **100% Dockerized**, **swagger** friendly  **Flask** app with different kind of **tests**.
Let's start the review


## Dependencies
To run this application, You need only  GNU **make** utility, **Docker/Docker Compose** and few commands to run:


## Getting Started

**1.** First, clone the project:

```bash
$ git clone https://github.com/ent1c3d/sentiment_analyzer.git <my-project-name>
$ cd <my-project-name>
```

**2.** Then install dependencies and check that it works

```bash
$ make install      # Install the pip dependencies on the docker container
$ make start        # Run the container containing your local python server
```
If everything works, you should see the available routes [here](http://127.0.0.1:3000/application/health).

You can also see list of running containers :
![enter image description here](https://user-images.githubusercontent.com/2203893/52539900-de587d00-2d9c-11e9-902c-60171653d963.png)

**3.** Run this command to create migration files based on our models :
```bash
$ make db/migrate
```
After this command, you can see into 'migrations/versions', that there was created our first migration file.

**4.** Let's generate tables from our migration file
```bash
$ make db/upgrade
```

Now you already can connect with your database with any client (for example with  Navicat)   
user: 'postgres'  
psw:'' (empty)   
port:5432
or with command :
```bash
$ make db/connect
```


**5.** For test/train data I am using nltk twitter corpus. I decided to save all of this data into my db, because I think  in the future I will add some functionality to this app(like - add new data using post requests) and it will be better, if all of this data will be already into my database, instead of json files.
So,  I created custom seeder and using it with flask-script extension to download nltk corpus and insert it into db.
Just run this command:
```bash
$ make db/seed  # it takes little time (approx 1-2 min)
```
You can check the database tables, there will already be thousands of classified posts from Twitter.
![enter image description here](https://user-images.githubusercontent.com/2203893/52540080-03e68600-2d9f-11e9-90ea-dbf888a960c3.png)



Now everything is ready, you can see the **[result](http://127.0.0.1:3000/application/sentiment_analysis/I%20am%20a%20happy%20man)** !
![enter image description here](https://user-images.githubusercontent.com/2203893/52540441-d8fe3100-2da2-11e9-921f-997e9534f219.png)


---

So, Application already includes classifier model, but you can add some more data into database/posts table and then regenerate classifier model with this command :

```bash
$ make gc  # generate classifier
```


## Testing

With one command you can run swagger, functional and unit tests  :
```bash
$ make tests
```
I have commented testing database into docker file  and using main database for tests too, because  this application doesn't inserts anything into db(only seeder inserts), we are using db only for reading and to save time, I am using only one db yet.


---
You can also run Run flake8 on the `src` and `test` directories.
```bash
$ make lint
```

## Commands  List


|`make <script>`|Description|
|------------------|-----------|
|`install`|Install the pip dependencies on the server's container.|
|`start`|Run your local server in its own docker container.|
|`db/connect`|Connect to your docker database.|
|`db/migrate`|Generate a database migration file using alembic, based on your model files.|
|`db/upgrade`|Run the migrations until your database is up to date.|
|`db/downgrade`|Downgrade your database by one migration.|
|`tests`|Run unit tests with unittest in its own container.|
|`lint`| Run flake8 on the `src` and `test` directories.|
