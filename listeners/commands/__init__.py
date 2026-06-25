from slack_bolt import App
from .confess_command import confess_command_callback


def register(app: App):
    app.command("/confess")(confess_command_callback)
    app.command("/uselesscmd67")(confess_command_callback)
