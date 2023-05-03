# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/ollo.png" alt=""><figcaption></figcaption></figure>

OLLO is a sovereign L1 chain built on the Cosmos network providing  next-gen trading tools & sustainable tokenomics.

**Chain ID**: ollo-testnet-1 | **Latest Version Tag**: v0.0.1 | **Wasm**: OFF

[Website](https://www.ollostation.zone) | [Discord](https://discord.com/invite/GxBqZ9mSSm) | [Twitter](https://twitter.com/OLLOStation)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/ollo-testnet](https://explorer.kjnodes.com/ollo-testnet)

## Public endpoints

* api: [https://ollo-testnet.api.kjnodes.com](https://ollo-testnet.api.kjnodes.com)
* rpc: [https://ollo-testnet.rpc.kjnodes.com](https://ollo-testnet.rpc.kjnodes.com)
* grpc: ollo-testnet.grpc.kjnodes.com:13290

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@ollo-testnet.rpc.kjnodes.com:13256
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@ollo-testnet.rpc.kjnodes.com:13259
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/ollo-testnet/addrbook.json > $HOME/.ollo/config/addrbook.json
```

**live-peers** (10)
```bash
peers="cadc2b601a188aedbe4156a6eb5a81e00770bcfc@65.108.219.110:26656,dd577d8f2e997d7e70495640aff124ddb70d1a21@95.217.192.222:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13256,9865c6e15faced6643adc228e3a59744e1b4e277@116.203.29.162:46656,69d2c02f413bea1376f5398646f0c2ce0f82d62e@141.94.73.93:26656,e2d59891f1aed38fe8884c63e0bb00f8ddc41b6f@5.78.46.66:26656,036d17d15c4e36cee8d93f9fb1a5ad5cb956631f@213.136.76.191:26656,1e5d9db4138ed31ecf81b09365230d33360f8cde@65.109.81.119:32656,125b0e30f00df3ff2ee7b29b7992ed888998ad31@65.109.28.177:47656,dba5e8b41c4e369418f83a449966e4eb7ca05cd4@65.109.23.114:18156"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ollo/config/config.toml
```
