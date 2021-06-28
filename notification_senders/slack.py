import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

slack_token = os.environ["SLACK_API_TOKEN"]
client = WebClient(token=slack_token)


def send_message(subject: str, body: str):
  try:
    response = client.chat_postMessage(
      channel="general",
      text=subject + "\n" + body
    )
  except SlackApiError as e:
    assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
