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
peers="f9e950870eccdb40e2386896d7b6a7687a103c99@88.99.219.120:43656,5c464c8a7f4182492f3e0ab71f14c3f3a43b5f7b@176.9.157.38:26656,1f05828ec9264cfa83454b0176414006bd40dce3@162.19.171.122:26656,6fbb911f2d20d86a77ecb8b8e95f6e80cfb62548@144.76.236.211:26656,d046e88879cf5f6299cfc87ec05038ea98ee3aa0@5.9.154.105:26656,9fd9275b49d478bf8352dc160dc0e9a184011098@217.182.194.152:26656,6f3b4a8311463a03805fc6dcf48ea00b3f84357e@65.108.234.207:26656,ebf8c82dd6bc37aebcc38f5bff61593d9e3ca370@65.21.163.230:26656,a1e08e481992149d50cb74144602334e71fa3aa3@62.232.97.106:26656,b937814a2ddd889a9a72aaf48d013a47f98721ee@217.160.39.214:26656,dc76534dfede17c47ec162fce0937b446a627820@206.189.92.202:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:20656,b9a59a4e1e521ff3bf651c20a17bbad61fdd443d@104.128.62.172:26656,2b9c71541bb54d13e887b9ec6ff88bf09ea4c4a3@138.197.134.254:26656,29c8a82a0be59a2c6a5d6fb2ad0a2e1b4d09de0f@186.3.232.252:26656,143a1eda55f71240a9b22a1bedc00868fd2a46de@65.109.19.168:26656,7a89c8c63ee0a305d236eabb435ea54f1c08d3dd@125.143.190.194:17002,5cb79244142c36768571cf1e791578dc45969fd2@195.189.97.33:23656,ed878d106169c4ac694f571d78b99d8abfe29b33@149.102.130.59:26656,a86db178fbf5f9072b1bd0df465b947c5bb715e1@142.165.207.19:46656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.celestia-app/config/config.toml
```
