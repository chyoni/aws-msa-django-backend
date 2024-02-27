#!/bin/bash

docker stop django-order-service-backend

docker compose -f ./docker-compose.yml down

docker compose -f ./docker-compose.yml -p msa-order-service up --build -d