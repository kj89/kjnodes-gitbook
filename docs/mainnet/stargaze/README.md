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
peers="6f8eddb672e93eb3362a7cb1c843a4e26af71ebc@149.202.72.186:26629,ce764e158a4a29a4af7606c38c44e976c69b3982@144.91.78.94:26656,22a5266cb18ea209d3725e561bd9d2d27ee81d50@195.3.223.96:26656,ff10ddf3e5853586cfeab268cbab77ccbabf6927@188.166.148.13:26656,ccb1f620a420bc4c2286ad816aca5c9656869430@45.34.1.114:36656,0a935dd56157e719e704bc46633faf6ef0d52f11@51.159.109.243:21103,cd0e1ec85c6d9ab8304cbb387d531aaedc1efab1@211.219.19.72:26656,85591aa9be728b7f705382794a5c1d73dae8f2ae@141.94.196.138:26656,778e22fa6e604e9fdd410c2ef9598254eb34f46a@198.244.176.186:46656,6e5e6a674f41f7b1e6515ba735fbb836c0d89849@66.172.36.140:52656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:15856"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.starsd/config/config.toml
```
