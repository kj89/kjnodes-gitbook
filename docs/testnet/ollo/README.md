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
peers="0bee9e500e51465917506b47691a8fb032100da9@94.130.200.168:32656,3ea40f63890f10272201edf96d2a49e197e52091@65.108.105.48:18156,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13256,42beefd08b5f8580177d1506220db3a548090262@65.108.195.29:26116,c2bc7720a610d753b037d89e6c3f58f7c718e24f@116.202.117.229:32656,95ca646da3736cef5d6c6704f736bc49ff87ef6c@109.123.249.213:26656,9865c6e15faced6643adc228e3a59744e1b4e277@116.203.29.162:46656,cadc2b601a188aedbe4156a6eb5a81e00770bcfc@65.108.219.110:26656,dba5e8b41c4e369418f83a449966e4eb7ca05cd4@65.109.23.114:18156,b5f55cfc7b4d19f2dd3cdc71795f5a81e2c67f96@38.242.232.72:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ollo/config/config.toml
```
