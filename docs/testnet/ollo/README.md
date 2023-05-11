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
peers="4b73754c2c10d523ffd43ca95d9cb6e0ad8204a4@5.189.148.147:26656,dba5e8b41c4e369418f83a449966e4eb7ca05cd4@65.109.23.114:18156,da8d3ca8e1c147f0037b1c43ad3de7174f5ec1b7@209.145.59.224:26656,15bcdea616c717eb4356e125d4f631aaa596dfd5@65.108.77.106:26929,595a8418f3f68a499a873148ec19a95b0f34390c@65.109.82.106:32656,d14b740968d24aa5c31ade7dbda2b1204c40f24c@65.109.52.156:46656,cadc2b601a188aedbe4156a6eb5a81e00770bcfc@65.108.219.110:26656,42beefd08b5f8580177d1506220db3a548090262@65.108.195.29:26116,dd577d8f2e997d7e70495640aff124ddb70d1a21@95.217.192.222:26656,7349272f712e713a957bf5349930e3439e98b518@167.235.27.69:20656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ollo/config/config.toml
```
