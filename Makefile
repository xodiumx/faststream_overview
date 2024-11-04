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
