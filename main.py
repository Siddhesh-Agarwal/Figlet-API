import pyfiglet
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()


# allow CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# convert text to ascii art
@app.get("/")
def main(text: str, font: str="standard"):
    if text is None:
        return {"status": "ok"}
    if font not in pyfiglet.FigletFont.getFonts():
        return {"status": "error", "message": "font not found"}
    res = pyfiglet.figlet_format(text, font)
    return {"status": "ok", "text": text, "font": font, "ascii": res}


# list all available fonts
@app.get("/fonts")
def fonts():
    return pyfiglet.FigletFont.getFonts()


