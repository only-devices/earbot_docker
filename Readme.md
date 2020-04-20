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

## Getting started

1. Clone this GitHub repo
