.PHONY: kafka
kafka:
	docker-compose -f ./dev/docker/docker-compose-kafka.yml up -d


.PHONY: simple
simple:
	python src/fast_stream/simple/run.py


.PHONY: fastapi
fastapi:
	python src/fast_stream/fastapi_integration/run.py
