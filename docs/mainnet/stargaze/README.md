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

**live-peers** (11)
```bash
peers="0edce41e754e9bb9a228d4d2b0878713f6bd6de9@65.108.99.169:26656,7bca4f963ddc1d3863e0cc1815beab219e33302e@65.21.198.130:46656,e1b058e5cfa2b836ddaa496b10911da62dcf182e@23.88.21.235:26656,9125aeea6976e9550fd824a8ff517d1f0dca06d5@95.214.53.201:26656,ccb1f620a420bc4c2286ad816aca5c9656869430@45.34.1.114:36656,22a5266cb18ea209d3725e561bd9d2d27ee81d50@195.3.223.96:26656,0d9c5b7b4361cacb7ec5b08b818358f9cf23034b@65.108.66.92:26656,54d4bf577c2dce3a8137d8fe7820b46d199344e5@135.181.76.35:26656,8f3b17746be8f6faba3457c1e039e4a2fe3cb483@65.108.111.32:26656,56a776a589fbc4d038db956791bcf75204c67872@172.105.112.35:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:15856"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.starsd/config/config.toml
```
