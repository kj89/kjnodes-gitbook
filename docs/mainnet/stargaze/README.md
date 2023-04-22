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
peers="1e1237931e262cd7a00803dfa1ce51b7a36eb1fa@194.163.150.135:26656,22a5266cb18ea209d3725e561bd9d2d27ee81d50@195.3.223.96:26656,6f8eddb672e93eb3362a7cb1c843a4e26af71ebc@149.202.72.186:26629,b1ddf96ff6db5cfe77fa9c88dc2925f4525d0a02@141.94.141.144:56656,c75c47ffc1a32b6320b6c7e5252ee9361e69ce92@15.235.51.191:10156,f5fa74f9a41b3d71f29a95cb1c90717e193a337d@23.111.163.2:26656,8833968b0e6696a075774f2dbe874f6872ac4cc6@57.128.75.17:25050,85591aa9be728b7f705382794a5c1d73dae8f2ae@141.94.196.138:26656,0a935dd56157e719e704bc46633faf6ef0d52f11@51.159.109.243:21103,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:58656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.starsd/config/config.toml
```
