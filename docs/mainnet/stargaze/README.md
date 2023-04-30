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
peers="8f3b17746be8f6faba3457c1e039e4a2fe3cb483@65.108.111.32:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:58656,bb5a32a9301b06cd4f30c0e45ca023213c95e9f6@213.133.111.71:36656,afbbff9114b9e542aea7d07523f5528fc8d05f9b@185.252.220.89:26004,9125aeea6976e9550fd824a8ff517d1f0dca06d5@95.214.53.201:26656,2344a4bc1d8c78ddf078e3d7c596d8bdda6cd4d6@139.144.77.69:26656,62378c0bfc79666d6f7fb17be2af6a4889e775e8@65.108.46.248:36656,6e5e6a674f41f7b1e6515ba735fbb836c0d89849@66.172.36.140:52656,e726816f42831689eab9378d5d577f1d06d25716@23.88.22.11:26656,dc3037694a6bb18c1d570bb4c6278323a9286de8@5.9.48.85:36656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.starsd/config/config.toml
```
