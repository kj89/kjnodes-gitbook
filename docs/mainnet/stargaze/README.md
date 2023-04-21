# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/stargaze.png" width="150" alt=""><figcaption></figcaption></figure>

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
peers="06805bbbb45dbbcdadb963fda7f5b3733f331ebe@185.119.118.109:3000,22a5266cb18ea209d3725e561bd9d2d27ee81d50@195.3.223.96:26656,fe6f8c74250b8235aa984f6c472993d85e16c163@144.76.94.124:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:58656,54d4bf577c2dce3a8137d8fe7820b46d199344e5@135.181.76.35:26656,f5fa74f9a41b3d71f29a95cb1c90717e193a337d@23.111.163.2:26656,85591aa9be728b7f705382794a5c1d73dae8f2ae@141.94.196.138:26656,d3393f1ddc2b2f1ad4e91d86b429576ab1ed241f@195.154.99.18:28454,b212d5740b2e11e54f56b072dc13b6134650cfb5@134.65.193.223:26656,531a3c9fddf61af2b684b140ba954dab55db739f@198.244.165.175:12656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.starsd/config/config.toml
```
