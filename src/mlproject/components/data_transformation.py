from mlproject import logger
import os
from mlproject.entity.config_entity import TransformationConfig
import pandas as pd
from sklearn.model_selection import train_test_split



class DataTransformation:
    def __init__(self, config: TransformationConfig):
        self.config = config

    
    def preprocessing(self):
        data = pd.read_csv(self.config.data_path)
        # data['quality'] = data['quality'].apply(lambda x: 1 if x >= 7 else 0)
        # Manually map the labels to expected classes
        label_mapping = {3: 0, 4: 1, 5: 2, 6: 3, 7: 4, 8: 5}
        data["quality"] = data["quality"].map(label_mapping)
        data_copy = data.copy()

        for column in data.columns[:-1]:  # Exclude 'quality' since it's the target
            Q1 = data[column].quantile(0.25)
            Q3 = data[column].quantile(0.75)
            IQR = Q3 - Q1
            
            # Define bounds for outliers
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            
            # Replace outliers with the median
            median = data[column].median()
            data[column] = data[column].apply(
                lambda x: median if (x < lower_bound or x > upper_bound) else x
            )
        
        data['quality'] = data_copy['quality']
        return data


    def train_test_spliting(self, data):

        # Split the data into training and test sets. (0.75, 0.25) split.
        train, test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"),index = False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"),index = False)

        logger.info("Splited data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)
        