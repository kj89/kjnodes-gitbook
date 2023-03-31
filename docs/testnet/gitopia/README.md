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
peers="c2beb74ebaf76137702732f6076c9a319bf15262@159.69.72.247:41656,f1a47d469460fb0a70b12d7739afbc0bf78eadda@78.47.195.69:656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,1989ced6b71ce676a5ab4d0586d85e38fd41fbd2@136.243.88.91:7070,b745e0c6a1e0c7ec248ec274cfd038ed4bc4c2cf@65.21.134.202:26356,5f4aee494e44d65f31753d7122f074f27b3ed8a2@95.216.162.25:656,4e0e57bcac8aa2bc3188d5b7845eeee61a61f3f0@194.163.170.165:26656,7d819fa869f7c5b42c2c7a9538e1a9e7a52cfdee@65.108.226.26:24656,0c31077af45cb4f0424e58c91b0a917c36a90fd9@65.108.195.235:16656,9c265cb98c21d6748822ca2bed0accacdd8449db@38.242.205.25:26656,399d4e19186577b04c23296c4f7ecc53e61080cb@34.143.189.236:26656,f0b8227e40f25eaec0e25b9e91ca199d2d9a1ecb@167.86.94.177:656,eaa9978430e55663346eb61312cd5ecc21448b25@38.242.139.153:656,9bb344d83fc1fafc4bce6b8e4a95b82f37ac4f31@82.208.20.136:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:27036,8bec864d68a2542233ba37ac94c723fdf0b8e175@45.151.122.136:656,0e9f303834a5d1f3be0babd5466725b3609ebc82@65.21.141.246:28656,d2975b49708dc92ee3b7da1d72e3eee3119d1d0c@167.86.105.216:656,98bdfc67810bf7ac8f5c45b2c677b4bf199eb42e@185.193.67.65:41656,95fbdc6d62be17db6688222b15b57d3e795ed07a@167.86.84.102:656,bc688b2be879ba5bfa34587e096a9c9a4df2e6d4@45.151.122.116:656,955c997a67a82cbd005e5b2b7010a1de3ac54355@38.242.241.74:26656,007d2419fea80aee707d009af0153f5105c53379@38.242.139.164:656,971c22cfb2a8fee7e6b5b7fb125cc9551f3b5e60@65.109.106.91:16656,1f0f03a1c845e810e5cfeb0d960639c637d049fe@154.26.131.130:36656,4ed110a5b1ebad62d1e92e8cdabfc9160e2ca4db@65.109.92.148:46656,81f9bdd0e1e01390b70df7544b45efdccb52e41c@84.54.23.199:26656,24453bdf119b17550849851d69c50cde7b140460@84.46.253.3:41656,f9b892ea2e8ed8aa83f7b98e7e47371c23b01924@213.239.207.175:36656,77c344e663bb74eda8beec808792865bb3fa55e1@34.124.167.111:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gitopia/config/config.toml
```
