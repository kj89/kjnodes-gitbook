# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/stargaze.png" width="150" alt=""><figcaption></figcaption></figure>

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
peers="ecd1947cddb25e84d800b4e9967dc98a3f05a38a@95.216.191.134:26656,b1ddf96ff6db5cfe77fa9c88dc2925f4525d0a02@141.94.141.144:56656,a67a6e354a0a910149bdb13c985ca5ac16a333cd@217.160.249.168:26656,ce764e158a4a29a4af7606c38c44e976c69b3982@144.91.78.94:26656,7798342ae6f07e5c2e09bce8bab69e4485cacf64@5.9.72.212:3000,7d3b175e9c23bb80de6c0542e30eb40a678b711d@136.243.95.80:36656,b212d5740b2e11e54f56b072dc13b6134650cfb5@134.65.193.223:26656,0075beaca29af670b9ebe4acf74386d59ff5c365@77.68.90.48:26656,0a935dd56157e719e704bc46633faf6ef0d52f11@51.159.109.243:21103,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:58656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.starsd/config/config.toml
```
