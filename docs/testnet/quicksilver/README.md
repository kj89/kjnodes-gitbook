# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/quicksilver.png" width="150" alt=""><figcaption></figcaption></figure>

Quicksilver is a permissionless, sovereign Cosmos SDK zone providing liquid staking for the entire Cosmos Ecosystem.

**Chain ID**: innuendo-5 | **Latest Version Tag**: v1.4.0-rc10.2 | **Wasm**: OFF

[Website](https://quicksilver.zone) | [Discord](https://discord.gg/quicksilverprotocol) | [Twitter](https://twitter.com/quicksilverzone)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/quicksilver-testnet](https://explorer.kjnodes.com/quicksilver-testnet)

## Public endpoints

* api: [https://quicksilver-testnet.api.kjnodes.com](https://quicksilver-testnet.api.kjnodes.com)
* rpc: [https://quicksilver-testnet.rpc.kjnodes.com](https://quicksilver-testnet.rpc.kjnodes.com)
* grpc: quicksilver-testnet.grpc.kjnodes.com:11090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@quicksilver-testnet.rpc.kjnodes.com:11656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@quicksilver-testnet.rpc.kjnodes.com:11659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/quicksilver-testnet/addrbook.json > $HOME/.quicksilverd/config/addrbook.json
```

**live-peers** (30)
```bash
peers="e25a748120c9608c1d2a70fafa75178d862b3463@178.18.254.211:10656,a637b94cb989909cc182623748ef179b0659f148@65.109.23.114:11156,0551eaa0db7097274410ee27a71672817e314b83@167.235.245.191:26656,78d271e4b4692ff1ee8490f3825a541558b31870@65.21.95.46:28656,8ff8a186fe9cbc70d0f34891fa051f87e561a48b@158.160.0.93:26656,2be586e675b0f55c96905cc83496861c64112f44@65.108.99.224:56656,a49d8d304e96350272dca24934b8295bc81d75d2@23.227.200.10:26656,f0621c59ca7cfba98015ae2a47886fc3d9c0020c@94.130.132.227:2060,f7edad3ff5a85d039e7de12067c63064c5b42d63@46.4.121.72:11656,1c4274460224753e8080d0efd16c0ed88fe27fc0@51.195.145.103:26656,42f87cb55d5fdd222da28023613c66857398c4b8@5.22.223.252:26656,3519e61e653db97f5d1c7f1bec9b0072bca4d5fe@144.76.45.59:16656,c9a74cdd754a8ccc9243ac2b245e4caaa78695aa@45.85.147.96:26656,a288baa951cbe92b253c01c3936d930af1d56424@5.161.142.236:26656,13564ca7ffcc8fa6bcc6d405c96fe8c724ec17da@88.99.213.25:11656,c409d9297f85d1290b4d6b208a1e66015c51434d@5.161.145.173:26656,9434d151be05e013cb0f20d27b699c8272ec4c89@65.109.82.111:29656,87d4e2b90141d5d52ed04387db4a46408c3fd66c@35.228.160.230:26656,ee6bae1a6d4a1e07f1e4bc7963cabedc6b73426e@94.130.137.119:26656,d4d83e209a2b096859821228ea17475f9a487a48@23.88.0.170:15651,97377c16946f8e1fa69e7c2c6b7feb32c2090f09@116.202.227.117:11656,1452d484454c0f93ddf3cbf987ce1b9cadd8f23f@65.21.95.180:37656,0a3ac40a7a4ce35978c4da97be2eb6974bc3c58b@185.252.233.217:46656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:11656,f6f1e4a0baf856ff7d7f6d12868a201282914314@65.109.89.5:26656,03332cdbc3d354846a18992effbb8c20aa28f52a@65.21.133.125:28656,70c7663dba3b5181f1c3b8c92824dad070771ac6@217.13.223.167:56656,858ba6bc33a6d13fdd9ddad344d788dcf91cf565@142.132.151.99:15651,bdb93c655989b2c1882339fabb013317066dda56@95.214.52.138:26676,a37474c1f254cd4b16d924327a755c914e8e7d86@65.109.30.53:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quicksilverd/config/config.toml
```
