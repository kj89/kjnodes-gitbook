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
peers="8bec864d68a2542233ba37ac94c723fdf0b8e175@45.151.122.136:656,7e0acc9368640587d09fe0b2ef9cba3549b0ba44@65.108.9.164:20556,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,bd7c6c83af99edf0ee5b857a99997fb9fc8f40a7@65.109.116.204:20556,a8e74ebf033def6fbb28d1b846d7a6c275ad2ef1@65.109.65.163:20556,1f0f03a1c845e810e5cfeb0d960639c637d049fe@154.26.131.130:36656,63381c5528ed8ca93f9ba31008a9630d21b29a97@142.132.152.46:46656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:27036,f9b892ea2e8ed8aa83f7b98e7e47371c23b01924@213.239.207.175:36656,95fbdc6d62be17db6688222b15b57d3e795ed07a@167.86.84.102:656,9cd6d2477d278ef6ccffa5cc4e22fd0d9489cd23@85.10.199.157:34656,5c74fe6868cda2003926c0a6299c9cebec5c4d1a@65.21.239.60:41656,399d4e19186577b04c23296c4f7ecc53e61080cb@34.143.189.236:26656,9912d5c8d59b7736b0702b18aeb386efe7e46f3f@164.68.111.239:656,b745e0c6a1e0c7ec248ec274cfd038ed4bc4c2cf@65.21.134.202:26356,4cd60a4dd4211d38d948a86a614f1fd8d3d274eb@75.119.153.139:656,9c265cb98c21d6748822ca2bed0accacdd8449db@38.242.205.25:26656,5f4aee494e44d65f31753d7122f074f27b3ed8a2@95.216.162.25:656,59a99a10a28baeda8535598acef9abb706ec5dbc@45.85.249.132:656,314ee8896c9f9e39450dc25623f8019cf316ed60@38.242.135.124:26656,943dbf5b8694620c1e0cce336d6a8a3327929c77@65.109.122.105:60656,820024c34989e7605d9367847e1fc2d01ad763bd@65.109.92.235:30656,247dbc8048be7c024c5f5deee45c18bd2f19bc93@116.203.35.46:36656,d2975b49708dc92ee3b7da1d72e3eee3119d1d0c@167.86.105.216:656,f0a82f850a0da74c32836b125a52bdfd9a78fdd7@65.108.105.48:11356,f0b8227e40f25eaec0e25b9e91ca199d2d9a1ecb@167.86.94.177:656,8e20add7ed774bfd8600c628bb8fce87bacb207b@194.163.143.98:26656,d9d59b442e46f142394fcdf2f246ca8c7b2b7ce9@149.102.146.36:26656,bbc6a1e115185d5bffcbbf5520dca1c3d626e599@109.123.255.50:26656,8f5935761a8bc93c7eaf9fc8bb29b4b184269447@46.8.210.144:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gitopia/config/config.toml
```
