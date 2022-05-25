from typing import List
import shutil
from pathlib import Path

class Parser:
    
    def __init__(self):
        self.extensions : List[str] = []

    def valid_extension(self,extension):
        return True if extension in self.extensions else False
    
    def parse(self,source,dest,path):
        self.source = Path(source)
        self.dest = Path(dest)
        self.path = Path(path)
        raise NotImplementedError

    def read(self,path):
        with open(path,'r') as file:
            f = file.read()
            return f
    
    def write(self,path,dest,content,ext = ".html"):
        full_path = self.dest / path.with_suffix(ext).name
        with open(full_path,'w') as file:
            file.write(content)

    def copy(self,path,source,dest):
        shutil.copy2(path, dest / path.relative_to(source))

class ResourceParser(Parser):

    EXTENSIONS = ['.jpg','.png','.gif','.css','.hmtl']
    def parse(self,source,dest,path):
        super().copy(path,source,dest)
        