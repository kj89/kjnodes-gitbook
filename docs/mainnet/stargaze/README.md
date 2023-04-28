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
* grpc: stargaze.grpc.kjnodes.com:58090

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@stargaze.rpc.kjnodes.com:58656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@stargaze.rpc.kjnodes.com:58659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/stargaze/addrbook.json > $HOME/.starsd/config/addrbook.json
```

**live-peers** (10)
```bash
peers="4da84cfcc0fcc8e144f9fdb4af4b175d8c6864a0@142.93.214.125:26656,b1ddf96ff6db5cfe77fa9c88dc2925f4525d0a02@141.94.141.144:56656,6f8eddb672e93eb3362a7cb1c843a4e26af71ebc@149.202.72.186:26629,22a5266cb18ea209d3725e561bd9d2d27ee81d50@195.3.223.96:26656,9125aeea6976e9550fd824a8ff517d1f0dca06d5@95.214.53.201:26656,8cfd25b39a24cdf72b8ff9f9516d8c27365c640f@51.158.156.89:36656,eee6cb357d3248ea8c6138fea2d8004963d32743@65.108.138.80:13756,dc3037694a6bb18c1d570bb4c6278323a9286de8@5.9.48.85:36656,6e5e6a674f41f7b1e6515ba735fbb836c0d89849@66.172.36.140:52656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:58656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.starsd/config/config.toml
```
