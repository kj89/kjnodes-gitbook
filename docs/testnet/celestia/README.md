# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/celestia.png" width="150" alt=""><figcaption></figcaption></figure>

Celestia is a minimal blockchain that only orders and publishes transactions and  does not execute them. By decoupling the consensus and application execution layers,  Celestia modularizes the blockchain technology stack and unlocks new possibilities  for decentralized application builders.

**Chain ID**: blockspacerace-0 | **Latest Version Tag**: v0.12.0 | **Wasm**: OFF

[Website](https://celestia.org) | [Discord](https://discord.gg/celestiacommunity) | [Twitter](https://twitter.com/CelestiaOrg)




## Chain explorer
[https://explorer.kjnodes.com/celestia-testnet](https://explorer.kjnodes.com/celestia-testnet)

## Public endpoints

* api: [https://celestia-testnet.api.kjnodes.com](https://celestia-testnet.api.kjnodes.com)
* rpc: [https://celestia-testnet.rpc.kjnodes.com](https://celestia-testnet.rpc.kjnodes.com)
* grpc: [https://celestia-testnet.grpc.kjnodes.com](https://celestia-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@celestia-testnet.rpc.kjnodes.com:20656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@celestia-testnet.rpc.kjnodes.com:20659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/celestia-testnet/addrbook.json > $HOME/.celestia-app/config/addrbook.json
```

**live-peers** (10)
```bash
peers="cb0db7a1fb8897c8eec9b09285e39d1756ed87b7@65.109.88.254:26656,e286b562eddc6fea1b2635f6623430225666fb2f@147.135.144.58:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:20656,3ccaca3a32779bcf4c5cc85aae66a46902f0b641@95.216.223.149:26656,0d8b40858dcdf1e4370b2ed66b632bddf13a150d@75.119.143.147:26656,e6c28bd7cb4be3651942a9d93368651c97ee4733@65.108.65.36:20656,43e9da043318a4ea0141259c17fcb06ecff816af@141.94.73.39:43656,2c93920515e53e0e08ca4bc86dd76a194ee34a29@89.117.59.233:26656,ca40b8ccd7c9d717ca691a74bec1e67aa9ae72c8@31.223.32.35:26656,e8906342e657ace92e1ed8599f0949da8dd75fbd@146.19.24.52:20656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.celestia-app/config/config.toml
```
