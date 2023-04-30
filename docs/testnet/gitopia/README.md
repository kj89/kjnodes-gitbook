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
peers="eccdf1d5bf33bc1733838562b4d4a4a45869c3a8@135.181.183.93:41656,0e9f303834a5d1f3be0babd5466725b3609ebc82@65.21.141.246:28656,9c265cb98c21d6748822ca2bed0accacdd8449db@38.242.205.25:26656,4e0e57bcac8aa2bc3188d5b7845eeee61a61f3f0@194.163.170.165:26656,bd7c6c83af99edf0ee5b857a99997fb9fc8f40a7@65.109.116.204:20556,a8e74ebf033def6fbb28d1b846d7a6c275ad2ef1@65.109.65.163:20556,f9b892ea2e8ed8aa83f7b98e7e47371c23b01924@213.239.207.175:36656,4cd60a4dd4211d38d948a86a614f1fd8d3d274eb@75.119.153.139:656,399d4e19186577b04c23296c4f7ecc53e61080cb@34.143.189.236:26656,5b1075a6a1073168e2b44b4ceceb02218ba7bab1@185.211.6.207:26656,b745e0c6a1e0c7ec248ec274cfd038ed4bc4c2cf@65.21.134.202:26356,59a99a10a28baeda8535598acef9abb706ec5dbc@45.85.249.132:656,81f9bdd0e1e01390b70df7544b45efdccb52e41c@84.54.23.199:26656,95fbdc6d62be17db6688222b15b57d3e795ed07a@167.86.84.102:656,bbc6a1e115185d5bffcbbf5520dca1c3d626e599@109.123.255.50:26656,7da6c90fe420bca73b5274884236134acf49d565@35.168.32.254:26656,1989ced6b71ce676a5ab4d0586d85e38fd41fbd2@136.243.88.91:7070,df5b61e51ab2f6c3bf1f3c387ba1586a84b41b25@135.181.116.109:27956,d9d59b442e46f142394fcdf2f246ca8c7b2b7ce9@149.102.146.36:26656,eaa9978430e55663346eb61312cd5ecc21448b25@38.242.139.153:656,e500fe5b991d9d391e22a9b91b1cbc66b1d30aee@90.230.199.228:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,98bdfc67810bf7ac8f5c45b2c677b4bf199eb42e@185.193.67.65:41656,d318a60a25b7a84322a8083709ff8e8bbe82ddb7@65.108.13.154:26656,8d45cada398e1035e220857a84021fabfa723248@2.58.82.21:26656,ef8bf45c54182573c9a852e8181f43838e198467@185.245.183.253:41656,820024c34989e7605d9367847e1fc2d01ad763bd@65.109.92.235:30656,1f0f03a1c845e810e5cfeb0d960639c637d049fe@154.26.131.130:36656,7d39b009b329fc1a36457e814378872e67aef5c8@84.46.252.93:26656,e28ab99ea7db98c5dfd7225d1623959f27805d93@34.143.211.179:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gitopia/config/config.toml
```
