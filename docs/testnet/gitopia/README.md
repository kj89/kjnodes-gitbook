# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/gitopia.png" width="150" alt=""><figcaption></figcaption></figure>

Gitopia is the next-generation Code Collaboration Platform fuelled by  a decentralized network and interactive token economy. It is designed  to optimize the open-source software development process through  collaboration, transparency, and incentivization.

**Chain ID**: gitopia-janus-testnet-2 | **Latest Version Tag**: v1.2.0 | **Wasm**: OFF

[Website](https://gitopia.com/) | [Discord](https://discord.gg/hFTXCGNYDZ) | [Twitter](https://twitter.com/gitopiaDAO)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/gitopia-testnet](https://explorer.kjnodes.com/gitopia-testnet)

## Public endpoints

* api: [https://gitopia-testnet.api.kjnodes.com](https://gitopia-testnet.api.kjnodes.com)
* rpc: [https://gitopia-testnet.rpc.kjnodes.com](https://gitopia-testnet.rpc.kjnodes.com)
* grpc: gitopia-testnet.grpc.kjnodes.com:41090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@gitopia-testnet.rpc.kjnodes.com:41656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@gitopia-testnet.rpc.kjnodes.com:41659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/gitopia-testnet/addrbook.json > $HOME/.gitopia/config/addrbook.json
```

**live-peers** (30)
```bash
peers="f4a2a6b840d1bad6f09c726d51f81d03f41c9ecc@194.146.13.246:656,619a23818cddd40d0b9f57e9754b719da13609bc@65.108.108.52:24656,eaa9978430e55663346eb61312cd5ecc21448b25@38.242.139.153:656,7e0acc9368640587d09fe0b2ef9cba3549b0ba44@65.108.9.164:20556,399d4e19186577b04c23296c4f7ecc53e61080cb@34.143.189.236:26656,f13a4cb3ca18c1de6232e901c8feb209f0945954@65.109.65.248:26656,f1c042fca05e4bfb9a6da1cccaa5108a26ea1e0f@65.108.104.167:28656,8bec864d68a2542233ba37ac94c723fdf0b8e175@45.151.122.136:656,5f045d143cdf9ac78821e848cb10f9c861f5e272@89.117.56.126:24256,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:27036,53b421af01f3260e949d6a9c2dc09e3b1dbf9fb6@109.205.181.30:41656,0150c41282284a9546f8fe0f2531fc6b9d9128a3@65.109.23.114:11356,95203479677e2ab00b1fb0bc1359294d4612e684@85.239.231.0:26656,4cd60a4dd4211d38d948a86a614f1fd8d3d274eb@75.119.153.139:656,cac24f8dcd21095c75c268640f7c756fd43f7cfc@45.94.209.32:26656,cd720fc5703e1e9f65a80b6c5d44b0addecf050b@167.86.67.128:656,b745e0c6a1e0c7ec248ec274cfd038ed4bc4c2cf@65.21.134.202:26356,46dbff2358dddd99acc26c2d2ee5f204ccc347c7@217.76.61.242:26656,6e586e45f8a9d73333d24cd0fa7f64abc8be6d2b@65.108.226.183:11356,247dbc8048be7c024c5f5deee45c18bd2f19bc93@116.203.35.46:36656,007d2419fea80aee707d009af0153f5105c53379@38.242.139.164:656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,9c265cb98c21d6748822ca2bed0accacdd8449db@38.242.205.25:26656,820024c34989e7605d9367847e1fc2d01ad763bd@65.109.92.235:30656,d96adf084c8d6cee7bb318c848560acd19bb564f@194.163.128.179:656,9912d5c8d59b7736b0702b18aeb386efe7e46f3f@164.68.111.239:656,4ed110a5b1ebad62d1e92e8cdabfc9160e2ca4db@65.109.92.148:46656,61188ec3494908fc74f05a02c05cc86e4e587d9e@178.18.241.103:41656,d2975b49708dc92ee3b7da1d72e3eee3119d1d0c@167.86.105.216:656,66f94651fb02f277c90c605a38df549d3c0a9269@75.119.151.217:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gitopia/config/config.toml
```
