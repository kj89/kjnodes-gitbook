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
peers="dba5e8b41c4e369418f83a449966e4eb7ca05cd4@65.109.23.114:18156,dd577d8f2e997d7e70495640aff124ddb70d1a21@95.217.192.222:26656,e53eedfc4c5c4487e1fba7f3b97de6aadfca8cea@5.161.179.64:26656,0bee9e500e51465917506b47691a8fb032100da9@94.130.200.168:32656,0f99f7481a1b49701866ddbdfe71dc3b2fd792d8@109.123.244.56:26626,771cfca799033e327511b25ae77784e02818d77f@65.108.101.4:23486,47655c33bdecae7f449301197d8b951a97e1b680@89.58.59.75:26656,b5f55cfc7b4d19f2dd3cdc71795f5a81e2c67f96@38.242.232.72:26656,3ea40f63890f10272201edf96d2a49e197e52091@65.108.105.48:18156,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13256"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ollo/config/config.toml
```
