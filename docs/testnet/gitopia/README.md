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
peers="6ea375302fdd319ef64e013f469e286faf739da8@213.239.207.165:20086,7e0acc9368640587d09fe0b2ef9cba3549b0ba44@65.108.9.164:20556,a8e74ebf033def6fbb28d1b846d7a6c275ad2ef1@65.109.65.163:20556,bd7c6c83af99edf0ee5b857a99997fb9fc8f40a7@65.109.116.204:20556,66f94651fb02f277c90c605a38df549d3c0a9269@75.119.151.217:26656,f4a2a6b840d1bad6f09c726d51f81d03f41c9ecc@194.146.13.246:656,399d4e19186577b04c23296c4f7ecc53e61080cb@34.143.189.236:26656,9645f93ac2b57431a8ca32ac56b0ff63fe9c10ed@144.76.164.139:10656,66116d559390844588c67db54b894779cf00d559@5.9.61.237:41656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:27036,1f0f03a1c845e810e5cfeb0d960639c637d049fe@154.26.131.130:36656,f0b8227e40f25eaec0e25b9e91ca199d2d9a1ecb@167.86.94.177:656,a52dcd34843340a4df6dcb93e8a8d6eb78d796fa@85.10.193.246:26656,b745e0c6a1e0c7ec248ec274cfd038ed4bc4c2cf@65.21.134.202:26356,eaa9978430e55663346eb61312cd5ecc21448b25@38.242.139.153:656,9c265cb98c21d6748822ca2bed0accacdd8449db@38.242.205.25:26656,247dbc8048be7c024c5f5deee45c18bd2f19bc93@116.203.35.46:36656,06d87468fe35522abb186dd569d3beea579fc74c@5.78.42.204:26656,5b1c25f4dff541f77f1532c457f73ca7ee2e4c18@194.163.170.225:26656,4cd60a4dd4211d38d948a86a614f1fd8d3d274eb@75.119.153.139:656,ffb4f7d43d6449c292d4e60c8a48eb3d31c39691@38.242.139.100:656,59a99a10a28baeda8535598acef9abb706ec5dbc@45.85.249.132:656,b10fe01639478f1232aa02a9693b5aaae8dc84bc@144.76.196.121:41656,8bec864d68a2542233ba37ac94c723fdf0b8e175@45.151.122.136:656,0e9f303834a5d1f3be0babd5466725b3609ebc82@65.21.141.246:28656,03073657e8bc5bcf71e7fd8df281ab8dcbc8821a@45.151.122.130:656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,d2975b49708dc92ee3b7da1d72e3eee3119d1d0c@167.86.105.216:656,082e95b5d5351e68dcfb24dff802f9064cfd5a4c@65.109.92.241:51056,7da6c90fe420bca73b5274884236134acf49d565@35.168.32.254:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gitopia/config/config.toml
```
