# Welcome to Earbot!

This guide will walk you through the configuration process and have you up and running with Earbot in just a few minutes!

## What is Earbot?

Earbot is a customizable listening bot for Slack. With Earbot you can:

- Add specific phrases for Earbot to listen for
- Configure which channel(s) you'd like Earbot to listen to
- Remove phrases you don't want Earbot to listen for any more

Earbot will send you a DM with a link to the message containing your listen phrase whenever it's mentioned across your Slack team.

## What you'll need before you get started:

1. A Slack team.
Before anything else you'll need a Slack team, free or paid. Either [Sign into an existing Slack workspace](https://get.slack.help/hc/en-us/articles/212681477-Sign-in-to-Slack) or [create a new Slack workspace](https://get.slack.help/hc/en-us/articles/206845317-Create-a-Slack-workspace).

2. A terminal with Python 3.6+ installed.
Check your installation by running the following command in your terminal:
```
$ python3 --version
-> Python 3.6.7
```

You'll need to install Python 3.6 if you receive the following error:
```
-> bash: python3: command not found
```


3. Docker and docker-compose.
If you're on macOS, you can use [Homebrew](https://brew.sh/) and run the following commands in Terminal or iTerm:
```
$ brew install docker docker-compose
```

4. A text editor of your choice. I prefer [Microsoft Visual Studio Code](https://code.visualstudio.com/).

### Give your app permissions

Create an Earbot app on [Slack](https://api.slack.com/apps?new_app=1).

Navigate to **OAuth & Permissions** on the sidebar to add scopes to your app.

- Scroll down to the **Bot Token Scopes** section and click **Add an OAuth Scope**.

Add the following scopes:

- `channels:history`
- `chat:write`
- `commands`
- `groups:read`
- `users:read`

Save your changes.

### Install the app in your workspace

- Scroll up to the top of the **OAuth & Permissions** pages and click the green "Install App to Workspace" button.

You'll need to authorize the app for the Bot User permissions.

- Click the "Allow" button.

Copy and paste the Bot User OAuth Access Token somewhere locally after the app is installed. We'll need this soon.

Navigate to the "Basic Information" tab near the top of the left side navigation menu, click it and then scroll down and view and copy and paste the "Signing Secret" as well.

### Getting up and running locally

### Configuring the events listener

### Adding slash commands

Clone this GitHub repo!

2. Navigate to the directory you've cloned the repo to locally, and open up ```docker.compose.yml```


