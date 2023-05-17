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
peers="2b4f46e601fb4ede2a0c98976337e3afdaa50dac@65.108.238.102:15956,669470aba9778ccccd07127115dcdc30e141d7ae@65.108.232.248:33656,7c0f6f5c49d380f4b484e8da1ab51b3fd7befb76@163.172.135.245:26656,ab03f6d2d469e0be5b7fd5cb7388c7feffc1deac@15.235.114.194:10656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:11956,9a215b682a48dfc0435c590e945c9c2c07915ca8@65.21.170.3:26656,3bd3a20d7c8a26a20927289a7a6bffecf71de53e@51.81.155.97:10856,0e189bbc6db606a14950a0e59641b798a255c3c8@65.109.37.154:3000,719fec9bd14d52d5ea1048efa6d749e256811292@65.108.140.110:26656,ce3baba928ae06cd3ff0af20aec888a82ddffef7@54.37.129.171:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.teritorid/config/config.toml
```
