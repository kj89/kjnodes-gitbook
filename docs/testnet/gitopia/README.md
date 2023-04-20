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
peers="1f7f58f130ea9c89be44fd60554d5e97da56c395@206.221.181.234:56656,77c344e663bb74eda8beec808792865bb3fa55e1@34.124.222.140:26656,8bec864d68a2542233ba37ac94c723fdf0b8e175@45.151.122.136:656,bd7c6c83af99edf0ee5b857a99997fb9fc8f40a7@65.109.116.204:20556,a8e74ebf033def6fbb28d1b846d7a6c275ad2ef1@65.109.65.163:20556,7e0acc9368640587d09fe0b2ef9cba3549b0ba44@65.108.9.164:20556,975a3ade04fc92d00c7ad59d536506fde46169e7@167.86.96.233:656,bc688b2be879ba5bfa34587e096a9c9a4df2e6d4@45.151.122.116:656,6ea375302fdd319ef64e013f469e286faf739da8@213.239.207.165:20086,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:27036,d82bf877378f15e026fd10abb1a6879df55ed955@188.34.167.80:26656,4cd60a4dd4211d38d948a86a614f1fd8d3d274eb@75.119.153.139:656,399d4e19186577b04c23296c4f7ecc53e61080cb@34.143.189.236:26656,820024c34989e7605d9367847e1fc2d01ad763bd@65.109.92.235:30656,9c265cb98c21d6748822ca2bed0accacdd8449db@38.242.205.25:26656,9bb344d83fc1fafc4bce6b8e4a95b82f37ac4f31@82.208.20.136:26656,006be929170f69951b08c7f839952776e3f7f4b4@109.123.253.67:26656,d2975b49708dc92ee3b7da1d72e3eee3119d1d0c@167.86.105.216:656,f0b8227e40f25eaec0e25b9e91ca199d2d9a1ecb@167.86.94.177:656,06d87468fe35522abb186dd569d3beea579fc74c@5.78.42.204:26656,63381c5528ed8ca93f9ba31008a9630d21b29a97@142.132.152.46:46656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,bbc6a1e115185d5bffcbbf5520dca1c3d626e599@109.123.255.50:26656,247dbc8048be7c024c5f5deee45c18bd2f19bc93@116.203.35.46:36656,b745e0c6a1e0c7ec248ec274cfd038ed4bc4c2cf@65.21.134.202:26356,eaa9978430e55663346eb61312cd5ecc21448b25@38.242.139.153:656,1f0f03a1c845e810e5cfeb0d960639c637d049fe@154.26.131.130:36656,66f94651fb02f277c90c605a38df549d3c0a9269@75.119.151.217:26656,4e0e57bcac8aa2bc3188d5b7845eeee61a61f3f0@194.163.170.165:26656,7da6c90fe420bca73b5274884236134acf49d565@35.168.32.254:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gitopia/config/config.toml
```
