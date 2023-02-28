# ElasticSearch Test App

## Technologies
- ElasticSearch
- Kibana
- VueJS
- FastAPI
## Installation

1. Clone this repo and after you ran Docker

```sh
 git clone https://github.com/Kushnar/elastic_pr.git
```

2. Build container from existed docker-compose.yml file (you should run command from the same directory with
   docker-compose.yml )

```sh
 docker-compose build
```

3. Up the container (you should run command from the same directory with
   docker-compose.yml )

```sh
 docker-compose up
```

4. Your SPA ready to use at [http://localhost:8080/](http://localhost:8080/) on your device.
Elasticsearch container will have to start after 5-10 seconds, so data couldn't be showed immediately.
Searching include first name, second name, last name and email adress fields
## Using
- front - [http://localhost:8080/](http://localhost:8080/)
- back - [http://localhost:8000/](http://localhost:8000/)
- kibana - [http://localhost:5601/](http://localhost:5601/)
- elasticsearch - [http://localhost:9200/](http://localhost:9200/)