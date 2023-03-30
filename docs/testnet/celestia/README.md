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

**live-peers** (21)
```bash
peers="02241bb63c01fb52033029f7155c3db5d7846c1f@168.119.64.26:26656,e85b086d236a2c9a4d285e6d44126bb6fc6a1555@131.153.158.209:26656,9fd9275b49d478bf8352dc160dc0e9a184011098@217.182.194.152:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:20656,ed878d106169c4ac694f571d78b99d8abfe29b33@149.102.130.59:26656,a86db178fbf5f9072b1bd0df465b947c5bb715e1@142.165.207.19:46656,29c8a82a0be59a2c6a5d6fb2ad0a2e1b4d09de0f@186.3.232.252:26656,7a89c8c63ee0a305d236eabb435ea54f1c08d3dd@125.143.190.194:17002,5d02fa37f0fe3f198b3fdcea78b8961d04425b5d@185.227.135.173:26656,2b8f5b788108c593378ce0dad8faff180b854cb4@185.56.139.86:26656,dc76534dfede17c47ec162fce0937b446a627820@206.189.92.202:26656,384266dddab82417fb12ac44a9bdd36578a9cf0c@185.255.131.173:26656,f9e950870eccdb40e2386896d7b6a7687a103c99@88.99.219.120:43656,af66f28f19f747bd2b5a18d91d143dc8e035f86a@47.147.226.228:52656,60e771182358034b4ce475b7a0d8d48734aa9dc8@85.190.134.34:26656,ebf8c82dd6bc37aebcc38f5bff61593d9e3ca370@65.21.163.230:26656,43e9da043318a4ea0141259c17fcb06ecff816af@141.94.73.39:43656,5c464c8a7f4182492f3e0ab71f14c3f3a43b5f7b@176.9.157.38:26656,7db3d8fa353b4cf293244f7526cdabfaebef53bf@158.160.24.133:26656,3ef426538e3b8bfa274aa9a442583bbbda71942f@185.144.99.12:26656,0293f2cf7184da95bc6ea6ff31c7e97578b9c7ff@65.109.106.95:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.celestia-app/config/config.toml
```
