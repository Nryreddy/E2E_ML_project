import os
import sys
import numpy as np
import pandas as pd
import dill

from src.exception import CustomException

def save_object(file_path, obj):
    """
    For saving the pickel file

    Args:
        file_path (_type_): preprocessor object file path of transformed_data
        obj (_type_): preprocessing object  (data transformation)
    """
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)                 #dill extends python’s pickle module for serializing and de-serializing. 

    except Exception as e:
        raise CustomException(e, sys)
