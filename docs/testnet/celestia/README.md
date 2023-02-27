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

**live-peers** (8)
```bash
peers="e8906342e657ace92e1ed8599f0949da8dd75fbd@146.19.24.52:20656,70a4fcccfc02c8fc0172dd97def0e9d597ffa343@38.242.128.250:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:20656,77fe717fc70370c5b1782c136a5bf7ef1e1e7b5d@167.235.233.34:26656,e286b562eddc6fea1b2635f6623430225666fb2f@147.135.144.58:26656,3584c49855123abdc16b01a47f9e1bea38a9db1b@154.26.155.102:26656,e6c28bd7cb4be3651942a9d93368651c97ee4733@65.108.65.36:20656,1f243a32a4c741e6838f247350f0aa7655ea264e@173.249.40.87:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.celestia-app/config/config.toml
```
