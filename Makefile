.PHONY: help
help:
	@echo "You need to set environment variables using the command:"
	@echo "	 cd dev && source set_env.sh"
	@echo ""
	@echo "Available commands:"
	@echo "	 make kafka  -  run kafka in docker"
	@echo "	 make simple  -  basic example of faststream start"
	@echo "	 make multi  -  faststream app with many sub and pub handlers"
	@echo "	 make fastapi  -  example of integration with fastapi"
	@echo "	 make app  -  custom app example"
	@echo "	 make data  -  data generation for custom app"
	@echo ""
	@echo "  make main  -  You can run custom app in two docker containers and check data processing in kafka-ui"


.PHONY: kafka
kafka:
	docker-compose -f ./dev/docker/docker-compose-kafka.yml up -d


.PHONY: main
main:
	docker-compose -f ./dev/docker/docker-compose-main.yml up -d


.PHONY: simple
simple:
	python src/fast_stream/simple/run.py


.PHONY: fastapi
fastapi:
	python src/fast_stream/fastapi_integration/run.py


.PHONY: multi
multi:
	python src/fast_stream/multi/run.py


.PHONY: app
app:
	python src/fast_stream/custom/run.py


.PHONY: data
data:
	python src/data/generate.py
