# mlflow_script.py
import dagshub
dagshub.init(repo_owner='DataWhizEngineer', repo_name='MLops_EndToEnd', mlflow=True)

import mlflow
with mlflow.start_run():
    
    mlflow.log_metric('metric name', 1)