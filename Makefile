DOCKER_USERNAME = ansilema

IMAGE_NAME = python-oc-lettings-fr

LATEST_TAG = $(shell git rev-parse --short=8 HEAD)

run-latest:
	docker pull $(DOCKER_USERNAME)/$(IMAGE_NAME):$(LATEST_TAG)
	docker run --rm --platform linux/amd64 -p 8001:8000 \ --env-file .env \
		$(DOCKER_USERNAME)/$(IMAGE_NAME):$(LATEST_TAG)
