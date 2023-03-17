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
peers="8ec3dfbfa971264d8cdd86352ffa7bf95d341254@168.119.64.90:26656,d046e88879cf5f6299cfc87ec05038ea98ee3aa0@5.9.154.105:26656,5c464c8a7f4182492f3e0ab71f14c3f3a43b5f7b@176.9.157.38:26656,da5dd22ae25a061d92cd7979e8977c449712a19d@46.4.23.42:26656,dee24c88c902ae0b117141f3b1e696b5c92d8e51@57.128.74.73:26656,143a1eda55f71240a9b22a1bedc00868fd2a46de@65.109.19.168:26656,b820b229105de6beeca1ab9b5e2aae787cdf73b8@141.94.162.118:26656,02b93545950853d692d7ea63eac879e6dd4bf390@82.223.122.139:26656,b937814a2ddd889a9a72aaf48d013a47f98721ee@217.160.39.214:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:20656,ebf8c82dd6bc37aebcc38f5bff61593d9e3ca370@65.21.163.230:26656,e9f81c5428fb9f3645c691dfd3f1038705bbc734@54.160.136.237:26656,a86db178fbf5f9072b1bd0df465b947c5bb715e1@142.165.207.19:46656,dc76534dfede17c47ec162fce0937b446a627820@206.189.92.202:26656,b9a59a4e1e521ff3bf651c20a17bbad61fdd443d@104.128.62.172:26656,29c8a82a0be59a2c6a5d6fb2ad0a2e1b4d09de0f@186.3.232.252:26656,2b9c71541bb54d13e887b9ec6ff88bf09ea4c4a3@138.197.134.254:26656,b1b42ed03d101f8d0225b9796bfc9b628a2418c7@104.248.129.29:26656,af66f28f19f747bd2b5a18d91d143dc8e035f86a@47.147.226.228:52656,23c69377c73644e125d29cb01d1f61e897fc0ae4@65.109.104.70:21066"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.celestia-app/config/config.toml
```
