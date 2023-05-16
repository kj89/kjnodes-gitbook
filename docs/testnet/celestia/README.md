# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/celestia.png" alt=""><figcaption></figcaption></figure>

Celestia is a minimal blockchain that only orders and publishes transactions and  does not execute them. By decoupling the consensus and application execution layers,  Celestia modularizes the blockchain technology stack and unlocks new possibilities  for decentralized application builders.

**Chain ID**: blockspacerace-0 | **Latest Version Tag**: v0.13.0 | **Wasm**: OFF

[Website](https://celestia.org) | [Discord](https://discord.gg/celestiacommunity) | [Twitter](https://twitter.com/CelestiaOrg)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/celestia-testnet](https://explorer.kjnodes.com/celestia-testnet)

## Public endpoints

* api: [https://celestia-testnet.api.kjnodes.com](https://celestia-testnet.api.kjnodes.com)
* rpc: [https://celestia-testnet.rpc.kjnodes.com](https://celestia-testnet.rpc.kjnodes.com)
* grpc: celestia-testnet.grpc.kjnodes.com:12090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@celestia-testnet.rpc.kjnodes.com:12056
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@celestia-testnet.rpc.kjnodes.com:12059
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/celestia-testnet/addrbook.json > $HOME/.celestia-app/config/addrbook.json
```

**live-peers** (11)
```bash
peers="c054b3a758977691e284b04240efecfb5a56986b@195.201.197.4:20656,e4fa11cfb413d69d95dc90a0e12125b091b1d574@51.158.115.159:26656,193acd7bf7049b425d7b95c24e02250fce8ad45c@65.109.92.79:11656,0096a95343de3097594ebebc66542ed4a4167f2a@65.109.159.227:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:12056,de36dc2bc32ecaacafb213d173f6218f93ebb306@144.76.105.14:26656,6c73374cb78a543e2dd3eb218c29386392da2cf5@35.210.99.77:26656,7d6d1d1c3498687d4705fe4c7216623797835fae@74.118.136.164:26656,b9a59a4e1e521ff3bf651c20a17bbad61fdd443d@104.128.62.172:26656,8f14ec71e1d712c912c27485a169c2519628cfb6@185.225.232.196:21656,af66f28f19f747bd2b5a18d91d143dc8e035f86a@47.147.226.228:52656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.celestia-app/config/config.toml
```
