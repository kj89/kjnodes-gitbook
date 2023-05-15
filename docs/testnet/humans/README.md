# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/humans.png" alt=""><figcaption></figcaption></figure>

Humans is Blockchain of AIs. It is the first blockchain network  from the Cosmos ecosystem capable of managing, deploying and  executing artificial intelligence on the blockchain.

**Chain ID**: humans_3000-2 | **Latest Version Tag**: v0.2.1 | **Wasm**: OFF

[Website](https://humans.ai) | [Discord](https://discord.gg/humansdotai) | [Twitter](https://twitter.com/humansdotai)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/humans-testnet](https://explorer.kjnodes.com/humans-testnet)

## Public endpoints

* api: [https://humans-testnet.api.kjnodes.com](https://humans-testnet.api.kjnodes.com)
* rpc: [https://humans-testnet.rpc.kjnodes.com](https://humans-testnet.rpc.kjnodes.com)
* grpc: humans-testnet.grpc.kjnodes.com:12290

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@humans-testnet.rpc.kjnodes.com:12256
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@humans-testnet.rpc.kjnodes.com:12259
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/humans-testnet/addrbook.json > $HOME/.humansd/config/addrbook.json
```

**live-peers** (10)
```bash
peers="946b549550e9c564193bf4c963d84b17e5415a50@136.243.136.241:26656,b1f13e9971cfdcf784fb0efbd1b72417d5410a02@195.201.59.194:26656,de3cd5f6c726935c4c0fdb1e6bd5b705074c637c@144.76.45.59:26656,49f2ffa9786690548a1094b620d869ed72a33f8c@141.95.99.214:14356,19230fad7145e6fe80566a72f66b9ca3ec3f04d5@212.47.234.144:26656,35ad999115e2a58540f6cf3bc3b90cc3adc9debc@65.109.116.95:26656,be5158df5152ec7e6a4eca04c89e40494d19927c@51.79.101.159:26656,ef4cf8c00b34de7a8c1eba725ac91a93c085781c@38.146.3.210:18456,42f95015c31c7814b6a0a717fd8c63d15f896e88@94.237.27.19:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:12256"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.humansd/config/config.toml
```
