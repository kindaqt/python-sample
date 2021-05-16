SQLALCHEMY_DATABASE_URI=sqlite:////tmp/appointment.db
FLASK_APP=app.py
NAME=maven-sample
DOCKER_HUB_REPO=williamheiderman
DOCKER_HUB_LINK=${DOCKER_HUB_REPO}/${NAME}

.PHONY: build publish

build:
	docker build -t ${NAME} .

run:
	docker run --publish 5000:5000 ${NAME}

publish:
	docker tag maven-sample ${DOCKER_HUB_LINK}
	docker push ${DOCKER_HUB_LINK}

pull:
	docker pull ${DOCKER_HUB_LINK}:latest

dev:
	SQLALCHEMY_DATABASE_URI=${SQLALCHEMY_DATABASE_URI} \
	FLASK_APP=${FLASK_APP} \
	FLASK_ENV=development \
	flask run --host=0.0.0.0