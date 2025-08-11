from __future__ import annotations

import os
import argparse
from flask import Flask, jsonify


def create_app() -> Flask:
    """Create and configure the Flask application."""
    app = Flask(__name__)

    @app.get("/health")
    def health():
        return jsonify(status="ok")

    @app.get("/version")
    def version():
        return jsonify(version="1.0.0")

    return app


def main(argv=None) -> int:
    """CLI entrypoint."""
    parser = argparse.ArgumentParser(description="Codex secure sample app")
    parser.add_argument("--name", default="World", help="Name to greet")
    parser.add_argument(
        "--serve",
        action="store_true",
        help="Run Flask server",
    )
    args = parser.parse_args(argv)

    if args.serve:
        app = create_app()
        port = int(os.environ.get("PORT", "8000"))
        app.run(host="127.0.0.1", port=port)
        return 0

    print(f"Hello, {args.name}!")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
