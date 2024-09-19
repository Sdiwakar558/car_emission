import chardet

def get_encoading_details(file_path):
    with open(file_path,'rb') as file:
        raw_data = file.read(20000)
    result= chardet.detect(raw_data)
    return result
