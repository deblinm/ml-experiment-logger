from  ExperimentLogger import ExperimentLogger as EL
from fastapi import FastAPI
from dataclasses import asdict
from pydantic import BaseModel
from datetime import date
from experiment import Experiment
from prometheus_fastapi_instrumentator import Instrumentator

EL_OBJ = EL()
app = FastAPI()
Instrumentator().instrument(app).expose(app)

try:
    EL_OBJ.experiments = EL_OBJ.load_from_file()
except FileNotFoundError:
    pass


@app.get("/view_all_experiments")
def view_all_experiment():
        if not EL_OBJ.experiments:
                        return {"message": "No experiments found."}
        return [asdict(exp) for exp in EL_OBJ.experiments]

class Experiment_Inp(BaseModel):
        model_name: str
        model_parameters: dict
        model_metrics: dict
        experiment_date: date = date.today()
        notes: str
        status: str = 'completed'

@app.post("/add_new_experiment")
def add_experiment(exp_input: Experiment_Inp):
        new_exp = Experiment(**exp_input.model_dump())
        EL_OBJ.add_new_experiment(new_exp)
        EL_OBJ.save_to_file()
        return{"message": "Experiment added successfully", "id": new_exp.id}


@app.get("/experiments/best_experiment")
def get_best_experiment(metric: str):
        best=EL_OBJ.view_best_model(metric)
        if not best:
                return {"message": "No metric found with this name"}
        return asdict(best)

@app.get("/experiments/compare_two_experiments")
def compare_experiment(exp1: str, exp2: str):
        match1 = next (( exp_nm for exp_nm in EL_OBJ.experiments if exp_nm.id == exp1), None)
        match2 = next ((exp_nm for exp_nm in EL_OBJ.experiments if exp_nm.id == exp2), None)
        if not match1:
                return {
                        "message": f"There is no match found with experiment name {exp1}. Please input the exact name and retry. Thank You"}
        elif not match2:
                return {
                        "message":f"There is no match found with experiment name {exp2}. Please input the exact name and retry. Thank You"}
        else:
                return {
                        "model_name": {
                                "experiment_1": match1.model_name,
                                "experiment_2": match2.model_name
                        },
                        "metrics": {
                                key: {
                                        match1.model_name: match1.model_metrics.get(key, "N/A"),
                                        match2.model_name: match2.model_metrics.get(key, "N/A")
                                }
                                for key in match1.model_metrics
                        },
                        "parameters": {
                                key: {
                                        match1.model_name: match1.model_parameters.get(key, "N/A"),
                                        match2.model_name: match2.model_parameters.get(key, "N/A")
                                }
                                for key in match1.model_parameters
                        }
                }

@app.get("/experiments/{exp_id}")
def get_experiment_by_id (exp_id: str):
        match = next((exp for exp in EL_OBJ.experiments if exp.id == exp_id), None)
        if not match:
                return {"message": f"No experiment found with id {exp_id}"}
        return asdict(match)

@app.get("/health")
def get_health_check_status_For_kubernetes():
        return {"status": "healthy"}


@app.delete("/experiments/{exp_id}")
def del_experiment(exp_id: str):
        match = next((exp for exp in EL_OBJ.experiments if exp.id == exp_id), None)
        if not match:
                return {"message": f"No experiment found with id {exp_id}"}
        else:
                EL_OBJ.experiments.remove(match)
                EL_OBJ.save_to_file()
                return {"message": f"Experiment id {exp_id} successfully deleted"}
