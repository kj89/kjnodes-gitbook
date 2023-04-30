# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/celestia.png" alt=""><figcaption></figcaption></figure>

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

**live-peers** (30)
```bash
peers="62f6abc162db99389f13a1cdf1abaeb6efb647a7@35.210.78.75:26656,6f3b4a8311463a03805fc6dcf48ea00b3f84357e@65.108.234.207:26656,359ee07d67c29935472987e54ad0a3329a9b9a73@95.217.38.122:26656,e85b086d236a2c9a4d285e6d44126bb6fc6a1555@131.153.158.209:26656,6c73374cb78a543e2dd3eb218c29386392da2cf5@35.210.99.77:26656,2b8f5b788108c593378ce0dad8faff180b854cb4@185.56.139.86:26656,5fa6853eb52bc3a5ff1fe56b988515d16644819a@65.21.232.33:2000,a20a5f47307049619d2fe689f3c33f1f7ab9470c@162.55.245.144:2130,7a89c8c63ee0a305d236eabb435ea54f1c08d3dd@125.143.190.194:17002,9497e0c783d5cb9b18f6addfcf2f25cdc4d5d1a2@148.113.153.79:36656,92e7087b3dec79fb2b8105e5a61935d28927d511@45.83.104.218:2000,9df27099090e78f6091193c29a77d7858f59ec31@31.220.73.124:26656,60265d9737ffaae69ee9940cd3ad44a47a7b5bab@161.97.148.199:26656,105fc5cb9aa3a4c83bcc238e487b64116333800d@212.90.121.74:26656,c2c0ef31ed6d917dd675bd3599337235cd855e19@75.119.136.249:26656,fc7aa57ff8e73fa1ed4dfa378f1c698ca029931b@38.242.143.102:26656,b861e12c6d005f424dcb787865ea22ff7de4c1c3@194.163.169.224:26656,3ef426538e3b8bfa274aa9a442583bbbda71942f@185.144.99.12:26656,afa8e3de3c304db0fae0113428c1747081df35a2@194.163.134.232:26656,3602bfcd427d77dee80f287c9a7318fb2626890d@194.163.150.84:26656,e2aa8686a4b947fef3e14eb6b6106c180edb646a@109.205.181.63:26656,4a198b31a0f348a9f74f0a085bde574e55844ec4@89.116.31.123:26656,256897ad4c3888009256fa0dbd41949a882fe9d7@38.242.246.25:26656,ac1e585064da1976680820fdd7f4adbdba436531@89.116.31.113:26656,d3c0e1867ba635328dc019f1464acf1903f446a5@13.208.144.128:16656,10c84789386c2ee3aacd8e09f04b78fac14fb3d7@209.126.86.119:26656,af66f28f19f747bd2b5a18d91d143dc8e035f86a@47.147.226.228:52656,5729746e91760433f12f632fa9cca73f7389b087@23.91.80.34:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:20656,8c0856a492a6842a2a2483c400a571174053a107@38.242.133.24:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.celestia-app/config/config.toml
```
