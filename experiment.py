import uuid
from dataclasses import dataclass, field
from datetime import date


@dataclass (kw_only = True)
class Experiment:
    id : str = field (default_factory=lambda : uuid.uuid4().hex)
    model_name: str
    model_parameters: dict
    model_metrics: dict
    experiment_date: date = date.today()
    notes: str
    status: str = 'completed'

    def __str__(self):
        return (f"ID : {self.id}. "
                f"Model Name : {self.model_name}\n"
                f"Model Parameters : {self.model_parameters}\n"
                f"Model Metrics :  {self.model_metrics}\n"
                f"Experiment Date :  {self.experiment_date}\n"
                f"Status :  {self.status}\n")





