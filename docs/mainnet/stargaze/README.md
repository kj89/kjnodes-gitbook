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
peers="fc668bbf7e34d6926308487348b2655159198f1d@135.181.128.114:13756,7798342ae6f07e5c2e09bce8bab69e4485cacf64@5.9.72.212:3000,e1b058e5cfa2b836ddaa496b10911da62dcf182e@23.88.21.235:26656,0a935dd56157e719e704bc46633faf6ef0d52f11@51.159.109.243:21103,15bf6fc85e4e37b2c96e35c7b76816670ad63c18@65.108.75.107:8656,06805bbbb45dbbcdadb963fda7f5b3733f331ebe@185.119.118.109:3000,bae0d94b8f0f3dc8ea167a764e119c01dc2456f0@66.206.6.58:26656,02826a9d7da27fbaf869544a108218859106c7b1@65.108.77.98:26656,7bca4f963ddc1d3863e0cc1815beab219e33302e@65.21.198.130:46656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:15856"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.starsd/config/config.toml
```
