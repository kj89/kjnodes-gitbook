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

**live-peers** (10)
```bash
peers="f6eddb5f6ef49a1a2007e586da4755b2b2081b3d@51.89.6.150:20656,931f46cc338f59222c22565e216a16f57bbb9782@95.217.164.44:26656,e1b058e5cfa2b836ddaa496b10911da62dcf182e@65.21.136.170:55656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.44.167:26656,be7d56127ef887d095b2f55f09be5fee1969d922@146.59.52.48:18095,89757803f40da51678451735445ad40d5b15e059@169.155.44.75:26656,471518432477e31ea348af246c0b54095d41352c@169.155.47.57:26656,d8e92c3ca2daddef493d518b4e850af26ec4027b@199.85.208.186:26656,d2247f7b919f0781c90ee61958d7044665a22d38@169.155.168.110:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:14556"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.mars/config/config.toml
```
