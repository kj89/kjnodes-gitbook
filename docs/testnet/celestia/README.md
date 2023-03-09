# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/celestia.png" width="150" alt=""><figcaption></figcaption></figure>

Celestia is a minimal blockchain that only orders and publishes transactions and  does not execute them. By decoupling the consensus and application execution layers,  Celestia modularizes the blockchain technology stack and unlocks new possibilities  for decentralized application builders.

**Chain ID**: mocha | **Latest Version Tag**: v0.11.0 | **Wasm**: OFF

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

**live-peers** (11)
```bash
peers="6a03b088a9e183e7faa897afcc6b50c6971a4cd5@159.69.5.164:26656,e8906342e657ace92e1ed8599f0949da8dd75fbd@146.19.24.52:20656,cb0db7a1fb8897c8eec9b09285e39d1756ed87b7@65.109.88.254:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:20656,2c93920515e53e0e08ca4bc86dd76a194ee34a29@89.117.59.233:26656,0d8b40858dcdf1e4370b2ed66b632bddf13a150d@75.119.143.147:26656,e286b562eddc6fea1b2635f6623430225666fb2f@147.135.144.58:26656,43e9da043318a4ea0141259c17fcb06ecff816af@141.94.73.39:43656,f98ee535cea1baf4a8fa438d1cd4e69ac836791f@65.21.234.47:26826,ca40b8ccd7c9d717ca691a74bec1e67aa9ae72c8@31.223.32.35:26656,3c3347474b104b38a16f98c4bc09665199bb6741@142.132.211.91:20656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.celestia-app/config/config.toml
```
