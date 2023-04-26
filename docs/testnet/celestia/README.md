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
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:20656,5fa6853eb52bc3a5ff1fe56b988515d16644819a@65.21.232.33:2000,a20a5f47307049619d2fe689f3c33f1f7ab9470c@162.55.245.144:2130,e85b086d236a2c9a4d285e6d44126bb6fc6a1555@131.153.158.209:26656,7a89c8c63ee0a305d236eabb435ea54f1c08d3dd@125.143.190.194:17002,0aaea869d3c651143114f8e9529da72e40fe0828@46.4.5.45:11656,10c84789386c2ee3aacd8e09f04b78fac14fb3d7@209.126.86.119:26656,71819ce1899c1f4f0f138f7a538958dd0d3d3ff8@5.9.78.252:27656,fa3393d9ea9280d0042498b50da7c8e03c60c1e6@199.247.3.78:26656,e2aa8686a4b947fef3e14eb6b6106c180edb646a@109.205.181.63:26656,fc7aa57ff8e73fa1ed4dfa378f1c698ca029931b@38.242.143.102:26656,256897ad4c3888009256fa0dbd41949a882fe9d7@38.242.246.25:26656,afa8e3de3c304db0fae0113428c1747081df35a2@194.163.134.232:26656,c2c0ef31ed6d917dd675bd3599337235cd855e19@75.119.136.249:26656,b861e12c6d005f424dcb787865ea22ff7de4c1c3@194.163.169.224:26656,3ef426538e3b8bfa274aa9a442583bbbda71942f@185.144.99.12:26656,3602bfcd427d77dee80f287c9a7318fb2626890d@194.163.150.84:26656,105fc5cb9aa3a4c83bcc238e487b64116333800d@212.90.121.74:26656,2d778f142a6e483d7e60856e77c408e7af0911a2@38.242.245.230:26656,ac1e585064da1976680820fdd7f4adbdba436531@89.116.31.113:26656,9df27099090e78f6091193c29a77d7858f59ec31@31.220.73.124:26656,60265d9737ffaae69ee9940cd3ad44a47a7b5bab@161.97.148.199:26656,4a198b31a0f348a9f74f0a085bde574e55844ec4@89.116.31.123:26656,508706c7c37a7a5e4c99c4581d9334cbad34cb86@37.27.2.226:26656,768ac4ece936ca4eb01b763c119edb74c53b58b2@135.181.26.67:26656,9497e0c783d5cb9b18f6addfcf2f25cdc4d5d1a2@148.113.153.79:36656,19e453feaf0d1400a03674166d225258fa9e7657@194.163.149.204:26656,af66f28f19f747bd2b5a18d91d143dc8e035f86a@47.147.226.228:52656,e35144c78e110e2fa9c8ccdce919ae7b028d106d@3.144.212.128:31380,dc76534dfede17c47ec162fce0937b446a627820@206.189.92.202:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.celestia-app/config/config.toml
```
