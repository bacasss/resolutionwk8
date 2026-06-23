from logging import Logger

from slack_bolt import Ack
from slack_sdk import WebClient
from data import add_relate, get_conf_by_id


def relate_action_callback(ack: Ack, client: WebClient, body: dict, logger: Logger):
    try:
        ack()
        action = body["actions"][0]
        confession_id = int(action["value"])
        add_relate(confession_id)
        confession = get_conf_by_id(confession_id)
        channel_id = body["channel"]["id"]
        message_ts = body["message"]["ts"]
        client.chat_update(
            channel = channel_id,
            ts = message_ts,
            blocks=[
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f"*anonymous confessionnn:\n\n_{confession['message']}_"
                    }
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f"*{confession['relates']} people can relate!!*"
                    },
                    "accessory": {
                        "type": "button",
                        "text": {"type": "plain_text", "text": "I can relate!!!"},
                        "action_id": "relate_button",
                        "value": str(confession_id)
                    }
                }
            ],
            text=f"Anonymous confession ({confession['relates']} relates)"
        )



    except Exception as e:
        logger.error(e)
