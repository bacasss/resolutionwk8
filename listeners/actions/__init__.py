from slack_bolt import App
from .relate_action import relate_action_callback


def register(app: App):
    app.action("relate_button")(relate_action_callback)
