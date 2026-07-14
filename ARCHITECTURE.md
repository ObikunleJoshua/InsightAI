# InsightAI Architecture

## Overview

InsightAI is an AI-powered Data Intelligence Platform that automatically understands, analyzes, visualizes, and explains structured datasets.

Unlike traditional business intelligence tools that are designed for a specific industry, InsightAI is built to work with **any structured dataset**.

The platform follows a modular architecture where each service has a single responsibility.

---

# Core Philosophy

InsightAI follows one simple principle:

> **Python computes. AI explains.**

Python is responsible for:

- Data loading
- Dataset profiling
- Statistical analysis
- Insight generation
- Data quality assessment

AI is responsible for:

- Executive summaries
- Business explanations
- Recommendations
- Report writing

The AI never performs calculations.

---

# Design Goals

The platform is designed to be:

- Domain agnostic
- Modular
- Extensible
- Explainable
- Performant
- Maintainable
- Production-ready

---

# High-Level Architecture

```
                User Upload
                     │
                     ▼
              Data Service
                     │
                     ▼
      Dataset Intelligence Service
                     │
     ┌───────────────┼───────────────┐
     ▼               ▼               ▼
 Analytics      Visualization     Insights
                     │
                     ▼
                AI Manager
                     │
                     ▼
              Export Manager
```

---

# Responsibilities

## Data Service

Responsible for:

- Loading datasets
- File validation
- DataFrame creation

Supported formats:

- CSV
- Excel

Future:

- SQLite
- PostgreSQL
- MySQL

---

## Dataset Intelligence Service

Creates a complete description of the dataset.

Examples:

- Dataset shape
- Column information
- Data types
- Missing values
- Quality score
- Relationships
- Dataset capabilities

This service becomes the central source of truth for the platform.

---

## Analytics Service

Responsible for statistical analysis.

Examples:

- Correlation analysis
- Outlier detection
- Distribution analysis

---

## AI Manager

Provides a unified interface for AI providers.

Current provider:

- Ollama

Future providers:

- OpenAI
- Azure OpenAI

---

## Export Manager

Exports AI reports to:

- Markdown
- DOCX
- PDF

---

# Metadata-First Design

Every uploaded dataset is transformed into structured metadata.

Example:

```
Dataset

↓

Metadata

↓

Analytics

↓

Insights

↓

AI Report
```

This prevents every service from repeatedly inspecting the dataset.

---

# Folder Structure

```
services/
│
├── ai/
├── export/
│
├── analytics_service.py
├── data_service.py
├── dataset_classifier.py
├── review_service.py
```

The project continues evolving toward a metadata-first architecture.

---

# Why This Architecture?

The architecture is designed around **capabilities**, not industries.

InsightAI does not assume a dataset contains:

- Sales
- Profit
- Revenue
- Ratings

Instead, it discovers:

- Numeric columns
- Categorical columns
- Date columns
- Text columns
- Relationships
- Data quality

This allows the platform to analyze datasets from many domains including business, healthcare, education, manufacturing, finance, human resources, research, and more.

---

# Version

Current Version:

**InsightAI v1.0 (In Development)**
