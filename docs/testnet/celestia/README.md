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

**live-peers** (10)
```bash
peers="2b9c71541bb54d13e887b9ec6ff88bf09ea4c4a3@138.197.134.254:26656,6c73374cb78a543e2dd3eb218c29386392da2cf5@35.210.99.77:26656,62f6abc162db99389f13a1cdf1abaeb6efb647a7@35.210.78.75:26656,7b2f4cb70f04f2e9befb6ace66ce1ac7b3bea5b4@178.239.197.179:26656,0aaea869d3c651143114f8e9529da72e40fe0828@46.4.5.45:11656,00a7e4228936c514fa7e9df6466ddad0d08cbef2@18.191.143.132:31380,a20a5f47307049619d2fe689f3c33f1f7ab9470c@162.55.245.144:2130,dc76534dfede17c47ec162fce0937b446a627820@206.189.92.202:26656,b937814a2ddd889a9a72aaf48d013a47f98721ee@217.160.39.214:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:12056"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.celestia-app/config/config.toml
```
