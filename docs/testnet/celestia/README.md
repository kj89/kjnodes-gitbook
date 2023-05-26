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
peers="5fa6853eb52bc3a5ff1fe56b988515d16644819a@65.21.232.33:2000,c97019ef9ee43e93ad9019514b612e6b8363c3fd@138.201.63.38:26686,8f14ec71e1d712c912c27485a169c2519628cfb6@185.225.232.196:21656,f7916ed6f294f94740b98b5a7f21d368589fee56@202.61.194.254:60956,e4fa11cfb413d69d95dc90a0e12125b091b1d574@51.158.115.159:26656,f05e6a065b772dda4c7c0cbed40894a8c43416c7@57.128.86.3:26656,6c73374cb78a543e2dd3eb218c29386392da2cf5@35.210.99.77:26656,0196b56324c6fd3dd31110d3cb06dc169a1e1310@194.62.97.31:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:12056,ae95e8d93a0822a763823551c163d15d4cdce944@116.202.227.117:20656,ecd7a4c6b4411023626b3ebc148657f0513ea7d3@68.183.113.7:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.celestia-app/config/config.toml
```
