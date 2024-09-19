import os
import shutil
class Clean_Folder:
    def __init__(self):
        pass

    def folder(self,path):
        try:
            if os.path.exists(path):
                shutil.rmtree(path)
            else:
                self.folder(path)
        except OSError:
            raise OSError
        except Exception as e:
            raise e
