# Urban Mobility Intelligence Platform 🚇

[![CI](https://img.shields.io/github/actions/workflow/status/DhrumilPanchal10/urban-mobility-intelligence/ci.yml?branch=main)](https://github.com/DhrumilPanchal10/urban-mobility-intelligence/actions)
[![dbt docs](https://img.shields.io/badge/dbt-docs-published-blue)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## Overview

Urban Mobility Intelligence Platform ingests GTFS (NYC MTA), loads raw data into PostgreSQL, applies dbt transformations and tests, and surfaces analytics through a dashboard. It is organized for local development (Docker) and for deployment.

---

## Quick Links
- Repo: `https://github.com/DhrumilPanchal10/urban-mobility-intelligence`  
- Key folders: `airflow/dags`, `dbt`, `infrastructure/docker`, `scripts`, `run_pipeline.sh`

---

## Architecture

```mermaid
flowchart LR
    GTFS[NYC MTA GTFS] --> Ingest[Python Ingestor]
    Ingest --> Postgres[(PostgreSQL - staging)]
    Postgres --> dbt[dbt Transformations]
    dbt --> Analytics[(Analytics schema)]
    Analytics --> Dashboard[Streamlit / Dashboard]
    Airflow[Airflow Scheduler] --> Ingest
