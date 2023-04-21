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
peers="721d15a87ce8b3062284614def3c32b72019de5b@35.206.161.204:26656,9fd9275b49d478bf8352dc160dc0e9a184011098@217.182.194.152:26656,af66f28f19f747bd2b5a18d91d143dc8e035f86a@47.147.226.228:52656,19879d1fdf925d85f6892209297e27801184be63@89.116.31.225:26656,afa8e3de3c304db0fae0113428c1747081df35a2@194.163.134.232:26656,3ef426538e3b8bfa274aa9a442583bbbda71942f@185.144.99.12:26656,5fa6853eb52bc3a5ff1fe56b988515d16644819a@65.21.232.33:2000,a20a5f47307049619d2fe689f3c33f1f7ab9470c@162.55.245.144:2130,2b8f5b788108c593378ce0dad8faff180b854cb4@185.56.139.86:26656,e4fa11cfb413d69d95dc90a0e12125b091b1d574@51.158.115.159:26656,cb0c8eab8b18c4c6a2d0cc030d1b0787656b61bb@65.108.137.39:26656,fb9fc76ee67cd021b913752b49560dd9184688f2@135.181.216.215:36656,8f14ec71e1d712c912c27485a169c2519628cfb6@185.225.232.196:21656,fedea9723696360d429a23792225594779cc7cd7@65.108.231.124:11656,7a89c8c63ee0a305d236eabb435ea54f1c08d3dd@125.143.190.194:17002,e85b086d236a2c9a4d285e6d44126bb6fc6a1555@131.153.158.209:26656,24770b73138ee6a2113e4c35b5e3525749c21350@109.238.11.182:26656,768ac4ece936ca4eb01b763c119edb74c53b58b2@135.181.26.67:26656,38a3604c87e19301b2a028ef0b4a0735014de749@64.25.109.145:26656,10297d22a2f1f66bfb9f2c8f7d7152660bfffd92@65.109.32.148:26116,9497e0c783d5cb9b18f6addfcf2f25cdc4d5d1a2@148.113.153.79:36656,508706c7c37a7a5e4c99c4581d9334cbad34cb86@37.27.2.226:26656,0293f2cf7184da95bc6ea6ff31c7e97578b9c7ff@65.109.106.95:26656,f94f42134de575d00a75f8b2f77e4c56cdb750fc@88.217.142.187:26696,92e7087b3dec79fb2b8105e5a61935d28927d511@45.83.104.218:2000,6855a5168a860ca61b876c12cf7882b3be4ad58a@35.210.7.124:26656,e35144c78e110e2fa9c8ccdce919ae7b028d106d@3.144.212.128:31380,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:20656,f44d744448c0b6c4b722bb6ae62d31a800d447ef@66.94.127.235:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.celestia-app/config/config.toml
```
