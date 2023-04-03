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
peers="5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:27036,f3f72cf59352deed9a59eecef4884e12710c2177@65.109.85.225:7040,4cd60a4dd4211d38d948a86a614f1fd8d3d274eb@75.119.153.139:656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,b745e0c6a1e0c7ec248ec274cfd038ed4bc4c2cf@65.21.134.202:26356,f13a4cb3ca18c1de6232e901c8feb209f0945954@65.109.65.248:26656,399d4e19186577b04c23296c4f7ecc53e61080cb@34.143.189.236:26656,6b09dc9b3722ffa4d4da52ae3efee0af8afa72a0@65.109.90.171:26656,f1a47d469460fb0a70b12d7739afbc0bf78eadda@78.47.195.69:656,4e0e57bcac8aa2bc3188d5b7845eeee61a61f3f0@194.163.170.165:26656,314ee8896c9f9e39450dc25623f8019cf316ed60@38.242.135.124:26656,0eb70bf5e2403694109f9bba184570074c2dfdd5@38.242.235.255:26656,9bb344d83fc1fafc4bce6b8e4a95b82f37ac4f31@82.208.20.136:26656,63381c5528ed8ca93f9ba31008a9630d21b29a97@142.132.152.46:46656,92f5cee77d8c1a4e59c60c61ab56c6476fb0a72b@185.205.246.202:41656,bc688b2be879ba5bfa34587e096a9c9a4df2e6d4@45.151.122.116:656,8bec864d68a2542233ba37ac94c723fdf0b8e175@45.151.122.136:656,9912d5c8d59b7736b0702b18aeb386efe7e46f3f@164.68.111.239:656,eaa9978430e55663346eb61312cd5ecc21448b25@38.242.139.153:656,34d3ee88e9f3d677ca93c084e701d43e188f68c5@65.108.224.156:26656,3e5ba61e8481c6c71d3f2cc022dd6671ed7cacf8@65.21.170.3:41656,24453bdf119b17550849851d69c50cde7b140460@84.46.253.3:41656,9c265cb98c21d6748822ca2bed0accacdd8449db@38.242.205.25:26656,c84906b19dc7dc7bda94ab2167d4b0af64a28b49@45.151.122.191:656,1cf3826ccd9a24caa549cbea061446716858133e@154.26.130.95:36656,6c4bb3da218ec0ec031a546080b6b4db3fb5ac3d@82.208.21.174:26656,a6f4fd8efe8a575a15e25652ecebce3fa1ed62a0@213.239.217.52:35656,bbc6a1e115185d5bffcbbf5520dca1c3d626e599@109.123.255.50:26656,f026faf0dfc8a19f8029c6ec08d1e8454a2c9475@149.102.133.56:26656,7da6c90fe420bca73b5274884236134acf49d565@35.168.32.254:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gitopia/config/config.toml
```
