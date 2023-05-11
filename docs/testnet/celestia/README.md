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
peers="7135928a1a9e6cc13d139a67b4ef94c53f470e15@154.12.252.237:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:12056,c08cc20656b20b9590bfb28980100900631e3709@162.19.58.103:26656,e85b086d236a2c9a4d285e6d44126bb6fc6a1555@131.153.158.209:26656,ae95e8d93a0822a763823551c163d15d4cdce944@116.202.227.117:20656,a1b78a15e9a66f38903d66d019f9fb6c3066f936@31.220.87.65:26656,c97019ef9ee43e93ad9019514b612e6b8363c3fd@138.201.63.38:26686,62f6abc162db99389f13a1cdf1abaeb6efb647a7@35.210.78.75:26656,0196b56324c6fd3dd31110d3cb06dc169a1e1310@194.62.97.31:26656,5fa6853eb52bc3a5ff1fe56b988515d16644819a@65.21.232.33:2000"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.celestia-app/config/config.toml
```
