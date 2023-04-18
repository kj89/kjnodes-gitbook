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
peers="c124ce0b508e8b9ed1c5b6957f362225659b5343@169.155.44.11:26656,e726816f42831689eab9378d5d577f1d06d25716@23.88.22.1:26656,9edd51012df3a09395a48eb68a84723d6308e08c@35.212.116.100:26656,32bdba6ced12cdf2e534566e6c3d66ee2f7ef494@84.244.95.229:26656,1cce99042f884d669e7287e3e362bff8e385c63e@46.4.79.183:26726,6ecca845883e9273062ee515d2657080e6539d9e@65.109.32.148:26726,b6b9bc1a0c18d12be759111bb3a0d9a8958120c7@57.128.20.184:26656,0eeb20e044d632b279e67f2fe91f50e4fceab1fd@159.223.223.84:26656,36515aac2a928e227e7dc793a548b35b54bec974@45.63.82.80:26656,ca5011c44fd74d95e7fca487c69e301df195750c@65.108.122.246:26726,6681cee74de13aaac561442bcbc420bdb025aacc@116.202.85.179:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:34656,1279eae188599463661c3e2b9ab492615a6d7079@65.108.235.32:2010,f05ddce65f1e75babe01d05fef1bce5d8ffe0972@54.177.181.170:26656,1da54d20c7339713f1d6d28dd2117087dd33d0ca@5.9.59.145:26656,e829d4764a5cecc44b3414777853b34407b36601@185.16.39.179:26656,9e14c8c48776a789f7029e88c260b2a6cbbf1417@35.212.85.141:26656,b858ca4f3fed2c36b949cf67188b126e2542a39a@135.181.215.115:26726,2286eeee09fcf37e768dfffc0db8c821b9231b7b@204.16.244.78:26656,2532ad5b2f93fd521e97dbc3562db711df4bd763@65.109.88.70:26656,971ed177b284db42108187867cb8694df48ac742@95.217.205.41:26656,e3f76b923d03fc99510b31049144e22d8f0f0587@65.108.193.249:2010,5acfd758ce66cdb9764728fbe29a826241e07203@35.209.182.93:26656,3da88430414ec9084c8983fe4d462cce655ff1f3@51.222.245.114:26656,27ad834c62dbefc5beb74be7575515927bd07c58@193.176.85.151:26656,0393c19b176d1cf8bc560c5a8fa990301deb1a7e@135.181.188.17:26656,fe21dd474640247888fc7c4dce82da8da08a8bfd@135.181.113.227:26656,58f1815e3bd03bd93586f1e0287556c035d5ad14@142.132.146.164:15603,1997e68bf205bedeed0c4723786bf03464987dc1@77.87.108.21:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gaia/config/config.toml
```
