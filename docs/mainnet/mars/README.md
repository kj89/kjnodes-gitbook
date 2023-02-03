# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/mars.png" width="150" alt=""><figcaption></figcaption></figure>

Mars is a credit protocol for the future: non-custodial,  open-source, transparent, algorithmic and community-governed.

**Chain ID**: mars-1 | **Latest Version Tag**: v1.0.0 | **Wasm**: ON

[Website](https://marsprotocol.io) | [Discord](https://discord.gg/marsprotocol) | [Twitter](https://twitter.com/mars_protocol)




## Chain explorer
[https://explorer.kjnodes.com/mars](https://explorer.kjnodes.com/mars)

## Public endpoints

* api: [https://mars.api.kjnodes.com](https://mars.api.kjnodes.com)
* rpc: [https://mars.rpc.kjnodes.com](https://mars.rpc.kjnodes.com)
* grpc: [https://mars.grpc.kjnodes.com](https://mars.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@mars.rpc.kjnodes.com:45656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@mars.rpc.kjnodes.com:45659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/mars/addrbook.json > $HOME/.mars/config/addrbook.json
```

**live-peers** (10)
```bash
peers="ead869bce5e03c5512ceb99540e445e0bc639019@65.108.231.83:51656,5ffee90e41903f6fba29dc75446d536a02d626fe@65.108.232.150:18095,d10e5704f3c8e9dd6ef42445e4b88bb57d0a8289@65.108.8.247:18556,9cb92702727bc5f3d40154e625b9553a04f4d649@65.109.104.72:18556,f7126202172055ff4440e53c468146d3589c37ac@162.55.245.219:45656,1616af7456f519a0f2360adcad45d4bb9d39c92d@146.59.85.222:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:45656,e726816f42831689eab9378d5d577f1d06d25716@23.88.22.29:26656,eff52a6fcf2634ce1d60c1a5d38809718e22c5d2@23.88.69.22:28766,8253a88226cb44161f0f7eddb8aa0f022a0cf861@65.108.109.240:3000"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.mars/config/config.toml
```
