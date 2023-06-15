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
peers="b05e9018dbe13d5706a6eba13050890865dbe1c2@135.181.208.166:28656,5889ea00677d3ffa998a18c59f99a23632190c8d@65.109.95.26:33656,974912ea6ac97594b51875985684533c21d879c2@185.252.232.85:26656,93f4b883a14bac52c5a5436b0577d084ffc2c0f5@38.146.3.143:18456,d70c9343af28023a78aceb653e885666c12fec3b@138.201.121.185:26687,abd78601b249e56a0d88d8ea361bae8e36cbf804@103.180.28.92:26656,44deaab1264724b6e98ee3882dc2fe19defe033c@135.181.156.110:26656,9193e655f0581b4acf2e87976ac0b55795359742@167.235.177.226:26656,9a4c00c2d3bb30204561dbe7d6cb7d1a7ff9880b@65.108.213.235:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:12256"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.humansd/config/config.toml
```
