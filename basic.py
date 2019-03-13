#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask
from flask_bootstrap import Bootstrap
from flask import current_app, Blueprint, render_template
from flask_nav import Nav
from flask_nav.elements import Navbar, View, Separator, Text, Subgroup
import os

nav = Nav()
topbar = Navbar(
    "", View("Home", "frontend.index"), Text("Foo"), Subgroup("Products", Text("Bar"), Separator(), Text("Baz"))
)
nav.register_element("top", topbar)


# Blueprint
frontend_cfg = {
    "name": "frontend",
    "import_name": __name__,
    "static_folder": "static",
    "static_url_path": "/static_url",
    "template_folder": "templates",
    "url_prefix": None,
    "subdomain": None,
    "url_defaults": None,
}
frontend = Blueprint(**frontend_cfg)


@frontend.route("/")
def index():
    return render_template("index.html")


@frontend.route("/html5")
def html5():
    return render_template("html5.html")


def create_app():
    app = Flask(__name__)
    app.config["DEBUG"] = True
    app.config["SECRET_KEY"] = os.urandom(12).hex()
    app.config["BOOTSTRAP_SERVE_LOCAL"] = True

    Bootstrap(app)
    nav.init_app(app)

    blueprint_cfg = {"blueprint": frontend, "url_prefix": "/", "subdomain": None}
    app.register_blueprint(**blueprint_cfg)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
