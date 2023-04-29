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
peers="54d4bf577c2dce3a8137d8fe7820b46d199344e5@135.181.76.35:26656,7798342ae6f07e5c2e09bce8bab69e4485cacf64@5.9.72.212:3000,c5ca72ea2b6d098ccfa7fc8b9c994fe4db854e2f@162.55.5.230:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:58656,f5fa74f9a41b3d71f29a95cb1c90717e193a337d@23.111.163.2:26656,e726816f42831689eab9378d5d577f1d06d25716@23.88.22.11:26656,673ad0cb62287afcdbe5e5c88b91e39ee1bd394a@65.21.181.67:26656,c124ce0b508e8b9ed1c5b6957f362225659b5343@169.155.45.253:26656,6e5e6a674f41f7b1e6515ba735fbb836c0d89849@66.172.36.140:52656,6f8eddb672e93eb3362a7cb1c843a4e26af71ebc@149.202.72.186:26629"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.starsd/config/config.toml
```
