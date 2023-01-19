import pyfiglet
from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/")
def main(text: str, font: str = "standard"):
    if font not in pyfiglet.FigletFont.getFonts():
        return HTTPException(
            status_code=404,
            detail=f"Font '{font}' not found. Check /fonts for available fonts.",
        )
    res = pyfiglet.figlet_format(text, font=font)
    return {"status_code": 200, "result": res}


@app.get("/fonts")
def fonts():
    return {"status_code": 200, "fonts": pyfiglet.FigletFont.getFonts()}
