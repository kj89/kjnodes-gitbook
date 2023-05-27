# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/stargaze.png" alt=""><figcaption></figcaption></figure>

Stargaze is a Cosmos zone (layer 1 proof-of-stake blockchain).  It is the base layer node software for the Stargaze NFT Marketplace.

**Chain ID**: stargaze-1 | **Latest Version Tag**: v9.0.0 | **Wasm**: ON

[Website](https://www.stargaze.zone) | [Discord](https://discord.gg/stargaze) | [Twitter](https://twitter.com/stargazezone)



Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/stargaze](https://explorer.kjnodes.com/stargaze)

## Public endpoints

* api: [https://stargaze.api.kjnodes.com](https://stargaze.api.kjnodes.com)
* rpc: [https://stargaze.rpc.kjnodes.com](https://stargaze.rpc.kjnodes.com)
* grpc: stargaze.grpc.kjnodes.com:15890

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@stargaze.rpc.kjnodes.com:15856
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@stargaze.rpc.kjnodes.com:15859
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/stargaze/addrbook.json > $HOME/.starsd/config/addrbook.json
```

**live-peers** (10)
```bash
peers="fee838fe0381b3f74538a36d643991ceca3793c8@65.108.141.109:8656,e726816f42831689eab9378d5d577f1d06d25716@23.88.22.11:26656,8cfd25b39a24cdf72b8ff9f9516d8c27365c640f@51.158.156.89:36656,4eeadb9b2af44a34252c8ba236a29fa4eb6931ab@141.95.155.224:10156,778e22fa6e604e9fdd410c2ef9598254eb34f46a@198.244.176.186:46656,7d3b175e9c23bb80de6c0542e30eb40a678b711d@136.243.95.80:36656,0edce41e754e9bb9a228d4d2b0878713f6bd6de9@65.108.99.169:26656,f57f1869d29b43b56c9af36807948797842b5a03@15.235.114.53:26656,82d89abe4024c54b68b8d07887cbb7f3d0710f71@130.61.146.203:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:15856"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.starsd/config/config.toml
```
