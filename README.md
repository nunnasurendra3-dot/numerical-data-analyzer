Numerical Data Analyzer

A Python-based numerical data analysis application designed to process CSV datasets, perform statistical and correlation analysis, and generate meaningful visual insights from numerical data.

The project is containerized with Docker to provide a consistent and reproducible development and execution environment.

📌 Overview

Numerical Data Analyzer is a data analysis project that simplifies the process of exploring numerical datasets.

The application can work with CSV data, analyze relationships between numerical variables, and generate visual reports such as correlation heatmaps.

The project follows a modular structure so that data processing, analysis logic, visualization, and application/backend components can be maintained independently.

✨ Features

📊 Numerical dataset analysis

📁 CSV dataset support

🔢 Statistical analysis of numerical data

🔗 Correlation analysis between variables

🌡️ Correlation heatmap generation

📈 Data visualization

🐍 Python-based implementation

🐳 Docker containerization

🧩 Modular project structure

📄 Sample dataset included for testing

🛠️ Tech Stack
Technology	Purpose
Python	Core programming language
FastAPI	Backend/API framework
NumPy	Numerical computation
Pandas	Data processing
Matplotlib	Data visualization
Seaborn	Statistical visualization
Uvicorn	Application server
Docker	Containerization
CSV	Dataset format
📂 Project Structure
numerical-data-analyzer/
│
├── data/
│   └── sample.csv
│
├── reports/
│   └── correlation_heatmap.png
│
├── src/
│   ├── analyzer.py
│   ├── app.py
│   ├── correlation.py
│   ├── Dockerfile
│   ├── requirements.txt
│   │
│   └── backend/
│       └── main.py
│
├── .gitignore
└── README.md

Directory Description

data/

Contains input datasets used by the application.

reports/

Contains generated analysis reports and visualizations.

src/analyzer.py

Contains the core data-analysis functionality.

src/correlation.py

Handles correlation-related analysis and visualization.

src/app.py

Application-level functionality and execution logic.

src/backend/main.py

Contains the backend application/API implementation.

src/Dockerfile

Defines the Docker image and runtime environment.

src/requirements.txt

Contains the Python dependencies required by the application.

🚀 Getting Started
Prerequisites

Make sure the following are installed on your system:

Python 3.10+

Git

Docker

Verify your installations:

python --version
git --version
docker --version

💻 Local Installation
1. Clone the repository
git clone https://github.com/nunnasurendra3-dot/numerical-data-analyzer.git


Navigate into the project:

cd numerical-data-analyzer

2. Create a virtual environment
Windows
python -m venv venv


Activate it:

venv\Scripts\activate

Linux / macOS
python3 -m venv venv
source venv/bin/activate

3. Install dependencies
pip install -r src/requirements.txt

🐳 Running with Docker

Docker is provided to make the application environment consistent across different machines.

Navigate to the source directory:

cd src


Build the Docker image:

docker build -t numerical-data-analyzer .


Run the container:

docker run -p 8000:8000 numerical-data-analyzer


The application can then be accessed through the configured application port.

The exact host/port and startup command should match the configuration in src/Dockerfile.

📊 Data Analysis

The project accepts numerical data in CSV format.

A sample dataset is provided at:

data/sample.csv


The analysis workflow generally consists of:

CSV Dataset
     │
     ▼
Data Loading
     │
     ▼
Data Validation
     │
     ▼
Numerical Analysis
     │
     ▼
Correlation Analysis
     │
     ▼
Visualization
     │
     ▼
Generated Report

🔗 Correlation Analysis

The project includes functionality for analyzing relationships between numerical variables.

Correlation analysis helps identify the strength and direction of linear relationships between variables.

The generated visualization is available in:

reports/correlation_heatmap.png


Example:

Correlation Matrix
        A      B      C
A      1.00   0.82   0.21
B      0.82   1.00   0.35
C      0.21   0.35   1.00


Correlation describes statistical association and should not automatically be interpreted as causation.

📈 Output

The project generates visual analytical output such as correlation heatmaps.

Generated reports are stored in:

reports/


This makes the analysis results easier to inspect and share.

🔌 Backend

The project includes a backend component implemented using FastAPI.

The backend is located at:

src/backend/main.py


For API-specific usage, refer to the application's configured routes and startup configuration.

When running a FastAPI application locally, interactive API documentation is commonly available through:

/docs


and:

/redoc


These endpoints are available when the FastAPI application is configured and running with the corresponding documentation enabled.

🧪 Testing

Before committing changes, verify that:

The application starts successfully.

The sample CSV can be processed.

Numerical analysis completes without errors.

Correlation analysis produces the expected output.

The Docker image builds successfully.

The Docker container starts successfully.

Example Docker verification:

docker build -t numerical-data-analyzer .
docker run -p 8000:8000 numerical-data-analyzer

## ☸️ Kubernetes Deployment

Kubernetes is used to deploy, manage, and run containerized applications. It helps automate container deployment, scaling, and recovery.

### Prerequisites

Make sure the following tools are installed and configured:

- Docker Desktop
- Kubernetes enabled and running
- `kubectl` command-line tool
- Docker image for the application

Verify the installations:

```powershell
docker --version
kubectl version --client
kubectl cluster-info
```

### 1. Start the Kubernetes Cluster

Start Docker Desktop and ensure your Kubernetes cluster is running.

Verify the cluster connection:

```powershell
kubectl cluster-info
kubectl get nodes
```

### 2. Build the Docker Image

From the project directory, build the application image using the Dockerfile location configured for your project.

```powershell
docker build -t numerical-data-analyzer:latest -f src/Dockerfile .
```

If your Kubernetes deployment uses a locally built image, configure the deployment to use the same image name and an appropriate image-pull policy.

### 3. Deploy the Application

Store your Kubernetes configuration files in a directory named `k8s/`.

For example:

```text
k8s/
├── deployment.yaml
└── service.yaml
```

Apply the configuration files:

```powershell
kubectl apply -f k8s/
```

Check the deployed resources:

```powershell
kubectl get deployments
kubectl get pods
kubectl get services
```

### 4. Access the Application

Use port forwarding to access the application from your local machine.

For a deployment exposing container port `8000`:

```powershell
kubectl port-forward deployment/numerical-data-analyzer 8000:8000
```

For a Streamlit dashboard exposing container port `8501`:

```powershell
kubectl port-forward deployment/student-analytics 8501:8501
```

Use only the command that matches your actual Kubernetes deployment name and container port. Keep the terminal running while accessing the application.

Open the corresponding URL in your browser:

- FastAPI: `http://localhost:8000`
- FastAPI interactive documentation: `http://localhost:8000/docs`
- Streamlit dashboard: `http://localhost:8501`

These URLs work only when the matching application is deployed and listening on the specified port.

### 5. Monitor the Deployment

Check the status of the pods:

```powershell
kubectl get pods
```

Inspect a deployment:

```powershell
kubectl describe deployment numerical-data-analyzer
```

View application logs:

```powershell
kubectl logs deployment/numerical-data-analyzer
```

Replace `numerical-data-analyzer` with the actual deployment name when necessary.

### 6. Update or Remove the Deployment

After updating the application image or Kubernetes manifests, apply the configuration again:

```powershell
kubectl apply -f k8s/
```

To remove the deployed resources created from these manifests:

```powershell
kubectl delete -f k8s/
```

**Note:** Kubernetes resources must be defined in valid manifest files before they can be deployed. The filenames, deployment names, image settings, and ports in this section must match the actual project configuration.


🔐 Configuration & Security

Do not commit sensitive information such as:

API keys

Passwords

Access tokens

Database credentials

.env files containing secrets

Sensitive configuration should be stored using environment variables or an appropriate secret-management solution.

The repository's .gitignore is configured to prevent common environment and Python-generated files from being committed.

📦 Dependencies

Project dependencies are maintained in:

src/requirements.txt


Install them using:

pip install -r src/requirements.txt

🐳 Docker Benefits

Containerizing the application provides several benefits:

Consistent runtime environment

Simplified deployment

Dependency isolation

Easier application setup

Reproducible builds

Better portability between development and production environments

🔮 Future Improvements

Potential improvements include:

 Add comprehensive automated tests

 Add data validation and schema checks

 Add additional statistical analysis

 Add more visualization types

 Improve API documentation

 Add CI/CD with GitHub Actions

 Add production-ready logging

 Add structured error handling

 Add API authentication where required

 Deploy the application to a cloud platform

 Add monitoring and health-check endpoints

🤝 Contributing

Contributions are welcome.

To contribute:

git clone https://github.com/nunnasurendra3-dot/numerical-data-analyzer.git
cd numerical-data-analyzer


Create a new branch:

git checkout -b feature/your-feature


Make your changes and commit:

git add .
git commit -m "Add your feature"


Push the branch:

git push origin feature/your-feature


Then open a Pull Request on GitHub.

📄 License

This project currently does not specify a license.

If this project is intended for public use or distribution, consider adding an appropriate open-source license.

👨‍💻 Author

Surendra

GitHub:
https://github.com/nunnasurendra3-dot

⭐ Project

If you find this project useful, consider giving the repository a star on GitHub.

Repository:
https://github.com/nunnasurendra3-dot/numerical-data-analyzer