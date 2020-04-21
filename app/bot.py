import os
import logging
from flask import Flask, jsonify, request
from flask_restful import Resource
from slack import WebClient
from slackeventsapi import SlackEventAdapter
import ssl as ssl_lib
import certifi

# Initialize Flask
app = Flask(__name__)

# Initialize Slack events adapter using Flask app
slack_events_adapter = SlackEventAdapter(
    os.environ["SLACK_SIGNING_SECRET"], "/slack/events", app)

# In-memory storage for listening configurations per-user
listen_config = {}


@app.errorhandler(500)
def error(self):
    return jsonify({"text": "Oh no! Something went horribly wrong!"})


@app.route("/listen/add", methods=['POST'])
def listen_add():
    """Allows users to add specific listening phrases.
    """
    # Grab request content
    listen_data = request.form
    # Set user_id variable
    listen_user_id = listen_data['user_id']
    # Set channel_id variable
    listen_channel_id = listen_data['channel_id']
    # Set channel_name variable
    listen_channel_name = listen_data['channel_name']
    # Set phrase variable
    listen_phrase = listen_data['text'].strip()
    # Check if user already has created a config
    if listen_user_id in listen_config:
        # Check if there is a channel config for the user
        if listen_channel_id in listen_config[listen_user_id] and listen_phrase not in listen_config[listen_user_id][listen_channel_id]:
            listen_config[listen_user_id][listen_channel_id].append(
                listen_phrase)
            return jsonify({
                "text": f"Okay, I'll listen for `{listen_phrase}` in `{listen_channel_name}` from now on!"
            })
        elif listen_channel_id in listen_config[listen_user_id] and listen_phrase in listen_config[listen_user_id][listen_channel_id]:
            return jsonify({
                "text": f"I'm already listening for `{listen_phrase} `in `{listen_channel_name}`!"
            })
        elif listen_channel_id not in listen_config[listen_user_id]:
            listen_config[listen_user_id][listen_channel_id] = []
            listen_config[listen_user_id][listen_channel_id].append(
                listen_phrase)
            return jsonify({
                "text": f"Okay, I'll listen for `{listen_phrase}` in `{listen_channel_name}` from now on!"
            })
    # If the user doesn't yet have a config, create one
    elif listen_user_id not in listen_config:
        listen_config[listen_user_id] = {}
        listen_config[listen_user_id][listen_channel_id] = []
        listen_config[listen_user_id][listen_channel_id].append(listen_phrase)
        return jsonify({
            "text": f"Okay, I'll listen for `{listen_phrase}` in `{listen_channel_name}` from now on!"
        })


@app.route("/listen/delete", methods=['POST'])
def listen_delete():
    """Stops listening for the phrases that are specified.
    """
    # Grab request content
    listen_data = request.form
    # Set user_id variable
    listen_user_id = listen_data['user_id']
    # Set channel_id variable
    listen_channel_id = listen_data['channel_id']
    # Set channel_name variable
    listen_channel_name = listen_data['channel_name']
    # Set phrase variable
    listen_phrase = listen_data['text'].strip()
    # Remove user-specific phrase from listen_config
    if listen_user_id in listen_config:
        if listen_channel_id in listen_config[listen_user_id] and listen_phrase in listen_config[listen_user_id][listen_channel_id]:
            listen_config[listen_user_id][listen_channel_id].remove(listen_phrase)
            return jsonify({
                "text": f"Okay, I won't listen for `{listen_phrase}` in `{listen_channel_name}` anymore!"
            })
        elif listen_channel_id in listen_config[listen_user_id] and listen_phrase not in listen_config[listen_user_id][listen_channel_id]:
            return jsonify({
                "text": f"I wasn't able to find a listening rule for `{listen_phrase}` in `{listen_channel_name}`"
            })
        elif listen_channel_id not in listen_config[listen_user_id]:
            return jsonify({
                "text": f"I wasn't able to find any listen rules for `{listen_channel_name}`. You can set up a new rule by typing `/listen` and the phrase you want me to listen for."
            })
    elif listen_user_id not in listen_config:
        return jsonify({
            "text": f"Sorry, I'm not listening for any phrases for you yet! You can set up a new rule by typing `/listen` and the phrase you want me to listen for."
        })

## THIS CODE IS INCOMPLETE ## Event listener for specific messages that match listen_config criteria
# @slack_events_adapter.on("message")
# def message(payload):
#     """Searches for matching listening words each time a message is sent in any Slack channel, team-wide.
#     """
#     # Capture message event
#     msg_event = payload.get("event", {})
#     # Parse event for pertinent information
#     msg_channel_id = msg_event.get("channel")
#     msg_text = msg_event.get("text")

#     print(msg_text)
#     print(msg_channel_id)
#     # Search for any matches
#     tmp_msg_channel_id = []
#     for k1,v1 in listen_config.items():
#         counter = ""
#         counter+= k1
#         for k2,v2 in v1.items():
#            if msg_text == v2:
#                 print(v2)
#                 tmp_msg_channel_id.append(v2)

## THIS CODE IS INCOMPLETE ## 

if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.addHandler(logging.StreamHandler())
    ssl_context = ssl_lib.create_default_context(cafile=certifi.where())
    app.run(port=3000, host="0.0.0.0")
