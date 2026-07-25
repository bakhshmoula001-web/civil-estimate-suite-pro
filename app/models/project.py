from dataclasses import dataclass
from typing import Optional
@dataclass(slots=True)
class Project:
    id: Optional[int]=None
    project_code:str=""
    project_name:str=""
    client_name:str=""
    consultant:str=""
    contractor:str=""
    location:str=""
    start_date:str=""
    end_date:str=""
    status:str="Planning"
    remarks:str=""
    created_at:str=""
    updated_at:str=""
