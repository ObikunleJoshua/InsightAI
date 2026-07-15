<p align="center">
  <img src="assets/logo-trans3.png" alt="InsightAI" width="300">
</p>
<p align="center">
AI-powered Decision Intelligence Platform
</p>

<p align="center">
<i>From Data to Decisions.</i>
</p>

<p align="center">
<img src="https://img.shields.io/badge/Status-Under%20Development-orange?style=flat-square">
<img src="https://img.shields.io/badge/Python-3.12-blue?style=flat-square&logo=python">
<img src="https://img.shields.io/badge/Streamlit-Framework-red?style=flat-square&logo=streamlit">
<img src="https://img.shields.io/badge/Ollama-AI-purple?style=flat-square">
<img src="https://img.shields.io/badge/License-MIT-green?style=flat-square">
</p>

## Overview

InsightAI is an AI-powered Data Intelligence Platform that automatically understands, profiles, analyzes, visualizes and explains structured datasets.

Unlike traditional analytics tools designed for a single industry, InsightAI is domain-agnostic. It first understands the dataset through a Metadata Service before generating statistical insights, interactive visualizations, AI-generated reports and exportable documentation.

Whether the dataset comes from business operations, customer feedback, education, healthcare, finance, research or any other structured source, InsightAI adapts its analysis to the data itself rather than relying on predefined business assumptions.

It asks the question:
- **What does this dataset contain?**
- **What insights can be discovered?**
- **What actions should be considered?**

The vision is to provide organizations with a single intelligent workspace for exploring data, monitoring KPIs, generating reports, and making smarter business decisions.

---

## Key Features

### 📊 Business Intelligence

- Interactive dashboards
- KPI monitoring
- Trend analysis
- Business reporting

### 🤖 Artificial Intelligence

- AI-generated reports
- Executive summaries
- Natural language insights
- Business recommendations

### 📈 Analytics

- Exploratory Data Analysis (EDA)
- Data profiling
- Data cleaning
- Statistical summaries

### 📉 Visualization

- Interactive charts
- Dynamic filtering
- Comparative analysis
- Business metrics

### 🧠 Dataset Intelligence

- Automatic metadata extraction
- Dataset quality assessment
- Column profiling
- Capability detection
- Domain-agnostic dataset understanding
---

## System Architecture

                 User Upload
                      │
                      ▼
                DataService
                      │
                      ▼
              MetadataService
                      │
                      ▼
          Dataset Intelligence
                      │
      ┌─────────┬──────────┬──────────┐
      ▼         ▼          ▼          ▼
 Dataset   Analytics   ChartService  AI Manager
Classifier    │              │            │
              └──────┬───────┘            │
                     ▼                    ▼
                ExportManager       Streamlit UI

## Tech Stack

| Category | Technologies |
|-----------|--------------|
| Language | Python 3.12 |
| Framework | Streamlit |
| Data Processing | Pandas, NumPy |
| Visualization | Plotly |
| AI | Ollama |
| Export | Markdown, DOCX, PDF |
| Testing | Pytest |

---

## Project Structure

```text
InsightAI/

├── assets/
│   ├── banner.png
│   ├── logo.png
│   ├── dashboard.jpeg
│   ├── ai-analyst.jpeg
│   └── icon.png
│
├── components/
│
├── services/
│
├── data/
│
├── exports/
│
├── tests/
│
├── app.py
│
├── requirements.txt
│
└── README.md
```

---

## Roadmap

### Version 1
- [x] Metadata Service
- [x] Dataset Intelligence
- [x] Dataset Classification
- [x] AI Report Generation
- [x] Interactive Dashboards
- [x] Dataset Profiling
- [x] Analytics Workspace
- [x] Chart Service
- [x] Export (Markdown, DOCX, PDF)

### Version 2
- [ ] AI Report Generator (Activeness)
- [ ] Authentication
- [ ] SQL databases
- [ ] Forecasting
- [ ] ML
- [ ] RAG
- [ ] Chat Assistant
- [ ] Multi-provider AI

### Version 3

- [ ] Predictive Analytics
- [ ] Forecasting
- [ ] Recommendation Engine
- [ ] Chat Assistant

### Version 4

- [ ] Authentication
- [ ] Cloud Deployment
- [ ] REST API
- [ ] Multi-user Workspace

---

## Installation

Clone the repository.

```bash
git clone https://github.com/ObikunleJoshua/InsightAI.git
```

Navigate into the project.

```bash
cd InsightAI
```

Create a virtual environment.

```bash
python -m venv venv
```

Activate the environment.

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

Run the application.

```bash
streamlit run app.py
```

---

## Project Status

InsightAI v1.0 is feature-complete and currently undergoing final stabilization, documentation, testing and deployment preparation.

---

## Author

### Joshua OBIKUNLE

Business Intelligence Engineer • AI Adoption Specialist

Creator of **InsightAI**

📧 joshuaobikunle94@gmail.com

💼 https://www.linkedin.com/in/joshua-obikunle-1b8739111/

---

## License

This project is licensed under the **Apache-2.0 license**.

---

<br><br>
**InsightAI**
<br>
<i>From Data to Decisions.</i>
</p>
