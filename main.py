from typing import List
import pyfiglet  # type: ignore
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
    ascii: str

    class Config:
        schema_extra: dict[str, dict[str, str]] = {
            "example": {
                "text": "Hello World",
                "font": "standard",
                "ascii": pyfiglet.figlet_format("Hello World"),  # type: ignore
            }
        }


# convert text to ascii art
@app.get("/ascii")
def main(text: str, font: str = "standard") -> Response:
    if font not in pyfiglet.FigletFont.getFonts():
        raise ValueError("Invalid font name")
    ascii: pyfiglet.FigletString = pyfiglet.figlet_format(text, font)  # type: ignore
    return Response(text=text, font=font, ascii=ascii)


# list all available fonts
@app.get("/fonts")
def fonts() -> List[str]:
    return pyfiglet.FigletFont.getFonts()  # type: ignore


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=10000)  # type: ignore
