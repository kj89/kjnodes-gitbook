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

**live-peers** (29)
```bash
peers="5c45e8920c5094827ec5afaca9ab469aaa0b4eaf@65.109.88.254:28656,6e586e45f8a9d73333d24cd0fa7f64abc8be6d2b@65.108.226.183:11356,15bb9edc16710d321163e7ef8b9a44959dd7e657@65.108.126.46:30656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,7e0acc9368640587d09fe0b2ef9cba3549b0ba44@65.108.9.164:20556,292c099fc654a1331d3b62a1b939f867b62ef434@45.85.147.242:656,edd8102eaa14a940cef0ac938849c166f17b13a7@86.32.74.154:26656,e59f03376a1388bf6faffcb6ae3ce06476b1f735@65.21.200.54:41656,9912d5c8d59b7736b0702b18aeb386efe7e46f3f@164.68.111.239:656,8e20add7ed774bfd8600c628bb8fce87bacb207b@194.163.143.98:26656,03073657e8bc5bcf71e7fd8df281ab8dcbc8821a@45.151.122.130:656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:27036,f3f72cf59352deed9a59eecef4884e12710c2177@65.109.85.225:7040,619a23818cddd40d0b9f57e9754b719da13609bc@65.108.108.52:24656,399d4e19186577b04c23296c4f7ecc53e61080cb@34.143.189.236:26656,4e0e57bcac8aa2bc3188d5b7845eeee61a61f3f0@194.163.170.165:26656,bc688b2be879ba5bfa34587e096a9c9a4df2e6d4@45.151.122.116:656,f0b8227e40f25eaec0e25b9e91ca199d2d9a1ecb@167.86.94.177:656,007d2419fea80aee707d009af0153f5105c53379@38.242.139.164:656,9bb344d83fc1fafc4bce6b8e4a95b82f37ac4f31@82.208.20.136:26656,9c265cb98c21d6748822ca2bed0accacdd8449db@38.242.205.25:26656,1f0f03a1c845e810e5cfeb0d960639c637d049fe@154.26.131.130:36656,6ea375302fdd319ef64e013f469e286faf739da8@213.239.207.165:20086,b745e0c6a1e0c7ec248ec274cfd038ed4bc4c2cf@65.21.134.202:26356,81f9bdd0e1e01390b70df7544b45efdccb52e41c@84.54.23.199:26656,082e95b5d5351e68dcfb24dff802f9064cfd5a4c@65.109.92.241:51056,7da6c90fe420bca73b5274884236134acf49d565@35.168.32.254:26656,4cd60a4dd4211d38d948a86a614f1fd8d3d274eb@75.119.153.139:656,1cf3826ccd9a24caa549cbea061446716858133e@154.26.130.95:36656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gitopia/config/config.toml
```
