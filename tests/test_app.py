from app import create_app, main


def test_cli_greeting(capsys):
    rc = main(["--name", "Kenta"])
    assert rc == 0
    out = capsys.readouterr().out.strip()
    assert out == "Hello, Kenta!"


def test_health_endpoint():
    app = create_app()
    client = app.test_client()
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.get_json()["status"] == "ok"


def test_version_endpoint():
    app = create_app()
    client = app.test_client()
    resp = client.get("/version")
    assert resp.status_code == 200
    assert resp.get_json()["version"] == "1.0.0"
