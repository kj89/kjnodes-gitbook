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
peers="f9e950870eccdb40e2386896d7b6a7687a103c99@88.99.219.120:43656,de36dc2bc32ecaacafb213d173f6218f93ebb306@144.76.105.14:26656,6fbb911f2d20d86a77ecb8b8e95f6e80cfb62548@144.76.236.211:26656,384266dddab82417fb12ac44a9bdd36578a9cf0c@185.255.131.173:26656,0293f2cf7184da95bc6ea6ff31c7e97578b9c7ff@65.109.106.95:26656,ebf8c82dd6bc37aebcc38f5bff61593d9e3ca370@65.21.163.230:26656,23c69377c73644e125d29cb01d1f61e897fc0ae4@65.109.104.70:21066,ed878d106169c4ac694f571d78b99d8abfe29b33@149.102.130.59:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:20656,dc76534dfede17c47ec162fce0937b446a627820@206.189.92.202:26656,da5dd22ae25a061d92cd7979e8977c449712a19d@46.4.23.42:26656,2b9c71541bb54d13e887b9ec6ff88bf09ea4c4a3@138.197.134.254:26656,94b63fddfc78230f51aeb7ac34b9fb86bd042a77@46.4.53.94:30582,6f3b4a8311463a03805fc6dcf48ea00b3f84357e@65.108.234.207:26656,29c8a82a0be59a2c6a5d6fb2ad0a2e1b4d09de0f@186.3.232.252:26656,5d02fa37f0fe3f198b3fdcea78b8961d04425b5d@185.227.135.173:26656,af66f28f19f747bd2b5a18d91d143dc8e035f86a@47.147.226.228:52656,a86db178fbf5f9072b1bd0df465b947c5bb715e1@142.165.207.19:46656,143a1eda55f71240a9b22a1bedc00868fd2a46de@65.109.19.168:26656,be935b5942fd13c739983a53416006c83837a4d2@178.170.47.171:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.celestia-app/config/config.toml
```
