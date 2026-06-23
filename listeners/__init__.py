from slack_bolt import App

from listeners.commands import register as reg_commands
from listeners.events import register as reg_events
from listeners.actions import register as reg_actions
from listeners.views import register as reg_views

def register_listeners(app):
    reg_commands(app)
    reg_events(app)
    reg_actions(app)
    reg_views(app)
