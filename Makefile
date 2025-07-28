# Project Settings
COMPOSE=docker-compose
COMPOSE_FILE=docker-compose.yml

# Default target
.PHONY: help
help:
	@echo "Usage:"
	@echo "  make build         - Build all services"
	@echo "  make up            - Start all services"
	@echo "  make down          - Stop all services"
	@echo "  make restart       - Restart all services"
	@echo "  make logs          - Show logs for all services"
	@echo "  make clean         - Remove containers and volumes"
	@echo "  make test-mlflow   - Run a test MLflow script"

# Build all services
.PHONY: build
build:
	$(COMPOSE) -f $(COMPOSE_FILE) build

# Start containers
.PHONY: up
up:
	$(COMPOSE) -f $(COMPOSE_FILE) up -d

# Stop containers
.PHONY: down
down:
	$(COMPOSE) -f $(COMPOSE_FILE) down

# Restart containers
.PHONY: restart
restart: down up

# Show logs
.PHONY: logs
logs:
	$(COMPOSE) -f $(COMPOSE_FILE) logs -f

# Remove containers and volumes
.PHONY: clean
clean:
	$(COMPOSE) -f $(COMPOSE_FILE) down -v

# Run a quick MLflow test script (optional)
.PHONY: test-mlflow
test-mlflow:
	docker exec -it mlflow python test_mlflow.py

.PHONY: evidently
evidently:
	docker-compose build evidently
	docker-compose up -d evidently
	docker-compose logs -f evidently

reset:
	docker-compose down -v
	docker volume prune -f
	docker-compose build
	docker-compose up -d

soft-reset:
	docker exec airflow airflow dags delete predict_sp500_dag --yes || true
	docker exec airflow airflow dags delete train_and_promote_sp500_dag --yes || true
	docker exec airflow airflow dags delete sp500_data_ingestion_dag --yes || true

bash:
	docker compose exec airflow bash