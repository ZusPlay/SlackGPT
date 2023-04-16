#slackbot

## Content
<ul>
    <li><a href="#create-an-app-in-slack">Create an app in Slack</a></li>
    <li><a href="#setting-up-the-env-file">Setting up the env file</a></li>
    <ul><li><a href="#slack_bot_token">slack_bot_token</a></li></ul>
    <ul><li><a href="#slack_app_token">slack_app_token</a></li></ul>
    <ul><li><a href="#openai_api_key">openai_api_key</a></li></ul>
    <ul><li><a href="#ai_model">ai_model</a></li></ul>
    <ul><li><a href="#buffer_message_count">buffer_message_count</a></li></ul>
    <ul><li><a href="#template_path">template_path</a></li></ul>
    <ul><li><a href="#logfile_path">logfile_path</a></li></ul>
</ul>

## Create an app in Slack

Before we start setting up the bot, we need to create an application in Slack.
To get started go here: https://api.slack.com/.
Next, click on the "Create an app" button.

![Example 1](https://i.imgur.com/EDBry2P.png)

Next, select the item "From scratch". After that, fill in the "App Name" (in my case, it's "SlackGPT")
and select "Pick a workspace to develop your app in:" (in my case it's "Test_Workspace") and click on
"Create App".

After that, we get to the page "Basic Information" where below, in the category "Display Information"
we can customize the app title, avatar, background theme color and description.

To configure the bot to interact with it, we find the category "Add features and functionality"
and select the "Add features and functionality" item, where we see a list of configurations.

![Example 2](https://i.imgur.com/4FC0MkQ.png)

Go to the "Permissions" category. Here we need the "Scopes" category where we see the dropdown,
where it says "Add permission by Scope or API method...", click on it and select there
"chat:write" and "chat:write.public".

![Example 3](https://i.imgur.com/Laynk27.png)

Then in the sidebar select "Socket Mode" category.

![Example 4](https://i.imgur.com/jLBjmrc.png)

Then we enable "Enable Socket Mode" and are asked to generate an app-level token,
which we'll need later on. Specify any name you like and press "Generate":

![Example 5](https://i.imgur.com/Wq2j0mc.png)

Then we see "Token", which we want to copy and paste as `slack_app_token` attribute
in the env file. Press Done.

![Example 6](https://i.imgur.com/7tRdg6U.png)

Then in the sidebar choose category "Event Subscriptions".

![Example 7](https://i.imgur.com/nTQutVs.png)

Here we need to enable "Enable Events". Next, select "Subscribe to bot events"
and click on "Add Bot User Event" where you need to select "app_mention" and "message.im".

After that click on "Save Changes" in the bottom panel to save the changes.

![Example 8](https://i.imgur.com/Qvx3zDa.png)

Next, choose "App Home" category in sidebar.

![Example 9](https://i.imgur.com/MVwd4U8.png)

Next, in category "Show Tabs" we have to find
"Allow users to send Slash commands and messages from the messages tab" and select it.

![Example 10](https://i.imgur.com/jeF3jaJ.png)

Then in the sidebar we return to "Basic Information" category and in item
"Install your app, click on "Install to Workspace".

![Example 11](https://i.imgur.com/cIk2v9f.png)

Here we need to click "Allow" and our app will appear in the list of applications in our
Slack workspace.

![Example 12](https://i.imgur.com/qxcoMtI.png)

## Setting up the env file

Before running the bot, we need to configure the env file.

This is what the `.env` file looks like right now:
```yaml
#Keys
slack_bot_token=
slack_app_token=
openai_api_key=

# Open AI settings
ai_model=text-davinci-003
buffer_message_count=2

#Other
template_path=./template.txt
logfile_path=./logfile.txt
```

### slack_bot_token

In order to get a `slack_bot_token` you need to select the category
"Install App" category and copy our token. It starts as `xoxb-`.

![Example 13](https://i.imgur.com/NUdB9ZB.png)

### slack_app_token

To get `slack_app_token`, you need to go to "Basic Information" and under
"App-Level Tokens, click on the desired token and copy it.
It starts as `xapp-`.

![Example 6](https://i.imgur.com/7tRdg6U.png)

### openai_api_key

To get the `openai_api_key`, you need to have an account with ChatGPT. Go to the link:
https://platform.openai.com/account/api-keys and click on "Create new secret key".

![Example 14](https://i.imgur.com/evPI44W.png)

After that we will create a name for the key (optional) and generate the key:

![Example 15](https://i.imgur.com/LbdZjnb.png)

### ai_model

`ai_model` is a ChatGPT model type that will be used by our bot.
is set to `ChatGPT v3.5`.

### buffer_message_count

`buffer_message_count` - the number of messages that the bot leaves in the buffer. For example,
if set to `2`, the bot will remember the current message and 2 previous messages.

### template_path

The `template_path` is the path to the template that AI will use to better answer questions.
If there is no such txt file, you need to create and fill it with a template.
Here is an example you can use to make it work:

```text
Assistant is a large model trained by OpenAI.
Assistant should provide help for various tasks, from answering simple questions to providing detailed explanations and discussions with various topics. As a voice model, the Assistant can create human text based on the input it received, so that it has a natural dialogue and provides answers that are consistent with their respective themes.
Assistant has been learning and improved, and his skills are constantly developing. It can handle and understand a large number of texts, and can use these knowledge to provide accurate and rich answers to various questions. In addition, the Assistant can create his own text based on the entries he received, so that he can discuss and provide various theme explanations and descriptions.
In general, Assistant are a powerful tool that can help complete various tasks and provide valuable knowledge and information about various themes. Whether you need help on a specific issue or just want to talk to specific themes, Assistant can help here.
{history}
Human: {human_input}
Assistant:
```

### logfile_path

The `logfile_path` is the path to the logfile, which is used to log errors and warnings.

Проблема со скриншотом(-ами)? Весь список скриншотов можно найти [тут](https://imgur.com/a/f4VwPL3).