import time
import requests
from datetime import timedelta
from datetime import datetime
from discord_webhook import DiscordWebhook, DiscordEmbed

contract = input('Input the contract for the collection: ')

headers = {
    "Accept": "application/json",
    "X-API-KEY": "284ac5f7b70846faa889f8af0bff60c8"
}

sale = False

while sale != True:
    dhook = DiscordWebhook('https://discord.com/api/webhooks/917167474615652373/sf9ENqdTNBIDAYuwO0lRQHYhIaxFVBTWBcHAog9KRs74TFZQI1_1zQMGLe7uootbPa2p')
    minago = int((datetime.now() - timedelta(minutes=770)).timestamp())

    url = "https://api.opensea.io/api/v1/events?asset_contract_address="+ contract + "&event_type=successful&only_opensea=false&offset=0&limit=9&occurred_after=" + str(minago)
    result = requests.request("GET", url, headers=headers)

    if result:
        for value in result.json()['asset_events']:
            if value['asset']:
                embed = DiscordEmbed(title=value['asset']['asset_contract']['name'] + ' #' + value['asset']['token_id'] + ' was purchased for ' + str(int(value['total_price']) * (10 ** -18)) + ' ETH', color = '00FF00')
                embed.set_author(name='View on Opensea', url='https://opensea.io/assets/' + contract +'/'+ value['asset']['token_id'])
                embed.set_image(url=value['asset']['image_original_url'])
                embed.add_embed_field(name='Seller', value=value['seller']['user']['username'])
                embed.add_embed_field(name='Buyer', value=value['winner_account']['user']['username'])
                embed.set_timestamp()
                dhook.add_embed(embed)
            else:
                print('Not an asset')
    response = dhook.execute()

    time.sleep(59)   