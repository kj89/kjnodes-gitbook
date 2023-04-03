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

**live-peers** (29)
```bash
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:20656,3ef426538e3b8bfa274aa9a442583bbbda71942f@185.144.99.12:26656,e85b086d236a2c9a4d285e6d44126bb6fc6a1555@131.153.158.209:26656,5d02fa37f0fe3f198b3fdcea78b8961d04425b5d@185.227.135.173:26656,e225815e3da7a26d712c074045977034a901bbc0@5.9.106.214:26686,cb0c8eab8b18c4c6a2d0cc030d1b0787656b61bb@65.108.137.39:26656,721d15a87ce8b3062284614def3c32b72019de5b@35.206.161.204:26656,a20a5f47307049619d2fe689f3c33f1f7ab9470c@162.55.245.144:2130,24770b73138ee6a2113e4c35b5e3525749c21350@109.238.11.182:26656,0293f2cf7184da95bc6ea6ff31c7e97578b9c7ff@65.109.106.95:26656,5fa6853eb52bc3a5ff1fe56b988515d16644819a@65.21.232.33:2000,e4fa11cfb413d69d95dc90a0e12125b091b1d574@51.158.115.159:26656,3470257481d3f6cf1f7b13e47ce4347624f185c8@190.2.136.144:30156,c97019ef9ee43e93ad9019514b612e6b8363c3fd@138.201.63.38:26686,2b8f5b788108c593378ce0dad8faff180b854cb4@185.56.139.86:26656,ebf8c82dd6bc37aebcc38f5bff61593d9e3ca370@65.21.163.230:26656,7a89c8c63ee0a305d236eabb435ea54f1c08d3dd@125.143.190.194:17002,63636c9bec15f0039f78bc48736fe8b84e9e8a60@38.242.233.37:26656,8f14ec71e1d712c912c27485a169c2519628cfb6@185.225.232.196:21656,2b749c2f0dd5953eeb5379c7ae7a15ed1020f7e5@135.181.136.124:26656,10c84789386c2ee3aacd8e09f04b78fac14fb3d7@209.126.86.119:26656,28ec6fc21844eb07f8264694c723a8c6056b16c1@195.74.52.167:26656,2b9c71541bb54d13e887b9ec6ff88bf09ea4c4a3@138.197.134.254:26656,a98c082b003204f1bf4483cf2eb6ef2a7df4c8a2@103.50.32.25:26656,5f8be26e18e08d32b5f4273063819793fd9f93a4@35.206.182.97:26656,29c8a82a0be59a2c6a5d6fb2ad0a2e1b4d09de0f@186.3.232.252:26656,dc76534dfede17c47ec162fce0937b446a627820@206.189.92.202:26656,ccbd6262d0324e2e858594b639f4296cc4952c93@13.57.127.89:26656,af66f28f19f747bd2b5a18d91d143dc8e035f86a@47.147.226.228:52656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.celestia-app/config/config.toml
```
