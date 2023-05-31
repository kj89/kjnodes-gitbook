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
peers="be546a9a1b8b664a32ad5f45fa1d4087b44e0f83@135.181.214.120:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:11656,69fc32ac94aa1ccbac270fa58370459e647c251f@5.9.66.9:26656,aa0d47509ecadb630189fe4ef071d438a6493e69@178.162.165.194:24095,e4ef38aea46aed22c4241f691104e164df6fc15a@65.109.33.48:15656,d056dcd5ac8dddb23e2962a5ade6ee51f9bfd785@162.19.89.8:10456,e41dd510feb9e14df82ce0f4eab258fad78645ea@158.247.218.149:10002,8324d459d12f468199f6d1ec45b18ade35af18b8@5.78.104.216:26656,2f6a21a94be87df4c2a2d82683e6ea99b7b6b02b@50.21.173.78:26656,1ec2a654e00e22279ee50f13f074f2bce7218681@15.235.114.194:10156"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.stride/config/config.toml
```
