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
peers="f94f42134de575d00a75f8b2f77e4c56cdb750fc@88.217.142.187:26696,e85b086d236a2c9a4d285e6d44126bb6fc6a1555@131.153.158.209:26656,92e7087b3dec79fb2b8105e5a61935d28927d511@45.83.104.218:2000,a20a5f47307049619d2fe689f3c33f1f7ab9470c@162.55.245.144:2130,2b8f5b788108c593378ce0dad8faff180b854cb4@185.56.139.86:26656,e4fa11cfb413d69d95dc90a0e12125b091b1d574@51.158.115.159:26656,24770b73138ee6a2113e4c35b5e3525749c21350@109.238.11.182:26656,fb9fc76ee67cd021b913752b49560dd9184688f2@135.181.216.215:36656,cb0c8eab8b18c4c6a2d0cc030d1b0787656b61bb@65.108.137.39:26656,38a3604c87e19301b2a028ef0b4a0735014de749@64.25.109.145:26656,9497e0c783d5cb9b18f6addfcf2f25cdc4d5d1a2@148.113.153.79:36656,721d15a87ce8b3062284614def3c32b72019de5b@35.206.161.204:26656,768ac4ece936ca4eb01b763c119edb74c53b58b2@135.181.26.67:26656,0293f2cf7184da95bc6ea6ff31c7e97578b9c7ff@65.109.106.95:26656,3ef426538e3b8bfa274aa9a442583bbbda71942f@185.144.99.12:26656,508706c7c37a7a5e4c99c4581d9334cbad34cb86@37.27.2.226:26656,aa0f4f7f63460c19b448004283b6d3ffc682e443@65.109.38.111:11656,5fa6853eb52bc3a5ff1fe56b988515d16644819a@65.21.232.33:2000,afa8e3de3c304db0fae0113428c1747081df35a2@194.163.134.232:26656,8f14ec71e1d712c912c27485a169c2519628cfb6@185.225.232.196:21656,7a89c8c63ee0a305d236eabb435ea54f1c08d3dd@125.143.190.194:17002,e225815e3da7a26d712c074045977034a901bbc0@5.9.106.214:26686,10c84789386c2ee3aacd8e09f04b78fac14fb3d7@209.126.86.119:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:20656,af66f28f19f747bd2b5a18d91d143dc8e035f86a@47.147.226.228:52656,d3c0e1867ba635328dc019f1464acf1903f446a5@13.208.144.128:16656,dc76534dfede17c47ec162fce0937b446a627820@206.189.92.202:26656,2b749c2f0dd5953eeb5379c7ae7a15ed1020f7e5@135.181.136.124:26656,fedea9723696360d429a23792225594779cc7cd7@65.108.231.124:11656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.celestia-app/config/config.toml
```
