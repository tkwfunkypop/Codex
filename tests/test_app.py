from app import create_app, __version__


def test_health():
    app = create_app()
    with app.test_client() as c:
        res = c.get("/health")
        assert res.status_code == 200
        assert res.get_json() == {"status": "ok"}


def test_version():
    app = create_app()
    with app.test_client() as c:
        res = c.get("/version")
        assert res.status_code == 200
        assert res.get_json() == {"version": __version__}
