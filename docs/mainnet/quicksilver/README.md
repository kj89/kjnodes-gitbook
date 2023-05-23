# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/quicksilver.png" alt=""><figcaption></figcaption></figure>

Quicksilver is a permissionless, sovereign Cosmos SDK zone providing liquid staking for the entire Cosmos Ecosystem.

**Chain ID**: quicksilver-2 | **Latest Version Tag**: v1.2.11 | **Wasm**: OFF

[Website](https://quicksilver.zone) | [Discord](https://discord.gg/quicksilverprotocol) | [Twitter](https://twitter.com/quicksilverzone)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/quicksilver/quickvaloper1fqfgpwdngmmay6ah7mg9y4k7ayykpzu6l3ht2m)

Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals

## Restake

[Restake with kjnodes](https://restake.app/quicksilver/quickvaloper1fqfgpwdngmmay6ah7mg9y4k7ayykpzu6l3ht2m) (every 5 minutes)
## Chain explorer
[https://explorer.kjnodes.com/quicksilver](https://explorer.kjnodes.com/quicksilver)

## Public endpoints

* api: [https://quicksilver.api.kjnodes.com](https://quicksilver.api.kjnodes.com)
* rpc: [https://quicksilver.rpc.kjnodes.com](https://quicksilver.rpc.kjnodes.com)
* grpc: quicksilver.grpc.kjnodes.com:11190

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@quicksilver.rpc.kjnodes.com:11156
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@quicksilver.rpc.kjnodes.com:11159
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/quicksilver/addrbook.json > $HOME/.quicksilverd/config/addrbook.json
```

**live-peers** (12)
```bash
peers="3308d9078fcca016fbd8dc8f3b19666326f41a6f@138.201.121.185:26672,ae353518e6009eb48d80ccf6a006a9644e9dd309@146.19.24.101:26656,a87f48e433160970318d181bb69c378f4564cd2d@107.155.67.202:26736,ffd3a67122d557dbc426972196ded625757b71b6@85.239.242.5:11656,04dcb466b6804e6a57b7f9188b90f5bdc17037c0@108.165.178.242:26654,a1f5e0b68f36091d5fc8f30aba914b6c191f21fa@65.108.128.201:11156,26d23125db7493486dc9931b4181425d725e4ac6@65.109.55.186:20656,71d1e3336f41475c3dfc247aa77a8842a24c369a@144.91.80.32:11656,d5a9c9ae08f0d30e36c8f64eca046fc52b00561e@65.109.92.160:26656,833a368b9e639d50dcbeaa2e8347306979d55e50@199.217.117.78:11156,71b753819eb653e99e6a825b80af20ca9bccb087@135.125.163.63:24666,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:11156"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quicksilverd/config/config.toml
```
