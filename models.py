
from pydantic import BaseModel, Field
class TeroristCllas(BaseModel):
    name : str = Field(...)
    location : str = Field(...)
    danger_rate : str = Field(..., ge=0, le=10)

    # def get_dict(self):
    #     return {"name":self.name, "location":self.location ,"danger_rate":self.danger_rate}