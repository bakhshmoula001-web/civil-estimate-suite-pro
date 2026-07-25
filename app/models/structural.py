from dataclasses import dataclass
from typing import Optional
@dataclass(slots=True)
class StructuralReport:
    id: Optional[int]=None
    project_id:int=0
    member_name:str=""
    specification:str=""
    quantity:float=0.0
    remarks:str=""
