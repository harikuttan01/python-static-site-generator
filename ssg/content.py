import re
from importlib_metadata import metadata
from yaml import  FullLoader, load
from collections.abc import Mapping

class Content(Mapping):
    __delimiter = r"^(?: - |\+){3}\s*$"
    __regex = re.compile(__delimiter,re.MULTILINE)

    @classmethod
    def load(cls,string):
        _,fm,content = __regex.split(string)
        load(fm,Loader=FullLoader)
        return cls(metadata,content)

    def __init__(self,metadata,content):
        self.data = metadata
        self.data["content"] = content

    @property
    def body(self):
        self.data["content"]

    @property
    def type(self):
        return self.data["type"] if "type" in self.data.items() else None

    @type.setter
    def type(self,val):
        self.data["type"] = val

    def __getitem__(self, __k):
        return self.data[__k]

    def __iter__(self):
        return iter(self.data)

    def __len__(self) -> int:
        return len(self.data)

    def __repr__(self) -> str:
        data = {}
        for key,value in self.data.items():
            if key == "content":
                data[key] = value
            else:
                pass
        return str(data)
