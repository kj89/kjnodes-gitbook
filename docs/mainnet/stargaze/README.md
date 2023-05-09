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
peers="2344a4bc1d8c78ddf078e3d7c596d8bdda6cd4d6@139.144.77.69:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:15856,fe6f8c74250b8235aa984f6c472993d85e16c163@144.76.94.124:26656,d9307d7d7e219461ab9c333104780181b6933e74@89.58.50.116:26656,e726816f42831689eab9378d5d577f1d06d25716@23.88.22.11:26656,06805bbbb45dbbcdadb963fda7f5b3733f331ebe@185.119.118.109:3000,22a5266cb18ea209d3725e561bd9d2d27ee81d50@195.3.223.96:26656,54d4bf577c2dce3a8137d8fe7820b46d199344e5@135.181.76.35:26656,ebc272824924ea1a27ea3183dd0b9ba713494f83@195.3.220.136:26986,15bf6fc85e4e37b2c96e35c7b76816670ad63c18@65.108.75.107:8656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.starsd/config/config.toml
```
