from CSV_reader.Read_csv import Read_file
import os
from CSV_Encode_details.Encode_data import get_encoading_details
from Data_validation.Validation import File_validation
from Data_preprocessing.Raw_DataPreprocessing import DataPreprocessing
from CSV_Encode_details.Encode_data import get_encoading_details
from CSV_reader.Read_csv import Read_file
from Logger.Log_writer import Logwriter
from Encode.Encode_dataframe import Encode
from Data_Visual.Data_visualization import Data_visual

class Calling_function:
    def __init__(self):
        self.cwd = os.getcwd()
        self.raw_data_path = os.path.join(self.cwd,os.getenv("Raw_data_path"))
        self.merge_dataset_path= os.path.join(self.cwd,os.getenv("Client_merge_dataset"))

        self.Log_write = Logwriter()
        self.Log_file = os.path.join(self.cwd,"Log_file")


    def calling_function(self):
        log_file_path = os.path.join(self.Log_file,"process.txt")
        fileObj = open(log_file_path,'r+')
        self.Log_write.writelog(fileObj,"Process started")
        file_list = os.listdir(self.raw_data_path)[0]

        final_raw_data_filepath = os.path.join(self.raw_data_path,file_list)
        self.Log_write.writelog(fileObj, "till raw data file")
        dataset_return_val = get_encoading_details(final_raw_data_filepath)
        self.Log_write.writelog(fileObj, f"{dataset_return_val} ")
        dataframes = Read_file(final_raw_data_filepath).read_csv(dataset_return_val['encoding'])
        encoded_data = Encode().encode_data(dataframes)
        Data_visual().data_visual(encoded_data)










if __name__=="__main__":
    Calling_function().calling_function()



