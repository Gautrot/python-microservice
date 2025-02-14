.PHONY: init run test build clean

init:
	@echo "Installing dependencies..."
	pip install --upgrade pip
	pip install -r requirements.txt

run:
	@echo "Running the Flask app..."
	export $(cat .env | xargs) && python app.py

test:
	@echo "Running tests..."
	export $(cat .env | xargs) && pytest tests/test_health_calculator.py

build:
	@echo "Building the Docker image..."
	docker build -t health-calculator-service .

clean:
	@echo "Cleaning up..."
	docker rmi health-calculator-service
