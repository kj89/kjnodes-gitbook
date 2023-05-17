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
peers="8cfd25b39a24cdf72b8ff9f9516d8c27365c640f@51.158.156.89:36656,afbbff9114b9e542aea7d07523f5528fc8d05f9b@185.252.220.89:26004,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:15856,0edce41e754e9bb9a228d4d2b0878713f6bd6de9@65.108.99.169:26656,6f8eddb672e93eb3362a7cb1c843a4e26af71ebc@149.202.72.186:26629,fc668bbf7e34d6926308487348b2655159198f1d@135.181.128.114:13756,06887c80bf8150af6331a993411a701d6c76c769@194.195.118.177:26656,22a5266cb18ea209d3725e561bd9d2d27ee81d50@195.3.223.96:26656,4da84cfcc0fcc8e144f9fdb4af4b175d8c6864a0@142.93.214.125:26656,f57f1869d29b43b56c9af36807948797842b5a03@15.235.114.53:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.starsd/config/config.toml
```
