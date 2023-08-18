from typing import List
import pyfiglet
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(
    title="Figlet API",
    description="Convert text to ascii art",
    version="1.0.0",
    docs_url="/",
    redoc_url=None,
    deprecated=False,
)


# allow CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)


class Response(BaseModel):
    text: str
    font: str
    ascii: pyfiglet.FigletString


# convert text to ascii art
@app.get("/ascii")
def main(text: str, font: str = "standard") -> Response:
    if font not in pyfiglet.FigletFont.getFonts():
        raise ValueError("Invalid font name")
    ascii: pyfiglet.FigletString = pyfiglet.figlet_format(text, font)
    return Response(text=text, font=font, ascii=ascii)


# list all available fonts
@app.get("/fonts")
def fonts() -> List[str]:
    return pyfiglet.FigletFont.getFonts()  # type: ignore
