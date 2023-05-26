# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/stride.png" alt=""><figcaption></figcaption></figure>

Stride is a blockchain ("zone") that provides liquidity for staked assets.  Using Stride, you can earn both staking and DeFi yields across the Cosmos IBC ecosystem

**Chain ID**: stride-1 | **Latest Version Tag**: v9.0.1 | **Wasm**: OFF

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
peers="b212d5740b2e11e54f56b072dc13b6134650cfb5@164.152.160.97:26656,166da4de977381ea8853986be11dbb470d9dc2ba@149.202.72.186:26639,e8be5c472174a97a3d3076bd33be75f5fde92a5b@151.106.40.38:29656,ade7d4d0009c7725ee991b8c40a7f646f76bf1e3@149.102.140.108:26656,ea6a7b2f366bc343f0670f1673fd86001dd08eb0@65.108.122.246:26636,d36ac7580cc8907a00b0add8c3b047caea6df4ed@107.155.67.202:26636,222b5f1f8f8b4933c1913818ab2b7379c282b4e2@65.108.75.107:11656,20f56a68a04eedc764b7e1b87b7032a50b9d4fe9@51.81.155.97:10456,c948379b649bc6609557dd74f5a4e70716f100ea@51.210.240.201:10456,89757803f40da51678451735445ad40d5b15e059@169.155.168.67:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.stride/config/config.toml
```
