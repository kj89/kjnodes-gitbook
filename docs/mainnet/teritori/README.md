# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/teritori.png" alt=""><figcaption></figcaption></figure>

Teritori is a multi-chain hub designed to allow IBC and non IBC communities  to connect, trade services & NFTs, launch new projects & build further existing ones.

**Chain ID**: teritori-1 | **Latest Version Tag**: v1.3.1 | **Wasm**: ON

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
peers="c670830fdf60374f008fa4a4eb851deddcdaef5b@65.109.88.107:46656,e1b058e5cfa2b836ddaa496b10911da62dcf182e@138.201.8.248:26656,45f2d4f8ed2ef8d71a257cdeed27123f5fe3bef4@141.94.109.71:10356,ed090020aba4bb254ba1517644ab0d6c94c9461e@57.128.144.230:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:11956,89757803f40da51678451735445ad40d5b15e059@134.65.192.221:26656,6046cec27c36f0a7596cb9fa9f2c5decbd4e87cb@151.115.53.172:26656,3bd3a20d7c8a26a20927289a7a6bffecf71de53e@51.81.155.97:10856,d40face481bc00a617d9a29c39be412a776e28c2@116.202.36.240:10656,5fb621ecd0f48889939c663a2d0796403d5a2552@65.109.104.118:61156"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.teritorid/config/config.toml
```
