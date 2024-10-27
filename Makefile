.PHONY: kafka
kafka:
	docker-compose -f ./dev/docker/docker-compose-kafka.yml up -d

.PHONY: simple
simple:
	python src/run.py
