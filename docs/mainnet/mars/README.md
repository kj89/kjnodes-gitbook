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
peers="38edf28452ebc41f661d91b6613563c864f4c72e@35.228.114.46:26656,c0e6bf4193accabc14171ce163e704dcec5ea5df@51.91.215.170:36095,271593a440c65d6f224e852cb7ae65dd6863bc3a@74.50.94.66:56656,b88814bddfccd85289d7201bfd6fc6c4b3342ab2@178.162.165.193:36095,e1b058e5cfa2b836ddaa496b10911da62dcf182e@65.21.136.170:55656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.44.167:26656,d2247f7b919f0781c90ee61958d7044665a22d38@169.155.168.110:26656,d2a2c21754be65ad4a4f1de1f6163f681a6e8af8@192.99.44.79:18556,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:14556,6cceba286b498d4a1931f85e35ea0fa433373057@134.65.195.230:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.mars/config/config.toml
```
