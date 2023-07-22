from discord_webhooks import DiscordWebhooks

webhook_url = ''

def send_msg(ssh, vnc):

    WEBHOOK_URL = webhook_url 

    #message = ssh + "\n" + vnc

    webhook = DiscordWebhooks(WEBHOOK_URL)
    webhook.set_footer(text='-- thesynthax')

    webhook.set_content(title='Raspberry Pi Online', description="Here are the port numbers.")

    webhook.add_field(name='SSH: ', value=ssh)
    webhook.add_field(name='VNC: ', value=vnc)

    webhook.send()

    print("Sent message to discord")
