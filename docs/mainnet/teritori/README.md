# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/teritori.png" alt=""><figcaption></figcaption></figure>

Teritori is a multi-chain hub designed to allow IBC and non IBC communities  to connect, trade services & NFTs, launch new projects & build further existing ones.

**Chain ID**: teritori-1 | **Latest Version Tag**: v1.4.0 | **Wasm**: ON

[Website](https://teritori.com) | [Discord](https://discord.gg/teritori) | [Twitter](https://twitter.com/TeritoriNetwork)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/teritori/torivaloper184ln03hkpt75uhrrr26f66kvcqvf4yn4nc2xjm)

Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals

## Restake

[Restake with kjnodes](https://restake.app/teritori/torivaloper184ln03hkpt75uhrrr26f66kvcqvf4yn4nc2xjm) (every 5 minutes)
## Chain explorer
[https://explorer.kjnodes.com/teritori](https://explorer.kjnodes.com/teritori)

## Public endpoints

* api: [https://teritori.api.kjnodes.com](https://teritori.api.kjnodes.com)
* rpc: [https://teritori.rpc.kjnodes.com](https://teritori.rpc.kjnodes.com)
* grpc: teritori.grpc.kjnodes.com:11990

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@teritori.rpc.kjnodes.com:11956
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@teritori.rpc.kjnodes.com:11959
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/teritori/addrbook.json > $HOME/.teritorid/config/addrbook.json
```

**live-peers** (10)
```bash
peers="0e189bbc6db606a14950a0e59641b798a255c3c8@65.109.37.154:3000,d2247f7b919f0781c90ee61958d7044665a22d38@169.155.44.201:26656,78815c81331c114cd508dae3a012f0d3e5e2b966@185.119.118.117:3000,ce3baba928ae06cd3ff0af20aec888a82ddffef7@54.37.129.171:26656,89757803f40da51678451735445ad40d5b15e059@134.65.192.221:26656,106490318e51355bc6d72e7941a0080f8b8256b9@185.16.39.14:26656,04fca92ca1dddd2f006bcb9fc2f6e6567c8c46c3@51.89.40.85:27656,e1b058e5cfa2b836ddaa496b10911da62dcf182e@138.201.8.248:26656,3bd3a20d7c8a26a20927289a7a6bffecf71de53e@51.81.155.97:10856,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:11956"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.teritorid/config/config.toml
```
