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
peers="44deaab1264724b6e98ee3882dc2fe19defe033c@135.181.156.110:26656,5e51671241340f1d1e1409a9e0cc4474820bf782@65.109.116.151:17656,b05e9018dbe13d5706a6eba13050890865dbe1c2@135.181.208.166:28656,7889ee17b291451155190d40426e6154be4e1abc@135.181.142.60:15608,9193e655f0581b4acf2e87976ac0b55795359742@167.235.177.226:26656,a1ad90f3abf8e2875fb8c11f43498a7a8f63c9ad@139.59.6.61:26656,abd78601b249e56a0d88d8ea361bae8e36cbf804@103.180.28.92:26656,f9344349e8435362bc7f21f67b9b61d2f1d6891b@152.32.174.173:26656,93f4b883a14bac52c5a5436b0577d084ffc2c0f5@38.146.3.143:18456,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:12256"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.humansd/config/config.toml
```
