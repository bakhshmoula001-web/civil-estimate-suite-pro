from dataclasses import dataclass
from typing import Optional
@dataclass(slots=True)
class Material:
    id: Optional[int]=None
    project_id:int=0
    material_name:str=""
    unit:str=""
    quantity:float=0.0
    rate:float=0.0
    amount:float=0.0
