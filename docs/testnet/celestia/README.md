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
peers="8ec3dfbfa971264d8cdd86352ffa7bf95d341254@168.119.64.90:26656,6fbb911f2d20d86a77ecb8b8e95f6e80cfb62548@144.76.236.211:26656,da5dd22ae25a061d92cd7979e8977c449712a19d@46.4.23.42:26656,f9e950870eccdb40e2386896d7b6a7687a103c99@88.99.219.120:43656,1f05828ec9264cfa83454b0176414006bd40dce3@162.19.171.122:26656,23c69377c73644e125d29cb01d1f61e897fc0ae4@65.109.104.70:21066,143a1eda55f71240a9b22a1bedc00868fd2a46de@65.109.19.168:26656,6f3b4a8311463a03805fc6dcf48ea00b3f84357e@65.108.234.207:26656,46d3f4a8341c4523f4cafc778075688022280973@95.217.113.104:26656,b937814a2ddd889a9a72aaf48d013a47f98721ee@217.160.39.214:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:20656,572cb08735d4572fe62b2fc8b9555c479d8e162f@65.108.137.217:26656,dc76534dfede17c47ec162fce0937b446a627820@206.189.92.202:26656,b9a59a4e1e521ff3bf651c20a17bbad61fdd443d@104.128.62.172:26656,29c8a82a0be59a2c6a5d6fb2ad0a2e1b4d09de0f@186.3.232.252:26656,af66f28f19f747bd2b5a18d91d143dc8e035f86a@47.147.226.228:52656,7d6d1d1c3498687d4705fe4c7216623797835fae@74.118.136.164:26656,a86db178fbf5f9072b1bd0df465b947c5bb715e1@142.165.207.19:46656,7a89c8c63ee0a305d236eabb435ea54f1c08d3dd@125.143.190.194:17002,de36dc2bc32ecaacafb213d173f6218f93ebb306@144.76.105.14:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.celestia-app/config/config.toml
```
