from logging import Logger

from slack_sdk import WebClient
from data import load_conf


def app_home_opened_callback(client: WebClient, event: dict, logger: Logger):
    # ignore the app_home_opened event for anything but the Home tab
    if event["tab"] != "home":
        return
    try:
        confessions = load_conf()
        blocks = [
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": "anonymous confessions boarddd"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "use */confess* in any channel to post anonymously."
                }
            },
            {
                "type": "divider"
            }
        ]
        if len(confessions) == 0:
            blocks.append({
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "_no confssions yet :(_"
                }

            })
        else:
            for confession in reversed(confessions):
                blocks.append({
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f"_{confession['message']}_\n\n *{confession['relates']} people can relate!*"
                    }

                })
                blocks.append({"type": "divider"})
        client.views_publish(
            user_id=event["user"],
            view = {
                "type": "home",
                "blocks": blocks
            }
        )


    except Exception as e:
        logger.error(f"Error publishing home tab: {e}")
