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
peers="526d8c7c44f59be9a39d7463c576b68c0db23174@65.108.234.23:15956,4b04b3d164dc6dd5bb555a7a106a8d314f30516f@65.21.136.170:53656,82ebb17ddac20928fb8107201dad9f5aea7f9132@198.244.200.3:26656,ed090020aba4bb254ba1517644ab0d6c94c9461e@57.128.144.230:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@134.65.192.81:26656,45f2d4f8ed2ef8d71a257cdeed27123f5fe3bef4@141.94.109.71:10356,78815c81331c114cd508dae3a012f0d3e5e2b966@185.119.118.117:3000,3bd3a20d7c8a26a20927289a7a6bffecf71de53e@51.81.155.97:10856,5a98d637a16b16bf425a4a785c9d11a7d1e5b8a0@65.21.131.215:26736,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:11956"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.teritorid/config/config.toml
```
