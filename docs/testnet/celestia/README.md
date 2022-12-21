# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/celestia.png" width="150" alt=""><figcaption></figcaption></figure>

Celestia is a minimal blockchain that only orders and publishes transactions and  does not execute them. By decoupling the consensus and application execution layers,  Celestia modularizes the blockchain technology stack and unlocks new possibilities  for decentralized application builders.

**Chain ID**: mocha | **Latest Version Tag**: v0.11.0 | **Wasm**: OFF

[Website](https://celestia.org) | [Discord](https://discord.gg/celestiacommunity) | [Twitter](https://twitter.com/CelestiaOrg)


## Public endpoints

* rpc: [https://celestia-testnet.rpc.kjnodes.com](https://celestia-testnet.rpc.kjnodes.com)
* api: [https://celestia-testnet.api.kjnodes.com](https://celestia-testnet.api.kjnodes.com)

## Peering

**state-sync**

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@celestia-testnet.rpc.kjnodes.com:20656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@celestia-testnet.rpc.kjnodes.com:20659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/celestia-testnet/addrbook.json > $HOME/.celestia-app/config/addrbook.json
```

**live-peers** (8)
```
peers="8262231964896250acd4e8171663f59bd53d7a91@5.161.80.30:20656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:20656,3ccaca3a32779bcf4c5cc85aae66a46902f0b641@95.216.223.149:26656,f98ee535cea1baf4a8fa438d1cd4e69ac836791f@65.21.234.47:26826,e286b562eddc6fea1b2635f6623430225666fb2f@147.135.144.58:26656,002fc3b88ec74753e2539bf30828e7f8bd19cc65@35.220.185.86:26656,78091973241d5638259f518f3b19f6320b7fb451@135.181.119.59:20656,6a03b088a9e183e7faa897afcc6b50c6971a4cd5@159.69.5.164:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.celestia-app/config/config.toml
```
