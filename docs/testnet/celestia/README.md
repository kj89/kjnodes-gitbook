# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/celestia.png" width="150" alt=""><figcaption></figcaption></figure>

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

**live-peers** (9)
```bash
peers="38553b85b8740315da067fdd28a195c45df9069b@148.251.11.99:20656,78091973241d5638259f518f3b19f6320b7fb451@135.181.119.59:20656,e286b562eddc6fea1b2635f6623430225666fb2f@147.135.144.58:26656,77fe717fc70370c5b1782c136a5bf7ef1e1e7b5d@167.235.233.34:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:20656,0d8b40858dcdf1e4370b2ed66b632bddf13a150d@75.119.143.147:26656,cb0db7a1fb8897c8eec9b09285e39d1756ed87b7@65.109.88.254:26656,43e9da043318a4ea0141259c17fcb06ecff816af@141.94.73.39:43656,70a4fcccfc02c8fc0172dd97def0e9d597ffa343@38.242.128.250:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.celestia-app/config/config.toml
```
