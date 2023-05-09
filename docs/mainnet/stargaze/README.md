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
peers="b212d5740b2e11e54f56b072dc13b6134650cfb5@134.65.193.223:26656,c124ce0b508e8b9ed1c5b6957f362225659b5343@169.155.45.253:26656,bb5a32a9301b06cd4f30c0e45ca023213c95e9f6@213.133.111.71:36656,afbbff9114b9e542aea7d07523f5528fc8d05f9b@185.252.220.89:26004,ff10ddf3e5853586cfeab268cbab77ccbabf6927@188.166.148.13:26656,54d4bf577c2dce3a8137d8fe7820b46d199344e5@135.181.76.35:26656,998ec3a1b2ed38847ba03b6cfcd77eb51d3f8079@147.135.223.20:26656,e1b058e5cfa2b836ddaa496b10911da62dcf182e@23.88.21.235:26656,56a776a589fbc4d038db956791bcf75204c67872@172.105.112.35:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:15856"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.starsd/config/config.toml
```
