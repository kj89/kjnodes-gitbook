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
peers="c97019ef9ee43e93ad9019514b612e6b8363c3fd@138.201.63.38:26686,5fa6853eb52bc3a5ff1fe56b988515d16644819a@65.21.232.33:2000,0196b56324c6fd3dd31110d3cb06dc169a1e1310@194.62.97.31:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:12056,e85b086d236a2c9a4d285e6d44126bb6fc6a1555@131.153.158.209:26656,6fbb911f2d20d86a77ecb8b8e95f6e80cfb62548@144.76.236.211:26656,c08cc20656b20b9590bfb28980100900631e3709@162.19.58.103:26656,3ef426538e3b8bfa274aa9a442583bbbda71942f@185.144.99.12:26656,6c73374cb78a543e2dd3eb218c29386392da2cf5@35.210.99.77:26656,f9e950870eccdb40e2386896d7b6a7687a103c99@88.99.219.120:43656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.celestia-app/config/config.toml
```
