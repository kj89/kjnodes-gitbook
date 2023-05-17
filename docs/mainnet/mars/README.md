# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/mars.png" alt=""><figcaption></figcaption></figure>

Mars is a credit protocol for the future: non-custodial,  open-source, transparent, algorithmic and community-governed.

**Chain ID**: mars-1 | **Latest Version Tag**: v1.0.0 | **Wasm**: ON

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

**live-peers** (11)
```bash
peers="be494851610016cff8853796a99c3ad46d8d1b5b@65.108.76.242:36095,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.44.167:26656,d0dbb50a474888b8bed04bf8a23ac6b8bae443ee@5.79.79.80:18095,83199a9711e20f811add4a0cb6029856e25ebb7a@207.188.7.221:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:14556,931f46cc338f59222c22565e216a16f57bbb9782@95.217.164.44:26656,5ffee90e41903f6fba29dc75446d536a02d626fe@65.108.232.150:18095,d933a425e567c28b4695acbbf0d6cfa6c68cf0c5@65.108.72.156:26656,918041a30cfbf00e3bcff76faaceb3ccc3fe5032@162.19.89.8:18556,f6eddb5f6ef49a1a2007e586da4755b2b2081b3d@51.89.6.150:20656,695add58c0b9379f42b326977ffc4bc6d7fe2100@116.202.229.240:36656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.mars/config/config.toml
```
