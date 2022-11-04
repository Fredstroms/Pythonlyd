import winsound
from fileinput import filename
from typing import Union

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, PlainTextResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from uvicorn import run

app = FastAPI()
#import staticfiles og skriv koden under, (directory er mappen som blir statisk)
app.mount("/static", StaticFiles(directory="static"), name="static")

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


#Denne koden linker til html dokument
@app.get("/", response_class=PlainTextResponse)
async def main():
    with open("piano.html", "r") as f:
       html = f.read()
    return HTMLResponse(content=html, status_code=200)
   
if __name__ == "__main__":
    run("piano_api:app", host="0.0.0.0", reload=True)
    


 
#uvicorn lyd_api:app --reload --host 0.0.0.0
#datamaskinens ip + porten eksempel:(0.0.0.0:8000) /add?x=(skrivtall)&y=(skrivtall)
#Blackjack: sett opp enkelt python dokument, kan egentlig kopiere denne.
#Putt bilder, css og js i statisk mappe
