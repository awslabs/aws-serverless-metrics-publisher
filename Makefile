SHELL := /bin/sh
PY_VERSION := 3.6

export PYTHONUNBUFFERED := 1

BUILD_DIR := dist

# user must set PACKAGE_BUCKET env variable with valid bucket name
PACKAGE_BUCKET ?= <bucket>

# user can optionally override these with env vars
STACK_NAME ?= metricpublisher-stack
AWS_DEFAULT_REGION ?= us-east-1

PYTHON := $(shell /usr/bin/which python$(PY_VERSION))

.DEFAULT_GOAL := build

clean:
	rm -rf $(BUILD_DIR)

init:
	$(PYTHON) -m pip install pipenv --user

dev-deps: init
	pipenv sync --dev

compile: dev-deps
	pipenv run pydocstyle metricpublisher
	pipenv run flake8 metricpublisher

test: compile
	python -m pytest test/ -v
build: test

package: build
	mkdir -p $(BUILD_DIR)
	cp -r template.yaml metricpublisher $(BUILD_DIR)

	# package dependencies in lib dir
	pipenv lock --requirements > $(BUILD_DIR)/requirements.txt
	pipenv run pip install -t $(BUILD_DIR)/app/lib -r $(BUILD_DIR)/requirements.txt

	sam package --template-file $(BUILD_DIR)/template.yaml --s3-bucket $(PACKAGE_BUCKET) --output-template-file $(BUILD_DIR)/packaged-template.yaml

deploy:
	sam deploy --template-file $(BUILD_DIR)/packaged-template.yaml --stack-name $(STACK_NAME) --capabilities CAPABILITY_IAM
