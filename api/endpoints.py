from typing import Annotated, List
from fastapi import FastAPI, Depends, HTTPException
from starlette.staticfiles import StaticFiles
from pathlib import Path
from sqlalchemy.orm import Session
from sqlalchemy import Select
from api.database import MySession
from api.models import MasterBond, PricesSpreads
from api.schemas import Bond, Prices

app = FastAPI()

PROJECT_ROOT = Path(__file__).parent.parent

def get_session() -> Session:
    session = MySession()
    try:
        yield session
    finally:
        session.close()

@app.get("/bond/{isin}", response_model=Bond)
def get_bond(isin: str, db: Annotated[Session, Depends(get_session)]) -> MasterBond:
    bond = db.get(MasterBond, isin)
    if bond is None:
        raise HTTPException(status_code=404, detail=f"Cannot find any bond with ISIN code {isin}")
    return bond
    
@app.get("/bondlist", response_model=List[Bond])
def get_bondlist(db: Annotated[Session, Depends(get_session)]) -> MasterBond:
    bondlist = db.execute(Select(MasterBond)).scalars()
    bondlist = db.query(MasterBond)
    if bondlist is None:
        raise HTTPException(status_code=404, detail=f"Cannot Execute")
    return bondlist
    

@app.get("/bondprices/{isin}", response_model=List[Prices])
def get_bondprices(isin: str, db: Annotated[Session, Depends(get_session)]) -> PricesSpreads:
    bondprices = db.execute(Select(PricesSpreads).filter(PricesSpreads.ISIN == isin)).scalars()
    if bondprices is None:
        raise HTTPException(status_code=404, detail=f"Cannot find any bond with ISIN code {isin}")
    return bondprices
 

app.mount("/", StaticFiles(directory=PROJECT_ROOT / "html", html=True))
