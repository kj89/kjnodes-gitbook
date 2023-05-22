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

**live-peers** (9)
```bash
peers="cd0e1ec85c6d9ab8304cbb387d531aaedc1efab1@211.219.19.72:26656,fe6f8c74250b8235aa984f6c472993d85e16c163@144.76.94.124:26656,e726816f42831689eab9378d5d577f1d06d25716@23.88.22.11:26656,56a776a589fbc4d038db956791bcf75204c67872@172.105.112.35:26656,06805bbbb45dbbcdadb963fda7f5b3733f331ebe@185.119.118.109:3000,54d4bf577c2dce3a8137d8fe7820b46d199344e5@135.181.76.35:26656,673ad0cb62287afcdbe5e5c88b91e39ee1bd394a@65.21.181.67:26656,0a935dd56157e719e704bc46633faf6ef0d52f11@51.159.109.243:21103,0be77d7bf88c00ad0622df5f36ade9b4a96449cc@15.235.10.84:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.starsd/config/config.toml
```
