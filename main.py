import pyfiglet
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def main():
    text = request.args.get("text")
    font = request.args.get("font", "standard")
    if font not in pyfiglet.FigletFont.getFonts():
        return (
            jsonify(
                {
                    "status_code": 404,
                    "detail": f"Font '{font}' not found. Check /fonts for available fonts.",
                }
            ),
            404,
        )

    res = pyfiglet.figlet_format(text, font=font)
    return jsonify({"text": text, "font": font, "ascii": res})


@app.route("/fonts")
def fonts():
    return pyfiglet.FigletFont.getFonts()
