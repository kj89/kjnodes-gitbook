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
peers="33f4d6b3a09e5ee651b49b2f6e0eb3294a3adb86@135.181.133.120:26656,5e51671241340f1d1e1409a9e0cc4474820bf782@65.109.116.151:17656,f913050241ce5fd49ea3783ed21724ad05db7291@65.109.125.235:26656,250d5926777e735519813157e444f84212fc8290@5.161.216.102:26656,aad2aadbe97cca1079d983f213ea90805e9fe765@162.55.145.72:26656,7fe9fed5e1e07692c332ea38ff4ef5ad2ee0248c@138.201.121.185:26690,2b882f794ed974031b5b435fbf1a755b668d7529@178.23.126.79:26656,dc4c999d252b1cf99a341b3e6e752bd173c0fabf@51.89.195.66:28656,93f4b883a14bac52c5a5436b0577d084ffc2c0f5@38.146.3.143:18456,32793227512886818e6c13a928ccfd675c0030c3@51.79.82.138:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:12256"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.humansd/config/config.toml
```
