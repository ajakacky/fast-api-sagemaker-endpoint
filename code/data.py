from dataclasses import dataclass
from typing import List
from enum import Enum

class Datatype(Enum):
    derived, config, source = range(3)

@dataclass
class Result:
    data: str
    score: float
    datatype: Datatype = Datatype.derived

@dataclass
class Version:
    model_version: str
    image_version: str
    datatype: Datatype = Datatype.config

@dataclass
class Source:
    lob: str
    correlation_id: str
    datatype: Datatype = Datatype.source

@dataclass
class Model:
    features: List[str]
    result: Result

@dataclass
class VisibilityDoc:
    model: Model
    version: Version
    source: Source

if __name__ == "__main__":
    type_dict = {
        Datatype.source: "",
        Datatype.config: "hgs",
        Datatype.derived: "brrw"
    }