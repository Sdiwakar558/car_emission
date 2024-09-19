from datetime import datetime
class Logwriter:
    def __init__(self):
        self.curr_date = datetime.now()
        self.date = self.curr_date.date()
        self.time = self.curr_date.strftime("%H:%M:%S")
    def writelog(self,fileObj,message):
        fileObj.write(f"{self.date}\t{self.time}\t{message}\n")