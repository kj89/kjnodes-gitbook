# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/stride.png" alt=""><figcaption></figcaption></figure>

Stride is a blockchain ("zone") that provides liquidity for staked assets.  Using Stride, you can earn both staking and DeFi yields across the Cosmos IBC ecosystem

**Chain ID**: stride-1 | **Latest Version Tag**: v9.0.0 | **Wasm**: OFF

[Website](https://stride.zone) | [Discord](https://discord.gg/mzQZ8dAE7u) | [Twitter](https://twitter.com/stride_zone)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/stride/stridevaloper1j8gkhtllnp252l6g6zwzea30e7pvzqttr9768n)

Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals

## Restake

[Restake with kjnodes](https://restake.app/stride/stridevaloper1j8gkhtllnp252l6g6zwzea30e7pvzqttr9768n) (every 5 minutes)
## Chain explorer
[https://explorer.kjnodes.com/stride](https://explorer.kjnodes.com/stride)

## Public endpoints

* api: [https://stride.api.kjnodes.com](https://stride.api.kjnodes.com)
* rpc: [https://stride.rpc.kjnodes.com](https://stride.rpc.kjnodes.com)
* grpc: stride.grpc.kjnodes.com:11690

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@stride.rpc.kjnodes.com:11656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@stride.rpc.kjnodes.com:11659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/stride/addrbook.json > $HOME/.stride/config/addrbook.json
```

**live-peers** (10)
```bash
peers="ea6a7b2f366bc343f0670f1673fd86001dd08eb0@65.108.122.246:26636,be546a9a1b8b664a32ad5f45fa1d4087b44e0f83@135.181.214.120:26656,c948379b649bc6609557dd74f5a4e70716f100ea@51.210.240.201:10456,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:11656,b212d5740b2e11e54f56b072dc13b6134650cfb5@164.152.160.97:26656,df3f533e6b9776c11f08da804edcb810cbdd2080@65.108.234.23:12256,166da4de977381ea8853986be11dbb470d9dc2ba@149.202.72.186:26639,d041196a1a36091605448fc65181408ccc1d5da1@65.109.122.105:26656,87a7a8cc67967d0ede5d68a1477c44a40a8705f7@108.165.178.242:26653,bf0f5782650ddbf8121543b94705e5849f87120a@130.211.230.106:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.stride/config/config.toml
```
