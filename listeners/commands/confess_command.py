from slack_bolt import Ack, Respond
from logging import Logger
from slack_sdk import WebClient


def confess_command_callback(ack: Ack, body: dict, client: WebClient, logger: Logger):
    try:
        ack()
        client.views_open(
            trigger_id=body["trigger_id"],
            view = {
                "type": "modal",
                "callback_id": "confess_modal",
                "title": {"type": "plain_text", "text": "confess something!"},
                "submit": {"type": "plain_text", "text": "post anonymouslyy"},
                "close": {"type": "plain_text", "text": "cancel"},
                "blocks": [
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "*your confession will be posted anonymously!*"
                        }
                    },
                    {
                        "type": "divider"
                    },
                    {
                        "type": "input",
                        "block_id": "confession_block",
                        "label": {"type": "plain_text", "text": "whats upp"},
                        "element": {
                            "type": "plain_text_input",
                            "action_id": "confession_input",
                            "multiline": True,
                            "placeholder": {
                                "type": "plain_text",
                                "text": "i love pineapple on pizza!!!!"
                            }
                        }
                    },
                    {
                        "type": "input",
                        "block_id": "channel_block",
                        "label": {"type":  "plain_text", "text": "post to channel"},
                        "element": {
                            "type": "conversations_select",
                            "action_id": "channel_select",
                            "placeholder": {"type": "plain_text", "text": "pick a channel"}
                        }
                    }
                ]
            }
        )

    except Exception as e:
        logger.error(e)
