from logging import Logger

from slack_bolt import Ack
from slack_sdk import WebClient
from data import add_conf, save_message_ts

def conf_view_callback(view: dict, ack: Ack, body: dict, client: WebClient, logger: Logger):
    try:
        ack()
        provided_values = view["state"]["values"]
        confession_text = provided_values["confession_block"]["confession_input"]["value"]
        channel_id = provided_values["channel_block"]["channel_select"]["selected_conversation"]
        confession_id = add_conf(confession_text, channel_id)
        response = client.chat_postMessage(
            channel = channel_id,
            text = f"anon confession ({confession_id})",
            blocks=[
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f"*anonymous confession:*\n\n_{confession_text}_"
                    }
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "*0 people can relate.*"
                    },
                    "accessory": {
                        "type": "button",
                        "text": {"type": "plain_text", "text": "i can relate!!"},
                        "action_id": "relate_button",
                        "value": str(confession_id)
                    }
                }
            ]
        )
        message_ts = response["ts"]
        save_message_ts(confession_id, message_ts)
    except Exception as e:
        logger.error(e)

