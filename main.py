from fastapi import FastAPI, HTTPException
from schemas import RizzUrlChoices, Boi

app = FastAPI()

BOIZ = [
    {'id': 1, 'name': 'Yash', 'rizz': 'Ultra'},
    {'id': 2, 'name': 'Tavish', 'rizz': 'Thikthak', 'huzz': [
        {'title': 'side chick', 'date_rizzed': '2024-09-11'}
    ]},
    {'id': 3, 'name': 'Fawzaan', 'rizz': 'Daddy'},
    {'id': 4, 'name': 'Tejas', 'rizz': 'Ultra'},
]

@app.get("/boiz")
async def boiz(rizz: RizzUrlChoices | None = None) -> list[Boi]:
    if rizz:
        return[
            Boi(**b) for b in Boiz if b['rizz'].lower() == rizz.value
        ]
    return[
        Boi(**b) for b in BOIZ
    ]

@app.get("/boiz/{boiz_id}")
async def boi(boiz_id: int) -> Boi:
    boi = next((Boi(**b) for b in BOIZ if b['id'] == boiz_id), None)
    if boi is None :
        #Status code 404
        raise HTTPException(status_code=404, detail='Boi not found')
    return boi

@app.get("/boiz/rizz/{rizz}")
async def boiz_by_rizz(rizz: RizzUrlChoices) -> list[dict]:
    return[
        b for b in BOIZ if b['rizz'].lower() == rizz.lower() 
    ]



