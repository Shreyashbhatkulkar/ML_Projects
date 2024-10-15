import sys
from dataclasses import dataclass

import os
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer       ##to create pipeline for transformations
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler

from src.exception import CustomException
from src.logger import logging

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts',"preprocessor.pkl")
    
class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
    
    def get_data_transformer_object(self):
        try:
            numerical_columns = ['writing_score','reading_score']
            categorical_columns = ['gender',
                                   'race_ethnicity',
                                   'lunch',
                                   'test_preparation_course']
            
            num_pipeline = Pipeline(
                steps= [
                    ("imputer",SimpleImputer(strategy="median"))
                    ("scaler",StandardScaler())
                ]
                cat_pipeline = Pipeline(
                    steps=[]
                )
            )
        except:
            pass