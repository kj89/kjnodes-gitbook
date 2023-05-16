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
peers="7bca4f963ddc1d3863e0cc1815beab219e33302e@65.21.198.130:46656,c124ce0b508e8b9ed1c5b6957f362225659b5343@169.155.45.253:26656,8833968b0e6696a075774f2dbe874f6872ac4cc6@57.128.75.17:25050,b1ddf96ff6db5cfe77fa9c88dc2925f4525d0a02@141.94.141.144:56656,6c7a904400f646e43eaf1ea76976de037392efa1@23.88.69.22:26566,7ff48cc8533f31c1c14a687a0a193164dbefec38@194.163.171.38:26656,0a935dd56157e719e704bc46633faf6ef0d52f11@51.159.109.243:21103,f5fa74f9a41b3d71f29a95cb1c90717e193a337d@23.111.163.2:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:15856,7798342ae6f07e5c2e09bce8bab69e4485cacf64@5.9.72.212:3000"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.starsd/config/config.toml
```
