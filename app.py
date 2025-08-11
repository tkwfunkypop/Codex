from __future__ import annotations

from flask import Flask, jsonify

__version__ = "1.0.0"


def create_app() -> Flask:
    app = Flask(__name__)

    @app.get("/health")
    def health():
        return jsonify({"status": "ok"})

    @app.get("/version")
    def version():
        return jsonify({"version": __version__})

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=8000)
