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
peers="0c31077af45cb4f0424e58c91b0a917c36a90fd9@65.108.195.235:16656,59a99a10a28baeda8535598acef9abb706ec5dbc@45.85.249.132:656,7e0acc9368640587d09fe0b2ef9cba3549b0ba44@65.108.9.164:20556,a8e74ebf033def6fbb28d1b846d7a6c275ad2ef1@65.109.65.163:20556,59cdd2944de1d9eccdbb013123f2dc8b6a5770f8@178.18.254.33:26656,bd7c6c83af99edf0ee5b857a99997fb9fc8f40a7@65.109.116.204:20556,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:27036,0e9f303834a5d1f3be0babd5466725b3609ebc82@65.21.141.246:28656,399d4e19186577b04c23296c4f7ecc53e61080cb@34.143.189.236:26656,f13a4cb3ca18c1de6232e901c8feb209f0945954@65.109.65.248:26656,ed177ff3cf334df1a6c190438b0c7b5dd64b423a@45.151.122.140:656,46dbff2358dddd99acc26c2d2ee5f204ccc347c7@217.76.61.242:26656,1f0f03a1c845e810e5cfeb0d960639c637d049fe@154.26.131.130:36656,4cd60a4dd4211d38d948a86a614f1fd8d3d274eb@75.119.153.139:656,a6f4fd8efe8a575a15e25652ecebce3fa1ed62a0@213.239.217.52:35656,3b0956b482f89b361dd350f1c6b3743096897446@65.108.124.219:35656,cf97c77d4f28c3bd619efe10f4f9aa404f246853@161.97.154.51:26656,b745e0c6a1e0c7ec248ec274cfd038ed4bc4c2cf@65.21.134.202:26356,66f94651fb02f277c90c605a38df549d3c0a9269@75.119.151.217:26656,1cf3826ccd9a24caa549cbea061446716858133e@154.26.130.95:36656,38b327ce97c670014d52701e3a26eaa16fee1f7f@149.102.151.204:26656,98bdfc67810bf7ac8f5c45b2c677b4bf199eb42e@185.193.67.65:41656,1989ced6b71ce676a5ab4d0586d85e38fd41fbd2@136.243.88.91:7070,f0b8227e40f25eaec0e25b9e91ca199d2d9a1ecb@167.86.94.177:656,7d39b009b329fc1a36457e814378872e67aef5c8@84.46.252.93:26656,bc688b2be879ba5bfa34587e096a9c9a4df2e6d4@45.151.122.116:656,820024c34989e7605d9367847e1fc2d01ad763bd@65.109.92.235:30656,c84906b19dc7dc7bda94ab2167d4b0af64a28b49@45.151.122.191:656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,4e0e57bcac8aa2bc3188d5b7845eeee61a61f3f0@194.163.170.165:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gitopia/config/config.toml
```
