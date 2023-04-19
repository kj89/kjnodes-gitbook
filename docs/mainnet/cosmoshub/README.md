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
peers="4ebf074e8b4a24438bd0bd503b62b4728dfb8eae@35.212.101.35:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:34656,32bdba6ced12cdf2e534566e6c3d66ee2f7ef494@84.244.95.229:26656,5b143d463427d9ad0b621f97c0b8933643e293da@35.212.90.144:26656,5b4529df65f9c1006d51472a827f1deb23825ba2@91.194.30.204:14656,b6b9bc1a0c18d12be759111bb3a0d9a8958120c7@57.128.20.184:26656,6681cee74de13aaac561442bcbc420bdb025aacc@116.202.85.179:26656,1279eae188599463661c3e2b9ab492615a6d7079@65.108.235.32:2010,0eeb20e044d632b279e67f2fe91f50e4fceab1fd@159.223.223.84:26656,e3f76b923d03fc99510b31049144e22d8f0f0587@65.108.193.249:2010,b858ca4f3fed2c36b949cf67188b126e2542a39a@135.181.215.115:26726,971ed177b284db42108187867cb8694df48ac742@95.217.205.41:26656,36515aac2a928e227e7dc793a548b35b54bec974@45.63.82.80:26656,e726816f42831689eab9378d5d577f1d06d25716@23.88.22.1:26656,daa6d8314246ad65037a48ec2e2266eeea9d46f8@154.53.63.50:26656,6ecca845883e9273062ee515d2657080e6539d9e@65.109.32.148:26726,1da54d20c7339713f1d6d28dd2117087dd33d0ca@5.9.59.145:26656,9e14c8c48776a789f7029e88c260b2a6cbbf1417@35.212.85.141:26656,3334bb086be9ab0dba3a34331555624a7354a6ab@159.203.187.36:26090,dea13e7232642331360d4387b0ab106b014092d4@116.202.236.59:26656,f05ddce65f1e75babe01d05fef1bce5d8ffe0972@54.177.181.170:26656,25d3ec5a00235fe95d7a87bab54f03b6ac1962ba@34.78.95.235:26656,1cce99042f884d669e7287e3e362bff8e385c63e@46.4.79.183:26726,ca5011c44fd74d95e7fca487c69e301df195750c@65.108.122.246:26726,c03593feca52899e9cc38ae0fed671fb96ab0bba@3.217.133.209:26656,c1e437f73b8889b78ea34981e7c349157ad80284@107.135.15.66:26656,fe21dd474640247888fc7c4dce82da8da08a8bfd@135.181.113.227:26656,460967e46cc013e5e3eb365c1a8d271b0662549f@35.208.242.182:26656,9edd51012df3a09395a48eb68a84723d6308e08c@35.212.116.100:26656,1997e68bf205bedeed0c4723786bf03464987dc1@77.87.108.21:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gaia/config/config.toml
```
