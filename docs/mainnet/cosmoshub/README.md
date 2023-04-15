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
peers="81062b9a8807a1229543b84bae2898c50a1b1dfc@52.211.169.132:26656,d9dbd30f7e9ae99dc05645f48f4637c2f4a14645@34.107.9.71:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:34656,32bdba6ced12cdf2e534566e6c3d66ee2f7ef494@84.244.95.229:26656,b6b9bc1a0c18d12be759111bb3a0d9a8958120c7@57.128.20.184:26656,b14e5b9a4b53a3e0115ce525dfd5bf59cdf2a634@34.82.190.80:26656,e0ab6c5cc86959853f499236b8297344802ac5f4@5.161.139.201:26656,ee767901f4a7eaf44603ef0a5b6e5edac118ba1e@74.118.136.149:26656,36515aac2a928e227e7dc793a548b35b54bec974@45.63.82.80:26656,ca5011c44fd74d95e7fca487c69e301df195750c@65.108.122.246:26726,6ecca845883e9273062ee515d2657080e6539d9e@65.109.32.148:26726,460967e46cc013e5e3eb365c1a8d271b0662549f@35.208.242.182:26656,c14d39422b5d70d9084d19d286c7427c0762cdfc@162.55.92.114:2010,3da88430414ec9084c8983fe4d462cce655ff1f3@51.222.245.114:26656,fe21dd474640247888fc7c4dce82da8da08a8bfd@135.181.113.227:26656,0eeb20e044d632b279e67f2fe91f50e4fceab1fd@159.223.223.84:26656,9edd51012df3a09395a48eb68a84723d6308e08c@35.212.116.100:26656,b858ca4f3fed2c36b949cf67188b126e2542a39a@135.181.215.115:26726,1da54d20c7339713f1d6d28dd2117087dd33d0ca@5.9.59.145:26656,971ed177b284db42108187867cb8694df48ac742@95.217.205.41:26656,1279eae188599463661c3e2b9ab492615a6d7079@65.108.235.32:2010,1cce99042f884d669e7287e3e362bff8e385c63e@46.4.79.183:26726,1733aef88702bd8326bea0e1dc403d3dbb6f5d8a@158.247.202.33:26656,db7850e8e9bef0568904b7d5bcaec813e8e3d295@34.27.227.166:26656,9c116194f25fd0d146019f171ef0f49904dcc586@167.86.98.230:26656,87ccc1dcc0b846fc1623ab9a5ab55682e8e2ad2e@47.147.226.228:26656,4c46d32cbc4777c59a91a53fdadf8a3fa362036e@116.202.10.68:26656,1997e68bf205bedeed0c4723786bf03464987dc1@77.87.108.21:26656,daa6d8314246ad65037a48ec2e2266eeea9d46f8@154.53.63.50:26656,9d7d9ba2b9bc1c805a24413fcfdc75010d52dd61@159.89.101.239:26090"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gaia/config/config.toml
```
