from dataclasses import dataclass, field, asdict
from experiment import Experiment
from typing import List
import json

@dataclass
class ExperimentLogger:
    experiments: List[Experiment]= field(default_factory=list)

    def add_new_experiment(self,experiment):
        self.experiments.append(experiment)

    def filter_by_model(self,model_name):
        count=0
        model_list=[]
        for exp in self.experiments:
            if exp.model_name == model_name:
                count += 1
                model_list.append(exp)

        if count == 0:
                    print(f"There are no match to the model name {model_name}. Please input the exact name and retry. Thank You")
        else:
            print(f"{count} model name matched. Here are the details \n")
            for models in model_list:
                print(models)

    def view_best_model(self,in_metric):
        if not any(in_metric in exp.model_metrics for exp in self.experiments ):
            return None
        else:
            best_experiment = max(
            self.experiments,
            key=lambda exp: exp.model_metrics.get(in_metric, 0)
        )
            return best_experiment

    def save_to_file(self):
        path = "\\Users\\deblin\\PycharmProjects\\TargetFiles\\"
        file_name = "ML_Experiment_Logger"
        experiment_dict = [asdict(exp) for exp in self.experiments]
        with open (f"{path}{file_name}.json",'w') as f:
                json.dump(experiment_dict,f,indent=4, default=str)


    def load_from_file(self):
        path = "\\Users\\deblin\\PycharmProjects\\TargetFiles\\"
        file_name = "ML_Experiment_Logger"
        data_list = []
        with open(f"{path}{file_name}.json", 'r') as ip_file:
            reader = json.load(ip_file)
            for row in reader:
                data_obj = Experiment(**row)
                data_list.append(data_obj)
        return data_list