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
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,bd7c6c83af99edf0ee5b857a99997fb9fc8f40a7@65.109.116.204:20556,a8e74ebf033def6fbb28d1b846d7a6c275ad2ef1@65.109.65.163:20556,1f7f58f130ea9c89be44fd60554d5e97da56c395@206.221.181.234:56656,399d4e19186577b04c23296c4f7ecc53e61080cb@34.143.189.236:26656,1f0f03a1c845e810e5cfeb0d960639c637d049fe@154.26.131.130:36656,f0a82f850a0da74c32836b125a52bdfd9a78fdd7@65.108.105.48:11356,943dbf5b8694620c1e0cce336d6a8a3327929c77@65.109.122.105:60656,52ba59360cfc90c8beb1c3704a4c9ed9b38e597d@65.109.65.126:41656,820024c34989e7605d9367847e1fc2d01ad763bd@65.109.92.235:30656,81f9bdd0e1e01390b70df7544b45efdccb52e41c@84.54.23.199:26656,9c265cb98c21d6748822ca2bed0accacdd8449db@38.242.205.25:26656,d2975b49708dc92ee3b7da1d72e3eee3119d1d0c@167.86.105.216:656,f0b8227e40f25eaec0e25b9e91ca199d2d9a1ecb@167.86.94.177:656,2c091dd49fe2a2118339258b087b0655f7991289@45.151.122.167:656,8e20add7ed774bfd8600c628bb8fce87bacb207b@194.163.143.98:26656,95fbdc6d62be17db6688222b15b57d3e795ed07a@167.86.84.102:656,63381c5528ed8ca93f9ba31008a9630d21b29a97@142.132.152.46:46656,b745e0c6a1e0c7ec248ec274cfd038ed4bc4c2cf@65.21.134.202:26356,4e0e57bcac8aa2bc3188d5b7845eeee61a61f3f0@194.163.170.165:26656,4cd60a4dd4211d38d948a86a614f1fd8d3d274eb@75.119.153.139:656,9912d5c8d59b7736b0702b18aeb386efe7e46f3f@164.68.111.239:656,eaa9978430e55663346eb61312cd5ecc21448b25@38.242.139.153:656,70e3f040d7b0cac765bc3f82da7e52cc3ffc3c76@206.81.17.230:656,247dbc8048be7c024c5f5deee45c18bd2f19bc93@116.203.35.46:36656,e59f03376a1388bf6faffcb6ae3ce06476b1f735@65.21.200.54:41656,ac606e28c081c679dc23d9a94c29842be8f8b1f1@45.85.249.133:656,d9b86c9459ac8bb4760d37095732ccd2746aca1f@65.21.131.215:26356,98bdfc67810bf7ac8f5c45b2c677b4bf199eb42e@185.193.67.65:41656,d9d59b442e46f142394fcdf2f246ca8c7b2b7ce9@149.102.146.36:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gitopia/config/config.toml
```
