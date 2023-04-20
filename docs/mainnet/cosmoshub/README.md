# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/cosmoshub.png" width="150" alt=""><figcaption></figcaption></figure>

The Cosmos Hub is the blockchain protocol underlying an  increasingly large number of blockchains built on the  Cosmos Network, allowing them to communicate with each other.

**Chain ID**: cosmoshub-4 | **Latest Version Tag**: v9.0.0 | **Wasm**: OFF

[Website](https://hub.cosmos.network) | [Discord](https://discord.gg/cosmosnetwork) | [Twitter](https://twitter.com/cosmoshub)



Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/cosmoshub](https://explorer.kjnodes.com/cosmoshub)

## Public endpoints

* api: [https://cosmoshub.api.kjnodes.com](https://cosmoshub.api.kjnodes.com)
* rpc: [https://cosmoshub.rpc.kjnodes.com](https://cosmoshub.rpc.kjnodes.com)
* grpc: cosmoshub.grpc.kjnodes.com:34090

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@cosmoshub.rpc.kjnodes.com:34656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@cosmoshub.rpc.kjnodes.com:34659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/cosmoshub/addrbook.json > $HOME/.gaia/config/addrbook.json
```

**live-peers** (30)
```bash
peers="8698cb819c9a4503fe2c71055f1380d08edc5adf@204.16.244.116:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:34656,dea13e7232642331360d4387b0ab106b014092d4@116.202.236.59:26656,32bdba6ced12cdf2e534566e6c3d66ee2f7ef494@84.244.95.229:26656,1cce99042f884d669e7287e3e362bff8e385c63e@46.4.79.183:26726,b6b9bc1a0c18d12be759111bb3a0d9a8958120c7@57.128.20.184:26656,1279eae188599463661c3e2b9ab492615a6d7079@65.108.235.32:2010,0eeb20e044d632b279e67f2fe91f50e4fceab1fd@159.223.223.84:26656,1997e68bf205bedeed0c4723786bf03464987dc1@77.87.108.21:26656,67685d93f2256caa7a2d53e3a104f9e437c3d247@95.216.114.244:26656,f05ddce65f1e75babe01d05fef1bce5d8ffe0972@54.177.181.170:26656,b858ca4f3fed2c36b949cf67188b126e2542a39a@135.181.215.115:26726,1da54d20c7339713f1d6d28dd2117087dd33d0ca@5.9.59.145:26656,f6f5d71d0b9e29f2b86f47ce0d62b059b53009fc@74.118.143.238:26656,6ecca845883e9273062ee515d2657080e6539d9e@65.109.32.148:26726,ca5011c44fd74d95e7fca487c69e301df195750c@65.108.122.246:26726,460967e46cc013e5e3eb365c1a8d271b0662549f@35.208.242.182:26656,61afb0f37c02031f285f6b27ead2a3e7a97cc28a@35.212.34.104:26656,2286eeee09fcf37e768dfffc0db8c821b9231b7b@204.16.244.78:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.169.37:26656,e0ab6c5cc86959853f499236b8297344802ac5f4@5.161.139.201:26656,2532ad5b2f93fd521e97dbc3562db711df4bd763@65.109.88.70:26656,b79e1d3a621bdafd3a8d9a49dff8f4737d0bedc9@52.203.105.100:26656,fe21dd474640247888fc7c4dce82da8da08a8bfd@135.181.113.227:26656,9c116194f25fd0d146019f171ef0f49904dcc586@167.86.98.230:26656,daa6d8314246ad65037a48ec2e2266eeea9d46f8@154.53.63.50:26656,ee767901f4a7eaf44603ef0a5b6e5edac118ba1e@74.118.136.149:26656,9edd51012df3a09395a48eb68a84723d6308e08c@35.212.116.100:26656,9df3cb21ee4aeb3463a1014a345554bd88485811@3.231.68.59:26656,cd372322e563832871672be23d8303508d4385a3@139.59.8.48:26090"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gaia/config/config.toml
```
