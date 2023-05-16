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
peers="0edce41e754e9bb9a228d4d2b0878713f6bd6de9@65.108.99.169:26656,fe6f8c74250b8235aa984f6c472993d85e16c163@144.76.94.124:26656,bb5a32a9301b06cd4f30c0e45ca023213c95e9f6@213.133.111.71:36656,4eeadb9b2af44a34252c8ba236a29fa4eb6931ab@141.95.155.224:10156,6f8eddb672e93eb3362a7cb1c843a4e26af71ebc@149.202.72.186:26629,e726816f42831689eab9378d5d577f1d06d25716@23.88.22.11:26656,afbbff9114b9e542aea7d07523f5528fc8d05f9b@185.252.220.89:26004,82d89abe4024c54b68b8d07887cbb7f3d0710f71@130.61.146.203:26656,62378c0bfc79666d6f7fb17be2af6a4889e775e8@65.108.46.248:36656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:15856"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.starsd/config/config.toml
```
