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
peers="84f821d36d45cc0cdaa4ff05297e888bb0d9de8f@85.237.193.111:26656,7f4be5f7db9b920e965197b65974f0e1e64749e4@144.126.128.128:26656,7bcc2e490b6aa2536d68de0881cba2ee7134840c@139.59.8.48:26130,e61f11c5b03400d3a99c066f951ed0888a2b64af@65.108.238.103:18556,89757803f40da51678451735445ad40d5b15e059@169.155.44.75:26656,d0dbb50a474888b8bed04bf8a23ac6b8bae443ee@5.79.79.80:18095,c124ce0b508e8b9ed1c5b6957f362225659b5343@169.155.45.189:26656,e1b058e5cfa2b836ddaa496b10911da62dcf182e@65.21.136.170:55656,8e64e7d8501db5d6bc4091292d8b35271accc2ba@195.3.220.22:26656,d2247f7b919f0781c90ee61958d7044665a22d38@169.155.168.110:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.mars/config/config.toml
```
