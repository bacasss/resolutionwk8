from slack_bolt import App
from .confess_view import conf_view_callback


def register(app: App):
    app.view("confess_modal")(conf_view_callback)
