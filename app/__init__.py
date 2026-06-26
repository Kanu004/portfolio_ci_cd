import os

from flask import Flask


def create_app(config=None):
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    app = Flask(
        __name__,
        template_folder=os.path.join(base_dir, "templates"),
        static_folder=os.path.join(base_dir, "static"),
    )

    if config:
        app.config.update(config)

    from app.routes import bp

    app.register_blueprint(bp)

    return app
