# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/mars.png" alt=""><figcaption></figcaption></figure>

Mars is a credit protocol for the future: non-custodial,  open-source, transparent, algorithmic and community-governed.

**Chain ID**: mars-1 | **Latest Version Tag**: v1.0.1 | **Wasm**: ON

[Website](https://marsprotocol.io) | [Discord](https://discord.gg/marsprotocol) | [Twitter](https://twitter.com/mars_protocol)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/mars/marsvaloper1p9t4gr40rnpdwqacxgcqp7ffrfw908nu020g4n)

Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals

## Restake

[Restake with kjnodes](https://restake.app/mars/marsvaloper1p9t4gr40rnpdwqacxgcqp7ffrfw908nu020g4n) (every 5 minutes)
## Chain explorer
[https://explorer.kjnodes.com/mars](https://explorer.kjnodes.com/mars)

## Public endpoints

* api: [https://mars.api.kjnodes.com](https://mars.api.kjnodes.com)
* rpc: [https://mars.rpc.kjnodes.com](https://mars.rpc.kjnodes.com)
* grpc: mars.grpc.kjnodes.com:14590

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@mars.rpc.kjnodes.com:14556
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@mars.rpc.kjnodes.com:14559
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/mars/addrbook.json > $HOME/.mars/config/addrbook.json
```

**live-peers** (10)
```bash
peers="c06b9689397667fa060d8c3458dd391962d89be2@116.202.36.240:18556,be7d56127ef887d095b2f55f09be5fee1969d922@146.59.52.48:18095,4784e37f8df4c4271c92088ffc1df7908bd5126b@162.19.95.239:18556,5ffee90e41903f6fba29dc75446d536a02d626fe@65.108.232.150:18095,c124ce0b508e8b9ed1c5b6957f362225659b5343@169.155.45.189:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:14556,7a9560de3e7df9d4e193d512b3a9e23e13f18e4a@141.95.154.21:26656,f68d6eb7cddd667f0341c573a6d17f0d2253ca9d@136.243.67.44:18556,895e35334a32207ddba612cbfd5d177cee23ef88@155.133.22.9:24656,530b1964bc17bca6457311f1c2d5a2f3d25b297a@51.81.155.97:18556"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.mars/config/config.toml
```
