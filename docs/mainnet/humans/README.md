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
peers="f913050241ce5fd49ea3783ed21724ad05db7291@65.109.125.235:26656,025cdc1186815f3f28567b30a1667130f0f6c863@212.47.234.245:26656,974912ea6ac97594b51875985684533c21d879c2@185.252.232.85:26656,250d5926777e735519813157e444f84212fc8290@5.161.216.102:26656,a1ad90f3abf8e2875fb8c11f43498a7a8f63c9ad@139.59.6.61:26656,5e51671241340f1d1e1409a9e0cc4474820bf782@65.109.116.151:17656,abd78601b249e56a0d88d8ea361bae8e36cbf804@103.180.28.92:26656,d1a561f25837a6bbc930b0f40356c09a60de09fa@141.94.193.28:55686,f9344349e8435362bc7f21f67b9b61d2f1d6891b@152.32.174.173:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:12256"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.humansd/config/config.toml
```
