import os
from idlelib.iomenu import encoding

import pandas as pd

class Read_file:
    def __init__(self,csv_file_path):   ##default constructor to initialize path
        self.raw_file_path= csv_file_path
    def read_csv(self,encoading_type):   ## it will return a raw dataframe
        try:
            if os.path.exists(self.raw_file_path):
                raw_dataframe = pd.read_csv(self.raw_file_path,encoding=f"{encoading_type}")
                return raw_dataframe
            else:
                return  "File path not exist"
        except Exception as e:
            raise e
