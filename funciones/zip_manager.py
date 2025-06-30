    
class Zip_Manager():
    def __init__(self):
        self  

    def zip_write_str(self, zipf, name, content):
        zipf.writestr(name, content)
        return zipf

    def zip_write(self, zipf, name, content):
        zipf.write(name, content)
        return zipf