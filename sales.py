#NFT Sales Bot by Shrikanth Srenivasan Class of 2025
import time
import requests
from datetime import timedelta
from datetime import datetime
from discord_webhook import DiscordWebhook, DiscordEmbed

contract = input('Input the contract for the collection: ')
#identify the NFT collection using the smart contract address

headers = {
    "Accept": "application/json",
    "X-API-KEY": "284ac5f7b70846faa889f8af0bff60c8" #Opensea Api Key (Not Ratelimited)
}

sale = False

#Forever loop that iterates every 60 seconds. (Monitors for a sale every 60 seconds)
while sale != True: 
    dhook = DiscordWebhook('https://discord.com/api/webhooks/917167474615652373/sf9ENqdTNBIDAYuwO0lRQHYhIaxFVBTWBcHAog9KRs74TFZQI1_1zQMGLe7uootbPa2p')
    #Discord webhook to send the embed.
    minago = int((datetime.now() - timedelta(minutes=10)).timestamp())
    #Finds the timestamp of a minute before current time

    url = "https://api.opensea.io/api/v1/events?asset_contract_address="+ contract + "&event_type=successful&only_opensea=false&offset=0&limit=9&occurred_after=" + str(minago)
    result = requests.request("GET", url, headers=headers)
    #requests for all sales after one minute

    if result:
        for value in result.json()['asset_events']:
            if value['asset']:
                embed = DiscordEmbed(title=value['asset']['asset_contract']['name'] + ' #' + value['asset']['token_id'] + ' was purchased for ' + str(int(value['total_price']) * (10 ** -18)) + ' ETH', color = '00FF00')
                #Posts the name of the collection and the value it was purchased for
                embed.set_author(name='View on Opensea', url='https://opensea.io/assets/' + contract +'/'+ value['asset']['token_id'])
                #Links to the NFT on Opensea
                embed.set_image(url=value['asset']['image_original_url'])
                #Posts an image of the NFT
                embed.add_embed_field(name='Seller', value=value['seller']['user']['username'])
                #Posts the username of the seller
                embed.add_embed_field(name='Buyer', value=value['winner_account']['user']['username'])
                #Posts the username of the buyer
                embed.set_timestamp()
                dhook.add_embed(embed)
            else:
                print('Not an asset')
    response = dhook.execute() #Posts the webhook
    print("Monitoring")
    time.sleep(60) #Stops running the code for 60 seconds (makes the while loop loop every 60 sec)
    