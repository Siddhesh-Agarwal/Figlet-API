import pyfiglet
from flask import Flask, jsonify, request

app = Flask(__name__)


# convert text to ascii art
@app.route("/")
def main():
    text = request.args.get("text")
    font = request.args.get("font", "standard")
    if text is None:
        return (
            jsonify(
                {
                    "status_code": 400,
                    "detail": "Missing required parameter 'text'",
                }
            ),
            400,
        )
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


# list all available fonts
@app.route("/fonts")
def fonts():
    return pyfiglet.FigletFont.getFonts()


# error handler
@app.errorhandler(400)
def bad_request(e):
    return jsonify({"status_code": 400, "detail": "Bad request"}), 400


@app.errorhandler(404)
def not_found(e):
    return jsonify({"status_code": 404, "detail": "Not found"}), 404


if __name__ == "__main__":
    app.run()
