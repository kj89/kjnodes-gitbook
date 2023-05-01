# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/gitopia.png" alt=""><figcaption></figcaption></figure>

Gitopia is the next-generation Code Collaboration Platform fuelled by  a decentralized network and interactive token economy. It is designed  to optimize the open-source software development process through  collaboration, transparency, and incentivization.

**Chain ID**: gitopia-janus-testnet-2 | **Latest Version Tag**: v1.2.0 | **Wasm**: OFF

[Website](https://gitopia.com/) | [Discord](https://discord.gg/hFTXCGNYDZ) | [Twitter](https://twitter.com/gitopiaDAO)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/gitopia-testnet](https://explorer.kjnodes.com/gitopia-testnet)

## Public endpoints

* api: [https://gitopia-testnet.api.kjnodes.com](https://gitopia-testnet.api.kjnodes.com)
* rpc: [https://gitopia-testnet.rpc.kjnodes.com](https://gitopia-testnet.rpc.kjnodes.com)
* grpc: gitopia-testnet.grpc.kjnodes.com:141090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@gitopia-testnet.rpc.kjnodes.com:141656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@gitopia-testnet.rpc.kjnodes.com:141659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/gitopia-testnet/addrbook.json > $HOME/.gitopia/config/addrbook.json
```

**live-peers** (30)
```bash
peers="9cd6d2477d278ef6ccffa5cc4e22fd0d9489cd23@85.10.199.157:34656,eccdf1d5bf33bc1733838562b4d4a4a45869c3a8@135.181.183.93:41656,f13a4cb3ca18c1de6232e901c8feb209f0945954@65.109.65.248:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,bd7c6c83af99edf0ee5b857a99997fb9fc8f40a7@65.109.116.204:20556,a8e74ebf033def6fbb28d1b846d7a6c275ad2ef1@65.109.65.163:20556,820024c34989e7605d9367847e1fc2d01ad763bd@65.109.92.235:30656,ac606e28c081c679dc23d9a94c29842be8f8b1f1@45.85.249.133:656,399d4e19186577b04c23296c4f7ecc53e61080cb@34.143.189.236:26656,0150c41282284a9546f8fe0f2531fc6b9d9128a3@65.109.23.114:11356,a6f4fd8efe8a575a15e25652ecebce3fa1ed62a0@213.239.217.52:35656,8bec864d68a2542233ba37ac94c723fdf0b8e175@45.151.122.136:656,f0a82f850a0da74c32836b125a52bdfd9a78fdd7@65.108.105.48:11356,37677351ed74a5ced46a99217d19e30d5bcacc1d@5.75.147.138:26656,bce720f986092e4fb804655400cea1dbf29b594f@116.202.227.117:41656,46dbff2358dddd99acc26c2d2ee5f204ccc347c7@217.76.61.242:26656,619a23818cddd40d0b9f57e9754b719da13609bc@65.108.108.52:24656,4e0e57bcac8aa2bc3188d5b7845eeee61a61f3f0@194.163.170.165:26656,88ce80cb509fd973e06a552e1a5075d1292545d6@46.166.172.226:26656,1cf3826ccd9a24caa549cbea061446716858133e@154.26.130.95:36656,3e5ba61e8481c6c71d3f2cc022dd6671ed7cacf8@65.21.170.3:41656,975a3ade04fc92d00c7ad59d536506fde46169e7@167.86.96.233:656,81f9bdd0e1e01390b70df7544b45efdccb52e41c@84.54.23.199:26656,1f0f03a1c845e810e5cfeb0d960639c637d049fe@154.26.131.130:36656,eaa9978430e55663346eb61312cd5ecc21448b25@38.242.139.153:656,4cd60a4dd4211d38d948a86a614f1fd8d3d274eb@75.119.153.139:656,b745e0c6a1e0c7ec248ec274cfd038ed4bc4c2cf@65.21.134.202:26356,f0b8227e40f25eaec0e25b9e91ca199d2d9a1ecb@167.86.94.177:656,082e95b5d5351e68dcfb24dff802f9064cfd5a4c@65.109.92.241:51056,7da6c90fe420bca73b5274884236134acf49d565@35.168.32.254:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gitopia/config/config.toml
```
