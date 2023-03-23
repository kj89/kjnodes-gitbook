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
peers="de36dc2bc32ecaacafb213d173f6218f93ebb306@144.76.105.14:26656,cc167c48a977160de9f9bbb5c3b80ddb7d585a67@176.9.156.135:26656,b766d36a1e3bcefc5e5befddfad7b4589ba28a21@162.55.242.83:26656,f9e950870eccdb40e2386896d7b6a7687a103c99@88.99.219.120:43656,27238e2f804bf28a14c186a2e0f0ceaae0d2588f@176.9.98.24:30590,b1b42ed03d101f8d0225b9796bfc9b628a2418c7@104.248.129.29:26656,1f05828ec9264cfa83454b0176414006bd40dce3@162.19.171.122:26656,f94f42134de575d00a75f8b2f77e4c56cdb750fc@88.217.142.187:26696,e85b086d236a2c9a4d285e6d44126bb6fc6a1555@131.153.158.209:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:20656,b937814a2ddd889a9a72aaf48d013a47f98721ee@217.160.39.214:26656,68a87c501de64b9259a0023d20fb805dff89082e@13.58.18.103:31380,2b9c71541bb54d13e887b9ec6ff88bf09ea4c4a3@138.197.134.254:26656,572cb08735d4572fe62b2fc8b9555c479d8e162f@65.108.137.217:26656,b9a59a4e1e521ff3bf651c20a17bbad61fdd443d@104.128.62.172:26656,29c8a82a0be59a2c6a5d6fb2ad0a2e1b4d09de0f@186.3.232.252:26656,af66f28f19f747bd2b5a18d91d143dc8e035f86a@47.147.226.228:52656,63636c9bec15f0039f78bc48736fe8b84e9e8a60@38.242.233.37:26656,55c8588444791ceccc9bc380415773465574ab67@95.217.114.226:26656,dee24c88c902ae0b117141f3b1e696b5c92d8e51@57.128.74.73:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.celestia-app/config/config.toml
```
