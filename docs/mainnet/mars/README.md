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
peers="be494851610016cff8853796a99c3ad46d8d1b5b@65.108.76.242:36095,c06b9689397667fa060d8c3458dd391962d89be2@116.202.36.240:18556,7a9560de3e7df9d4e193d512b3a9e23e13f18e4a@141.95.154.21:26656,b88814bddfccd85289d7201bfd6fc6c4b3342ab2@178.162.165.193:36095,d2a2c21754be65ad4a4f1de1f6163f681a6e8af8@192.99.44.79:18556,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:45656,b6939330a08264dd09d531f1695e7114e0e7076c@65.108.126.35:33656,530b1964bc17bca6457311f1c2d5a2f3d25b297a@51.81.155.97:18556,4db44ebd58fed67d2a22ce06a395ce489415f498@5.75.197.137:26650,d10e5704f3c8e9dd6ef42445e4b88bb57d0a8289@65.108.8.247:18556"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.mars/config/config.toml
```
