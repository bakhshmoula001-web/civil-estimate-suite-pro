from dataclasses import dataclass
from typing import Optional
@dataclass(slots=True)
class BOQItem:
    id: Optional[int]=None
    project_id:int=0
    item_no:str=""
    description:str=""
    unit:str=""
    quantity:float=0.0
    rate:float=0.0
    amount:float=0.0
    remarks:str=""
