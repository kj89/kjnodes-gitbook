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

**live-peers** (29)
```bash
peers="72829b78b38408b03793ed389b9f16596b82c306@146.59.81.92:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:34656,ca5011c44fd74d95e7fca487c69e301df195750c@65.108.122.246:26726,e0ab6c5cc86959853f499236b8297344802ac5f4@5.161.139.201:26656,32bdba6ced12cdf2e534566e6c3d66ee2f7ef494@84.244.95.229:26656,1cce99042f884d669e7287e3e362bff8e385c63e@46.4.79.183:26726,b858ca4f3fed2c36b949cf67188b126e2542a39a@135.181.215.115:26726,1279eae188599463661c3e2b9ab492615a6d7079@65.108.235.32:2010,af58be7e0c9b36b506df93b3e1b34e5bd27fd9b8@65.109.43.75:27001,f05ddce65f1e75babe01d05fef1bce5d8ffe0972@54.177.181.170:26656,3c99aba53d77d9b86efb9a7a74037761360086e6@18.139.147.9:26656,36515aac2a928e227e7dc793a548b35b54bec974@45.63.82.80:26656,b6b9bc1a0c18d12be759111bb3a0d9a8958120c7@57.128.20.184:26656,0eeb20e044d632b279e67f2fe91f50e4fceab1fd@159.223.223.84:26656,c1e437f73b8889b78ea34981e7c349157ad80284@107.135.15.66:26656,6ecca845883e9273062ee515d2657080e6539d9e@65.109.32.148:26726,81062b9a8807a1229543b84bae2898c50a1b1dfc@52.211.169.132:26656,9d855646226f0f0737a3ce77db3ce950b92ce7cc@172.104.70.123:26656,3a436bbfdef463779c9593903063aa174879fa2e@54.159.132.131:26656,df1b21a6a92c6045946b2263ada344628ee9a8b6@74.118.143.189:26656,9edd51012df3a09395a48eb68a84723d6308e08c@35.212.116.100:26656,460967e46cc013e5e3eb365c1a8d271b0662549f@35.208.242.182:26656,3da88430414ec9084c8983fe4d462cce655ff1f3@51.222.245.114:26656,971ed177b284db42108187867cb8694df48ac742@95.217.205.41:26656,1da54d20c7339713f1d6d28dd2117087dd33d0ca@5.9.59.145:26656,25d3ec5a00235fe95d7a87bab54f03b6ac1962ba@34.78.95.235:26656,1be2bc01d01005833c538dedf11b23207cbb43f1@34.145.0.60:26656,281cc57298f0ff485f8ea2d6c24091273fcea4f3@65.108.234.159:26656,9e14c8c48776a789f7029e88c260b2a6cbbf1417@35.212.85.141:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gaia/config/config.toml
```
