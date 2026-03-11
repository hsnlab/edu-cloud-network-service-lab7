#FROM bitnami/spark:3.5.0
FROM spark:3.5.0-python3
#WORKDIR /opt/bitnami/spark
WORKDIR /opt/spark

USER root
RUN mkdir -p /home/spark && chmod -R 777 /home/spark
RUN pip install py4j
USER spark

COPY ./src/spark_pgsql/spark_streaming.py ./spark_streaming.py
COPY ./src/constants.py ./src/constants.py

ENV POSTGRES_DOCKER_USER=host.docker.internal
ARG POSTGRES_PASSWORD
ENV POSTGRES_PASSWORD=$POSTGRES_PASSWORD

