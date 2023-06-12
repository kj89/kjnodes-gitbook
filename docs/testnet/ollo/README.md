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
peers="032845b1a798108bfc1fd91ebe5bdbbccd4a34d8@135.181.221.186:32656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13256,70ba32724461c7ed4ec8d6ddc8b5e0b1cfb9e237@54.219.57.63:26656,125b0e30f00df3ff2ee7b29b7992ed888998ad31@65.109.28.177:47656,e53eedfc4c5c4487e1fba7f3b97de6aadfca8cea@5.161.179.64:26656,036d17d15c4e36cee8d93f9fb1a5ad5cb956631f@213.136.76.191:26656,dba5e8b41c4e369418f83a449966e4eb7ca05cd4@65.109.23.114:18156,2f5965450c9c831266959632fba2c1533b8f676d@38.242.248.2:26656,3ea40f63890f10272201edf96d2a49e197e52091@65.108.105.48:18156,da8d3ca8e1c147f0037b1c43ad3de7174f5ec1b7@209.145.59.224:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ollo/config/config.toml
```
