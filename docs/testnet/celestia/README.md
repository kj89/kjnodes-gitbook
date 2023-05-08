# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/celestia.png" alt=""><figcaption></figcaption></figure>

Celestia is a minimal blockchain that only orders and publishes transactions and  does not execute them. By decoupling the consensus and application execution layers,  Celestia modularizes the blockchain technology stack and unlocks new possibilities  for decentralized application builders.

**Chain ID**: blockspacerace-0 | **Latest Version Tag**: v0.12.1 | **Wasm**: OFF

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

**live-peers** (9)
```bash
peers="b1b42ed03d101f8d0225b9796bfc9b628a2418c7@104.248.129.29:26656,62f6abc162db99389f13a1cdf1abaeb6efb647a7@35.210.78.75:26656,af66f28f19f747bd2b5a18d91d143dc8e035f86a@47.147.226.228:52656,92e7087b3dec79fb2b8105e5a61935d28927d511@45.83.104.218:2000,de36dc2bc32ecaacafb213d173f6218f93ebb306@144.76.105.14:26656,a20a5f47307049619d2fe689f3c33f1f7ab9470c@162.55.245.144:2130,10c84789386c2ee3aacd8e09f04b78fac14fb3d7@209.126.86.119:26656,6c73374cb78a543e2dd3eb218c29386392da2cf5@35.210.99.77:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:12056"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.celestia-app/config/config.toml
```
