import os
import pandas as pd
from mlproject import logger
from sklearn.linear_model import ElasticNet, LogisticRegression
from xgboost import XGBClassifier
import joblib
from mlproject.entity.config_entity import ModelTrainerConfig

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    
    def train(self):
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)


        train_x = train_data.drop([self.config.target_col], axis=1)
        test_x = test_data.drop([self.config.target_col], axis=1)
        train_y = train_data[[self.config.target_col]]
        test_y = test_data[[self.config.target_col]]


        # lr = ElasticNet(alpha=self.config.alpha, l1_ratio=self.config.l1_ratio, random_state=42)
        # lr.fit(train_x, train_y)

        xgb_model = XGBClassifier(
        objective = self.config.objective,  # Binary classification
        eval_metric = self.config.eval_metric,  # Use AUC as the evaluation metric
        random_state=42
        )

        xgb_model.fit(train_x, train_y)

        joblib.dump(xgb_model, os.path.join(self.config.root_dir, self.config.model_name))

