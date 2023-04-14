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
peers="4e4f87cfa1993f4f3f7645c41f469987cafdf960@85.10.202.135:12656,1cf3826ccd9a24caa549cbea061446716858133e@154.26.130.95:36656,3e5ba61e8481c6c71d3f2cc022dd6671ed7cacf8@65.21.170.3:41656,95203479677e2ab00b1fb0bc1359294d4612e684@85.239.231.0:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,7e0acc9368640587d09fe0b2ef9cba3549b0ba44@65.108.9.164:20556,0c31077af45cb4f0424e58c91b0a917c36a90fd9@65.108.195.235:16656,b745e0c6a1e0c7ec248ec274cfd038ed4bc4c2cf@65.21.134.202:26356,9bb344d83fc1fafc4bce6b8e4a95b82f37ac4f31@82.208.20.136:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:27036,399d4e19186577b04c23296c4f7ecc53e61080cb@34.143.189.236:26656,9c265cb98c21d6748822ca2bed0accacdd8449db@38.242.205.25:26656,2236a75a7557d8633d06ac6f036c1b47c1fd1598@149.102.158.166:41656,eaa9978430e55663346eb61312cd5ecc21448b25@38.242.139.153:656,46dbff2358dddd99acc26c2d2ee5f204ccc347c7@217.76.61.242:26656,deca8c5aed2d1e617789d80927394a1d4d1c7360@149.102.146.123:26656,1f0f03a1c845e810e5cfeb0d960639c637d049fe@154.26.131.130:36656,820024c34989e7605d9367847e1fc2d01ad763bd@65.109.92.235:30656,03073657e8bc5bcf71e7fd8df281ab8dcbc8821a@45.151.122.130:656,63381c5528ed8ca93f9ba31008a9630d21b29a97@142.132.152.46:46656,9912d5c8d59b7736b0702b18aeb386efe7e46f3f@164.68.111.239:656,8bec864d68a2542233ba37ac94c723fdf0b8e175@45.151.122.136:656,f2bca9113807369ff96cfed3639bc6d65467e76d@149.102.159.81:26656,ee812a11525cf7e2de4bd63e66aed8b8de337902@38.242.235.199:41656,082e95b5d5351e68dcfb24dff802f9064cfd5a4c@65.109.92.241:51056,6ea375302fdd319ef64e013f469e286faf739da8@213.239.207.165:20086,f0b8227e40f25eaec0e25b9e91ca199d2d9a1ecb@167.86.94.177:656,4cd60a4dd4211d38d948a86a614f1fd8d3d274eb@75.119.153.139:656,8f5935761a8bc93c7eaf9fc8bb29b4b184269447@46.8.210.144:26656,7da6c90fe420bca73b5274884236134acf49d565@35.168.32.254:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gitopia/config/config.toml
```
