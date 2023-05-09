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
peers="0198f6d3ebe7bed4d176558a2ce8d341531f3e7b@74.80.183.130:26653,463b1dc6903455575079572fb23407be586f2a4b@185.16.39.37:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:11656,b212d5740b2e11e54f56b072dc13b6134650cfb5@164.152.160.97:26656,ade7d4d0009c7725ee991b8c40a7f646f76bf1e3@149.102.140.108:26656,ea6a7b2f366bc343f0670f1673fd86001dd08eb0@65.108.122.246:26636,e9ad059b88d593682307587b5c04a16a43893c5e@65.21.205.225:4656,1ec2a654e00e22279ee50f13f074f2bce7218681@15.235.114.194:10156,ed857708c330334e1e62751470d6ecddf0397459@65.109.69.59:12256,d36ac7580cc8907a00b0add8c3b047caea6df4ed@107.155.67.202:26636"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.stride/config/config.toml
```
