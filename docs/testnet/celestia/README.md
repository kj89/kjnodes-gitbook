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

**live-peers** (14)
```bash
peers="f7916ed6f294f94740b98b5a7f21d368589fee56@202.61.194.254:60956,5c464c8a7f4182492f3e0ab71f14c3f3a43b5f7b@176.9.157.38:26656,5fa6853eb52bc3a5ff1fe56b988515d16644819a@65.21.232.33:2000,02b93545950853d692d7ea63eac879e6dd4bf390@82.223.122.139:26656,64dc65c92babc84a3ce0791c704f5907851d3e93@38.242.217.231:12056,af66f28f19f747bd2b5a18d91d143dc8e035f86a@47.147.226.228:52656,8f14ec71e1d712c912c27485a169c2519628cfb6@185.225.232.196:21656,73e2aa2de6080734152b54020464fb9ba752a7dd@194.36.145.127:26656,7135928a1a9e6cc13d139a67b4ef94c53f470e15@154.12.252.237:26656,60e771182358034b4ce475b7a0d8d48734aa9dc8@85.190.134.34:26656,7b2fb9cdedb18336e55f4e8613e841982e455ba6@31.7.196.40:26656,6c73374cb78a543e2dd3eb218c29386392da2cf5@35.210.99.77:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:12056,92e7087b3dec79fb2b8105e5a61935d28927d511@45.83.104.218:2000"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.celestia-app/config/config.toml
```
