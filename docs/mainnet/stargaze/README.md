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
peers="0edce41e754e9bb9a228d4d2b0878713f6bd6de9@65.108.99.169:26656,fe6f8c74250b8235aa984f6c472993d85e16c163@144.76.94.124:26656,2dc5fefa675ef14718d6a0b9927f8b5955c94322@159.69.196.47:26629,0a935dd56157e719e704bc46633faf6ef0d52f11@51.159.109.243:21103,9125aeea6976e9550fd824a8ff517d1f0dca06d5@95.214.53.201:26656,ff10ddf3e5853586cfeab268cbab77ccbabf6927@188.166.148.13:26656,06805bbbb45dbbcdadb963fda7f5b3733f331ebe@185.119.118.109:3000,4da84cfcc0fcc8e144f9fdb4af4b175d8c6864a0@142.93.214.125:26656,2ec209c2dafbfc7a7f68e97d3bce4a91769162cc@168.119.77.200:26659,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:15856"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.starsd/config/config.toml
```
