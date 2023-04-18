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
peers="f1a47d469460fb0a70b12d7739afbc0bf78eadda@78.47.195.69:656,0c31077af45cb4f0424e58c91b0a917c36a90fd9@65.108.195.235:16656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,a8e74ebf033def6fbb28d1b846d7a6c275ad2ef1@65.109.65.163:20556,7e0acc9368640587d09fe0b2ef9cba3549b0ba44@65.108.9.164:20556,bd7c6c83af99edf0ee5b857a99997fb9fc8f40a7@65.109.116.204:20556,7d819fa869f7c5b42c2c7a9538e1a9e7a52cfdee@65.108.226.26:24656,399d4e19186577b04c23296c4f7ecc53e61080cb@34.143.189.236:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:27036,8bec864d68a2542233ba37ac94c723fdf0b8e175@45.151.122.136:656,f9b892ea2e8ed8aa83f7b98e7e47371c23b01924@213.239.207.175:36656,59a99a10a28baeda8535598acef9abb706ec5dbc@45.85.249.132:656,f0b8227e40f25eaec0e25b9e91ca199d2d9a1ecb@167.86.94.177:656,b745e0c6a1e0c7ec248ec274cfd038ed4bc4c2cf@65.21.134.202:26356,f0a82f850a0da74c32836b125a52bdfd9a78fdd7@65.108.105.48:11356,53b421af01f3260e949d6a9c2dc09e3b1dbf9fb6@109.205.181.30:41656,66f94651fb02f277c90c605a38df549d3c0a9269@75.119.151.217:26656,9912d5c8d59b7736b0702b18aeb386efe7e46f3f@164.68.111.239:656,247dbc8048be7c024c5f5deee45c18bd2f19bc93@116.203.35.46:36656,52a2fb0aa22551b1ef0155824228924d41c1daa6@85.239.230.213:26656,46dbff2358dddd99acc26c2d2ee5f204ccc347c7@217.76.61.242:26656,eaa9978430e55663346eb61312cd5ecc21448b25@38.242.139.153:656,1b4815a4a57422e8dfdbe2521d4012ac5f23dc83@75.119.140.73:41656,1f0f03a1c845e810e5cfeb0d960639c637d049fe@154.26.131.130:36656,95fbdc6d62be17db6688222b15b57d3e795ed07a@167.86.84.102:656,4cd60a4dd4211d38d948a86a614f1fd8d3d274eb@75.119.153.139:656,0150c41282284a9546f8fe0f2531fc6b9d9128a3@65.109.23.114:11356,4ed110a5b1ebad62d1e92e8cdabfc9160e2ca4db@65.109.92.148:46656,54756019bbc900b882b302786222978928d96d9e@65.109.65.210:41656,820024c34989e7605d9367847e1fc2d01ad763bd@65.109.92.235:30656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gitopia/config/config.toml
```
