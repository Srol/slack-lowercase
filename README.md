# Slack-Lowercase

This is a simple Slack integration I was asked by a colleague to make. 

Any text sent to it using a slash command is made lowercase.

I didn't think there was any need for this, but a friend asked for it so hopefully it helps somebody out there. ¯\_(ツ)_/¯

## How it works.

Type in your command like so `/lowercase THE TEXT YOU WANT LOWERCASED`. The bot will then reply with `The text you want lowercased`. It will automatically title case any words at the start of sentences, but it cannot recognize proper nouns. 

Here's how you formate proper nouns: `/lowercase THIS WAS WRITTEN BY **PATRICK **HOGAN.` That returns as `This was written by Patrick Hogan.`

## Setup

1. Clone this repository.
2. Create a new Slack slash command (I use /lowercase). 
3. Copy the token from this command to line 7 of lowercase.py
4. Create a new Heroku app.
5. Copy the URL from this new app, plus the endpoint of "/request" to the slash command configuration page.
6. Push the repository to Heroku.
7. That's it basically.