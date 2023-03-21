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
peers="b766d36a1e3bcefc5e5befddfad7b4589ba28a21@162.55.242.83:26656,da5dd22ae25a061d92cd7979e8977c449712a19d@46.4.23.42:26656,f9e950870eccdb40e2386896d7b6a7687a103c99@88.99.219.120:43656,2b8f5b788108c593378ce0dad8faff180b854cb4@185.56.139.86:26656,9fd9275b49d478bf8352dc160dc0e9a184011098@217.182.194.152:26656,6df4a6d0db5a771b84055646fe3814c655dd3428@95.216.163.64:26656,ed878d106169c4ac694f571d78b99d8abfe29b33@149.102.130.59:26656,5cb79244142c36768571cf1e791578dc45969fd2@195.189.97.33:23656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:20656,29c8a82a0be59a2c6a5d6fb2ad0a2e1b4d09de0f@186.3.232.252:26656,02c88d98245ec8b06546f6b19866b758f2df2c6e@95.217.194.249:26656,dc76534dfede17c47ec162fce0937b446a627820@206.189.92.202:26656,a86db178fbf5f9072b1bd0df465b947c5bb715e1@142.165.207.19:46656,af66f28f19f747bd2b5a18d91d143dc8e035f86a@47.147.226.228:52656,94b63fddfc78230f51aeb7ac34b9fb86bd042a77@46.4.53.94:30582,5d02fa37f0fe3f198b3fdcea78b8961d04425b5d@185.227.135.173:26656,7a89c8c63ee0a305d236eabb435ea54f1c08d3dd@125.143.190.194:17002,2b9c71541bb54d13e887b9ec6ff88bf09ea4c4a3@138.197.134.254:26656,b1b42ed03d101f8d0225b9796bfc9b628a2418c7@104.248.129.29:26656,46d3f4a8341c4523f4cafc778075688022280973@95.217.113.104:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.celestia-app/config/config.toml
```
