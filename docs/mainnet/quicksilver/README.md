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
peers="2020c09ef7542899a4c55b382013c469122186d6@51.195.88.136:15620,ae353518e6009eb48d80ccf6a006a9644e9dd309@146.19.24.101:26656,04dcb466b6804e6a57b7f9188b90f5bdc17037c0@108.165.178.242:26654,67c3cc1397d0a0f03a45d4cae6ff3380be7364f9@95.217.229.18:11656,5fa47201aa5208c30982b6f9d8ca44222d256fc5@51.91.70.90:48656,ffd3a67122d557dbc426972196ded625757b71b6@85.239.242.5:11656,ee14b4bbeb436056952c8e4e7c84826dfb92143b@65.109.105.17:26656,1b569bf57da79df4f85d207a161a97626988af76@65.109.92.241:20026,149a25417349d70f5e5127a5eb634dbfaf6e6c3a@142.165.207.19:56656,0de3ea135f09f6fcbe8ab75208ef9ca2e4b13d89@80.64.208.149:26656,ba52d6744d89cf66cf29d7663a21e1299d0f6744@74.80.183.130:26654,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:11156"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quicksilverd/config/config.toml
```
