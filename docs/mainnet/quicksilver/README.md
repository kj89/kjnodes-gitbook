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
peers="6053a39e67c6bae83430e354f53d99e160e4964b@65.109.28.177:28656,f73b2b887e7d1c01a3d753db359a0058e634e767@65.108.201.154:2090,71b753819eb653e99e6a825b80af20ca9bccb087@135.125.163.63:24666,b4bcce87121963e1e97619dc135f2eb1a9fd5dfc@88.198.32.17:36656,1b569bf57da79df4f85d207a161a97626988af76@65.109.92.241:20026,81547bb30946c359cfe72b441b0594547545cf8c@38.242.253.58:27656,ffd3a67122d557dbc426972196ded625757b71b6@85.239.242.5:11656,161f453c9ff27f3120ec5078f56b505316fbc720@65.108.6.45:61156,e1a24aaba30a8ff21e52fed92b96b36156b52e80@51.161.208.88:26656,0a226e70ceb7a4123e66216d1ed83ef22ed8a187@185.119.118.118:2000,04dcb466b6804e6a57b7f9188b90f5bdc17037c0@108.165.178.242:26654,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:11156"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quicksilverd/config/config.toml
```
