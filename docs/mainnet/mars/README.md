# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/mars.png" width="150" alt=""><figcaption></figcaption></figure>

Mars is a credit protocol for the future: non-custodial,  open-source, transparent, algorithmic and community-governed.

**Chain ID**: mars-1 | **Latest Version Tag**: v1.0.0 | **Wasm**: ON

[Website](https://marsprotocol.io) | [Discord](https://discord.gg/marsprotocol) | [Twitter](https://twitter.com/mars_protocol)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/mars/marsvaloper1p9t4gr40rnpdwqacxgcqp7ffrfw908nu020g4n)

## Restake

[Restake with kjnodes](https://restake.app/mars/marsvaloper1p9t4gr40rnpdwqacxgcqp7ffrfw908nu020g4n) (every 5 minutes)
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
peers="d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:45656,59bb909c57664fafe88bf1b6924769c15a769ba4@65.108.125.236:3000,5ffee90e41903f6fba29dc75446d536a02d626fe@65.108.232.150:18095,8253a88226cb44161f0f7eddb8aa0f022a0cf861@65.108.109.240:3000,6cbdee8a3fd9dc83b8296275c96e5372dbc3b143@148.113.159.123:26656,e726816f42831689eab9378d5d577f1d06d25716@23.88.22.29:26656,76969af1bccdd4dcc511741b171c3d4ccb837ba6@146.59.85.223:18556,e1b058e5cfa2b836ddaa496b10911da62dcf182e@65.21.136.170:55656,230c8b615ab3d0a92c88c765cded171338199edd@51.210.240.201:18556,d0dbb50a474888b8bed04bf8a23ac6b8bae443ee@5.79.79.80:18095"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.mars/config/config.toml
```
