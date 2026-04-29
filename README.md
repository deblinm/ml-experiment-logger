# ML Experiment Logger — MLOps & SRE Portfolio Project

A Python application to log, track and compare 
machine learning experiments — built as a 
learning project towards an MLOps Engineering career.

## What it does
- Log ML experiments with model name, parameters and metrics
- Compare two experiments side by side
- Find the best performing model by any metric
- Save and load experiments from JSON
- Full REST API using FastAPI and Pydantic

## Technologies Used
- Python 3.13
- FastAPI
- Pydantic
- Uvicorn
- JSON for persistence

## Project Structure
- experiment.py      — Experiment dataclass
- ExperimentLogger.py — Core business logic
- menu.py            — Interactive CLI menu
- main.py            — FastAPI REST endpoints

## API Endpoints
- GET  /view_all_experiments
- GET  /experiments/{exp_id}
- GET  /experiments/best_experiment?metric=accuracy
- GET  /experiments/compare_two_experiments?exp1=id1&exp2=id2
- POST /add_new_experiment
- DELETE /experiments/{exp_id}

## How to Run
## "Known Limitations":
- File paths are currently hardcoded for local development
- To be updated with configurable paths in next version


### CLI Version
python menu.py

### API Version
uvicorn main:app --reload
Then open http://localhost:8000/docs

## What I learned
- OOP design with Python dataclasses
- REST API development with FastAPI
- Data validation with Pydantic
- JSON persistence
- HTTP methods GET POST DELETE
