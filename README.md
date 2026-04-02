# acest-gym-app
 Gym Management App (DevOps Project)

Project Overview

This is a simple Flask-based Gym Management Application developed as part of a DevOps assignment.

The application provides basic REST APIs to:

* View available gym plans
* View gym members
* Display a welcome homepage

This project demonstrates:

* Python web development using Flask
* Automated testing using Pytest
* Containerization using Docker
* Continuous Integration using GitHub Actions
* Build automation using Jenkins

---

Local Setup and Execution Instructions

Step 1: Clone the Repository
git clone https://github.com/2024tm93724-Srishti/acest-gym-app.git

cd acest-gym-app


Step 2: Install Dependencies

pip install -r requirements.txt

Step 3: Run the Application

python app.py

Step 4: Open in Browser

http://localhost:5000/
http://localhost:5000/plans
http://localhost:5000/members

Running Tests Manually

Step 1: Install pytest (if not installed)

python -m pip install flask pytest

Step 2: Run Tests

pytest

Expected Output

3 passed in 15 seconds

Docker Instructions

Step 1: Build Docker Image

docker build -t acest-gym-app .

Step 2: Run Docker Container

docker run -p 5000:5000 acest-gym-app

Access Application

http://localhost:5000

CI/CD Pipeline Overview

GitHub Actions (Continuous Integration)

GitHub Actions is used to automate:

* Installing dependencies
* Running tests
* Building Docker image

Workflow file location:

.github/workflows/main.yml

Workflow Steps:

1. Checkout code from repository
2. Set up Python environment
3. Install dependencies from `requirements.txt`
4. Run tests using pytest
5. Build Docker image

Jenkins Integration (Build Automation)

Jenkins is used to:

* Pull code from GitHub repository
* Build the Docker image
* (Optional) Run tests

Steps in Jenkins:

1. Create Freestyle Project
2. Configure Git repository
3. Add Build Step:

docker build -t acest-gym-app .

Project Structure

acest-gym-app/
│
├── app.py
├── test_app.py
├── requirements.txt
├── Dockerfile
├── README.md
└── .github/
    └── workflows/


Srishti Sinha

