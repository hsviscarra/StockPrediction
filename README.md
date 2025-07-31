# 🧠 Stock Prediction & Fundamental Analysis Platform

A robust, scalable, and cloud-native pipeline for predicting stock prices and analyzing financial fundamentals using **free data sources like Yahoo Finance**. This project integrates the best MLOps and data engineering practices for research, deployment, and monitoring.

---

## 📌 1. Problem Description

Stock prediction is a long-standing challenge that combines quantitative modeling, macroeconomic insights, and technical analysis. This project aims to:

- Predict future stock prices using machine learning.
- Analyze companies based on fundamental indicators (e.g., P/E ratio, EPS, ROE).
- Enable long-term and short-term investment decision support.
- Deliver predictions via a production-grade pipeline.

The scope of the project is the following:
- Market: US Market
- Benchmark SP500 Index

The purpose is to make a prediction of the SP500 for the next 5 days using a comprehensive mlops project uses the following services:
- Apache airflow for orchestration
- MLFlow to track experiments and models
- Streamlit to expose the last prediction.
- Evidently to monitor the model and data
- FastAPI as the backend
- Terraform to automate the creation of App Service in Azure to host the production code
- Pytest to introduce tests in the CI/CD flow process

This project shows how to build a MLOPs infrastruvture for a specific task and it is easily extensible for more complex jobs. 


**Why this matters:**

- Helps retail and institutional investors make informed decisions.
- Offers a framework to test trading strategies with historical & live data.
- Demonstrates real-world MLOps for time-series forecasting.

---

## ☁️ 2. Cloud Architecture (Azure)

The project is cloud-ready and leverages AWS services such as:

- **AppService**: To host the production code and application

The entire project is containerized and deployable using **Docker**.

---

## 🛠️ 3. Infrastructure as Code (IaC)

All infrastructure is provisioned via **Terraform**, enabling reproducible environments.

---

## 🔬 4. Experiment Tracking & Model Registry

- **MLflow** is used for:
  - Tracking model experiments (params, metrics, artifacts)
  - Registering models with version control
  - Comparing and selecting the best-performing model

> UI accessible via localhost or deployed MLflow server in AWS

---

## 🛠️ 5. Workflow Orchestration

- **Apache Airflow** manages and schedules:
  - Daily data ingestion from Yahoo Finance
  - Feature engineering pipelines
  - Model training, evaluation, and deployment

---

## 🚀 6. Model Deployment

- Model is served using:
  - **FastAPI**  (RESTful API)
  - Dockerized container
  - Deployed via Docker
  - CI/CD pipeline ensures automatic deployments


---

## 🧭 7. Model Monitoring

- **Evidently AI** tracks:
  - Data drift
  - Prediction drift
  - Feature importance changes
- **Alerts** (to be implemented) via:
  - Slack/Email notifications
  - Airflow-triggered retraining workflows
  - Auto-switching to backup models (blue/green deployment)

---

## 🔁 8. Reproducibility

- Clear documentation and `Makefile` for setup and training
- `requirements.txt` and `environment.yml` specify exact dependency versions
- Sample `.env.example` file for secrets and configs
- Dockerfile ensures consistent environment across dev/staging/prod

---

## 🧪 9. Best Practices

| Area              | Tools / Techniques                                      |
|-------------------|----------------------------------------------------------|
| Unit Testing      | `pytest`                              |
| Integration Tests | End-to-end tests for data flow and predictions           |
| Code Formatting   | `black`, `isort`, `flake8`, `pylint`                     |
| Pre-commit Hooks  | Auto-formatting, linting, and secret scanning            |
| CI/CD             | GitHub Actions |
| Project Structure | Modular folder structure with clear separation of concerns |
| Makefile          | Reusable command recipes (e.g., `make train`, `make test`) |

---

## 🧾 Project Structure
.
├── .github/                    # DAGs and orchestration scripts
├── artifacts/                       # Raw and processed datasets
├── configs/                     # Dockerfiles and deployment configs
├── data/                     # MLflow tracking and registry setup
├── docs/                     # Saved models and training scripts
├── notebooks/                  # Exploratory analysis and prototyping
├── services/                  # All the services used for the project
├── src/                        # Source code (training, ETL, API)
├── terraform/                 # IaC scripts
├── tests/                      # Unit and integration tests
├── Makefile                    # Command recipes
├── Docker Compose              # Command recipes
├── poetry.lock
├── poetry.toml
├── environment.yml
└── README.md

---

## ⚙️ Quickstart

```bash
# Clone repository
git clone https://github.com/your-username/stock-mlops-platform.git
cd stock-mlops-platform

# Set up virtual environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Start services
make up

📬 Contributing

PRs are welcome. Please follow the code style, write tests, and explain your changes.

📄 License

This project is licensed under the MIT License.

📚 References
	•	Yahoo Finance API (yfinance)
	•	MLflow Docs
	•	Evidently AI
	•	Terraform AWS Provider


  