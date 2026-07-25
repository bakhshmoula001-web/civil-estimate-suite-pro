from dataclasses import dataclass
from typing import Optional
@dataclass(slots=True)
class CostReport:
    id: Optional[int]=None
    project_id:int=0
    category:str=""
    amount:float=0.0
    remarks:str=""
