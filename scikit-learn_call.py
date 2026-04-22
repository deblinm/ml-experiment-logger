from datetime import date

from sklearn.model_selection import train_test_split
from ML_Experiment_Logger.ETL_Titanic_DataSet import run_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from app.experiment import Experiment
from app.ExperimentLogger import  ExperimentLogger

df = run_pipeline()

X = df.drop(columns=['Survived'])
Y = df['Survived']

X_train, X_test, y_train, y_test = train_test_split(X,Y,test_size=0.2, random_state=10)
model= LogisticRegression(random_state=42, max_iter=1000)
model.fit(X_train, y_train)
predictions = model.predict(X_test)
accuracy = accuracy_score( predictions,y_test)
classification_res = classification_report(y_test,predictions,output_dict=True)

model_met = {
    "accuracy": round(accuracy,4),
    "precision_survived": round(classification_res['1']['precision'],4),
    "recall_survived" : round(classification_res['1']['recall'],4),
    "f1_survived":  round(classification_res['1']['f1-score'],4),
    "precision_not_survived": round(classification_res['0']['precision'],4),
    "recall_not_survived" : round(classification_res['0']['recall'],4),
    "f1_not_survived":  round(classification_res['0']['f1-score'],4),
    "precision_weighted_avg": round(classification_res['weighted avg']['precision'],4),
    "recall_weighted_avg" : round(classification_res['weighted avg']['recall'],4),
    "f1_weighted_avg":  round(classification_res['weighted avg']['f1-score'],4)
}


logger = ExperimentLogger()
exp = Experiment (
    model_name="Logistic Regression",
    model_parameters={"max_iter": 1000, "random_state": 42},
    model_metrics= model_met,
    experiment_date = date.today(),
    notes="First model on Titanic dataset")

logger.add_new_experiment(exp),
logger.save_to_file()

print("Experiment logged successfully!")


