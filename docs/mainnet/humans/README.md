# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/humans.png" alt=""><figcaption></figcaption></figure>

Humans is Blockchain of AIs. It is the first blockchain network  from the Cosmos ecosystem capable of managing, deploying and  executing artificial intelligence on the blockchain.

**Chain ID**: humans_1089-1 | **Latest Version Tag**: v1.0.0 | **Wasm**: OFF

[Website](https://humans.ai) | [Discord](https://discord.gg/humansdotai) | [Twitter](https://twitter.com/humansdotai)



Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/humans](https://explorer.kjnodes.com/humans)

## Public endpoints

* api: [https://humans.api.kjnodes.com](https://humans.api.kjnodes.com)
* rpc: [https://humans.rpc.kjnodes.com](https://humans.rpc.kjnodes.com)
* grpc: humans.grpc.kjnodes.com:12290

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@humans.rpc.kjnodes.com:12256
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@humans.rpc.kjnodes.com:12259
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/humans/addrbook.json > $HOME/.humansd/config/addrbook.json
```

**live-peers** (11)
```bash
peers="f9a289d71b2325ee87e9a358540e64fe97c3cf36@148.113.143.77:26656,7889ee17b291451155190d40426e6154be4e1abc@135.181.142.60:15608,5e51671241340f1d1e1409a9e0cc4474820bf782@65.109.116.151:17656,7fe9fed5e1e07692c332ea38ff4ef5ad2ee0248c@138.201.121.185:26690,aad2aadbe97cca1079d983f213ea90805e9fe765@162.55.145.72:26656,dc4c999d252b1cf99a341b3e6e752bd173c0fabf@51.89.195.66:28656,8204f0ddbb462749703a58ad6e4e57c5ea5a3379@193.34.212.99:26656,2b882f794ed974031b5b435fbf1a755b668d7529@178.23.126.79:26656,f913050241ce5fd49ea3783ed21724ad05db7291@65.109.125.235:26656,f9344349e8435362bc7f21f67b9b61d2f1d6891b@152.32.174.173:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:12256"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.humansd/config/config.toml
```
