# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/celestia.png" width="150" alt=""><figcaption></figcaption></figure>

Celestia is a minimal blockchain that only orders and publishes transactions and  does not execute them. By decoupling the consensus and application execution layers,  Celestia modularizes the blockchain technology stack and unlocks new possibilities  for decentralized application builders.

**Chain ID**: blockspacerace-0 | **Latest Version Tag**: v0.12.1 | **Wasm**: OFF

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

**live-peers** (19)
```bash
peers="b1b42ed03d101f8d0225b9796bfc9b628a2418c7@104.248.129.29:26656,60e771182358034b4ce475b7a0d8d48734aa9dc8@85.190.134.34:26656,1f05828ec9264cfa83454b0176414006bd40dce3@162.19.171.122:26656,dee24c88c902ae0b117141f3b1e696b5c92d8e51@57.128.74.73:26656,e85b086d236a2c9a4d285e6d44126bb6fc6a1555@131.153.158.209:26656,f94f42134de575d00a75f8b2f77e4c56cdb750fc@88.217.142.187:26696,23c69377c73644e125d29cb01d1f61e897fc0ae4@65.109.104.70:21066,ed878d106169c4ac694f571d78b99d8abfe29b33@149.102.130.59:26656,572cb08735d4572fe62b2fc8b9555c479d8e162f@65.108.137.217:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:20656,29c8a82a0be59a2c6a5d6fb2ad0a2e1b4d09de0f@186.3.232.252:26656,2b8f5b788108c593378ce0dad8faff180b854cb4@185.56.139.86:26656,8ed1977a80f1600815e44b981c3bf51506797843@141.94.252.88:31870,a86db178fbf5f9072b1bd0df465b947c5bb715e1@142.165.207.19:46656,dc76534dfede17c47ec162fce0937b446a627820@206.189.92.202:26656,af66f28f19f747bd2b5a18d91d143dc8e035f86a@47.147.226.228:52656,2b9c71541bb54d13e887b9ec6ff88bf09ea4c4a3@138.197.134.254:26656,0293f2cf7184da95bc6ea6ff31c7e97578b9c7ff@65.109.106.95:26656,7d6d1d1c3498687d4705fe4c7216623797835fae@74.118.136.164:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.celestia-app/config/config.toml
```
