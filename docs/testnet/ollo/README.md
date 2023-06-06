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
peers="0f99f7481a1b49701866ddbdfe71dc3b2fd792d8@109.123.244.56:26626,2f5965450c9c831266959632fba2c1533b8f676d@38.242.248.2:26656,cadc2b601a188aedbe4156a6eb5a81e00770bcfc@65.108.219.110:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13256,d14b740968d24aa5c31ade7dbda2b1204c40f24c@65.109.52.156:46656,c2bc7720a610d753b037d89e6c3f58f7c718e24f@116.202.117.229:32656,036d17d15c4e36cee8d93f9fb1a5ad5cb956631f@213.136.76.191:26656,e53eedfc4c5c4487e1fba7f3b97de6aadfca8cea@5.161.179.64:26656,799dff05af5d30477f44c816753ff89104b2b8b5@116.202.227.117:32656,125b0e30f00df3ff2ee7b29b7992ed888998ad31@65.109.28.177:47656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ollo/config/config.toml
```
