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
peers="619a23818cddd40d0b9f57e9754b719da13609bc@65.108.108.52:24656,ac606e28c081c679dc23d9a94c29842be8f8b1f1@45.85.249.133:656,52098a0fdd0dc566615ad37492019d252635bdda@45.85.249.131:656,bd7c6c83af99edf0ee5b857a99997fb9fc8f40a7@65.109.116.204:20556,a8e74ebf033def6fbb28d1b846d7a6c275ad2ef1@65.109.65.163:20556,d9d59b442e46f142394fcdf2f246ca8c7b2b7ce9@149.102.146.36:26656,399d4e19186577b04c23296c4f7ecc53e61080cb@34.143.189.236:26656,f13a4cb3ca18c1de6232e901c8feb209f0945954@65.109.65.248:26656,f3f72cf59352deed9a59eecef4884e12710c2177@65.109.85.225:7040,eaa9978430e55663346eb61312cd5ecc21448b25@38.242.139.153:656,f0b8227e40f25eaec0e25b9e91ca199d2d9a1ecb@167.86.94.177:656,8f5935761a8bc93c7eaf9fc8bb29b4b184269447@46.8.210.144:26656,5c74fe6868cda2003926c0a6299c9cebec5c4d1a@65.21.239.60:41656,314ee8896c9f9e39450dc25623f8019cf316ed60@38.242.135.124:26656,ee598d227438a0c68bea18ec1e1ba606c6be4cd3@193.34.217.174:26656,c84906b19dc7dc7bda94ab2167d4b0af64a28b49@45.151.122.191:656,88ce80cb509fd973e06a552e1a5075d1292545d6@46.166.172.226:26656,1cf3826ccd9a24caa549cbea061446716858133e@154.26.130.95:36656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,8bec864d68a2542233ba37ac94c723fdf0b8e175@45.151.122.136:656,59a99a10a28baeda8535598acef9abb706ec5dbc@45.85.249.132:656,0c31077af45cb4f0424e58c91b0a917c36a90fd9@65.108.195.235:16656,820024c34989e7605d9367847e1fc2d01ad763bd@65.109.92.235:30656,81f9bdd0e1e01390b70df7544b45efdccb52e41c@84.54.23.199:26656,247dbc8048be7c024c5f5deee45c18bd2f19bc93@116.203.35.46:36656,6e586e45f8a9d73333d24cd0fa7f64abc8be6d2b@65.108.226.183:11356,4e0e57bcac8aa2bc3188d5b7845eeee61a61f3f0@194.163.170.165:26656,1f0f03a1c845e810e5cfeb0d960639c637d049fe@154.26.131.130:36656,d9b86c9459ac8bb4760d37095732ccd2746aca1f@65.21.131.215:26356,7da6c90fe420bca73b5274884236134acf49d565@35.168.32.254:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gitopia/config/config.toml
```
