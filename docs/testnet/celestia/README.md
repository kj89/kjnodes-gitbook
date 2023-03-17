# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/celestia.png" width="150" alt=""><figcaption></figcaption></figure>

Celestia is a minimal blockchain that only orders and publishes transactions and  does not execute them. By decoupling the consensus and application execution layers,  Celestia modularizes the blockchain technology stack and unlocks new possibilities  for decentralized application builders.

**Chain ID**: blockspacerace-0 | **Latest Version Tag**: v0.12.0 | **Wasm**: OFF

[Website](https://celestia.org) | [Discord](https://discord.gg/celestiacommunity) | [Twitter](https://twitter.com/CelestiaOrg)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/celestia-testnet](https://explorer.kjnodes.com/celestia-testnet)

## Public endpoints

* api: [https://celestia-testnet.api.kjnodes.com](https://celestia-testnet.api.kjnodes.com)
* rpc: [https://celestia-testnet.rpc.kjnodes.com](https://celestia-testnet.rpc.kjnodes.com)
* grpc: celestia-testnet.grpc.kjnodes.com:20090

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

**live-peers** (20)
```bash
peers="da5dd22ae25a061d92cd7979e8977c449712a19d@46.4.23.42:26656,5c464c8a7f4182492f3e0ab71f14c3f3a43b5f7b@176.9.157.38:26656,b1b42ed03d101f8d0225b9796bfc9b628a2418c7@104.248.129.29:26656,d78275c79f81efc0eb357cec3ec35877efec4974@57.128.74.131:26656,7d6d1d1c3498687d4705fe4c7216623797835fae@74.118.136.164:26656,2b749c2f0dd5953eeb5379c7ae7a15ed1020f7e5@135.181.136.124:26656,6f3d14f3ca7bb06e6ba560ab78e70aa77c0ca0d0@65.108.99.238:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:20656,143a1eda55f71240a9b22a1bedc00868fd2a46de@65.109.19.168:26656,ed878d106169c4ac694f571d78b99d8abfe29b33@149.102.130.59:26656,b937814a2ddd889a9a72aaf48d013a47f98721ee@217.160.39.214:26656,b9a59a4e1e521ff3bf651c20a17bbad61fdd443d@104.128.62.172:26656,e9f81c5428fb9f3645c691dfd3f1038705bbc734@54.160.136.237:26656,29c8a82a0be59a2c6a5d6fb2ad0a2e1b4d09de0f@186.3.232.252:26656,af66f28f19f747bd2b5a18d91d143dc8e035f86a@47.147.226.228:52656,dc76534dfede17c47ec162fce0937b446a627820@206.189.92.202:26656,02b93545950853d692d7ea63eac879e6dd4bf390@82.223.122.139:26656,ebf8c82dd6bc37aebcc38f5bff61593d9e3ca370@65.21.163.230:26656,a86db178fbf5f9072b1bd0df465b947c5bb715e1@142.165.207.19:46656,6fbb911f2d20d86a77ecb8b8e95f6e80cfb62548@144.76.236.211:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.celestia-app/config/config.toml
```
