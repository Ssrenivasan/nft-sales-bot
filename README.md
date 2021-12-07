# nft-sales-bot

NFT Sales Bot by Shrikanth Srenivasan (Class of 2025)

Video presentation : https://youtu.be/qQtbNx4CDnQ

This bot uses python requests and discord webhooks to display info. User has to input the contract address for the NFT collection they want to monitor. The bot will send a GET request to Opensea using their API to get all sales for that collection after 1 minute ago. The GET request is in a while loop that loops every 60 seconds. Discord webhook posts the name and token id of the nft along with the price in ETH that the NFT was purchases for. If the buyer and seller have Opensea usernames, then the webhook will display that too.


During this project I had to learn python requests and also about Opensea and NFTs. It was pretty fun to learn and felt really good when it started worked. I encountered a lot of problems with using the request to get the recent sales and routing to the name and price. I had to calculate how to convert wei to eth and that conversion was online.

If you want to test out the script:
1. Change the discord webhook
2. Input a collection address with good activity

