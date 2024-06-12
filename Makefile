.PHONY: help
help: ## Show this help
	@printf "\033[33m%s:\033[0m\n" 'Available commands'
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z0-9_-]+:.*?## / {printf "  \033[32m%-19s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.PHONY: start
start: ## Start all docker containers
	docker-compose up

.PHONY: stop
stop: ## Stop all docker containers
	docker-compose stop

.PHONY: restart
restart: stop start ## Restart containers

.PHONY: delete-all
delete-all: ## Delete all docker containers
	docker rm $(docker ps -a -q)