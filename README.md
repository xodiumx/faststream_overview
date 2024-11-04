# faststream_overview

## Description

- A little extended example of working with faststream framework
- You can run kafka in docker and run the application with data processing and generation
- Also you can observe the data processing in kafka-ui

## Application installation

- Clone repository

- Set up a virtual environment and install dependicies:

```console
python -m venv venv
```

or

```console
pyenv virtualenv 3.12.3 kafka_example
```

```console
poetry install
```

- Available commands:

```console
make help
```

- Run kafka as a broker

```console
make kafka
```

> UI endpoint - http://localhost:8080/overview

- Setup environment variables:

```sh
cd dev && source set_env.sh
```

### Run example in docker

- To run the docker work example:

```console
make main
```

> OpenAPI endpoint - http://localhost:9000/docs
> Prometheus metrics endpoint - http://localhost:9000/metrics

- generated data is sent to the `consume` topic
- the data after processing is sent to the `pub` topic
