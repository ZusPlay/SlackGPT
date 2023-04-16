def convert_slack_id_to_username(slack_id: str):
    return f'<@{slack_id}>'


def convert_output_to_message(text: str, username: str):
    output = text.strip()
    output = output[:1].lower() + output[1:]
    return f'{username}, {output}'
