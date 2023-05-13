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
peers="1c3e1cafb4d3e9edeb37fc964e98ed1ae8bda6ee@144.76.223.202:26656,22a5266cb18ea209d3725e561bd9d2d27ee81d50@195.3.223.96:26656,2344a4bc1d8c78ddf078e3d7c596d8bdda6cd4d6@139.144.77.69:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:15856,c124ce0b508e8b9ed1c5b6957f362225659b5343@169.155.45.253:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@134.65.193.223:26656,15bf6fc85e4e37b2c96e35c7b76816670ad63c18@65.108.75.107:8656,d3393f1ddc2b2f1ad4e91d86b429576ab1ed241f@195.154.99.18:28454,4da84cfcc0fcc8e144f9fdb4af4b175d8c6864a0@142.93.214.125:26656,fee838fe0381b3f74538a36d643991ceca3793c8@65.108.141.109:8656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.starsd/config/config.toml
```
