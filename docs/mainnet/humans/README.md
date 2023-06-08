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

**live-peers** (10)
```bash
peers="524d635a8b60111ba5e44ca9bea4948d84b5a937@65.109.154.185:30656,20f95f8b8dd32b94b593dc3e8fcf0b0aeb74b85d@94.237.93.65:26656,d70c9343af28023a78aceb653e885666c12fec3b@138.201.121.185:26687,00d69cc662fc7135064769666b5d1a0df2b2bf31@3.77.65.248:26656,974912ea6ac97594b51875985684533c21d879c2@185.252.232.85:26656,d1a561f25837a6bbc930b0f40356c09a60de09fa@141.94.193.28:55686,025cdc1186815f3f28567b30a1667130f0f6c863@212.47.234.245:26656,250d5926777e735519813157e444f84212fc8290@5.161.216.102:26656,abd78601b249e56a0d88d8ea361bae8e36cbf804@103.180.28.92:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:12256"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.humansd/config/config.toml
```
