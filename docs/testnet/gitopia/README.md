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
peers="0c31077af45cb4f0424e58c91b0a917c36a90fd9@65.108.195.235:16656,f9b892ea2e8ed8aa83f7b98e7e47371c23b01924@213.239.207.175:36656,397cf4db87961e3a92f54b460300fc01d4dfa8f4@142.132.202.50:37656,81f9bdd0e1e01390b70df7544b45efdccb52e41c@84.54.23.199:26656,5b1c25f4dff541f77f1532c457f73ca7ee2e4c18@194.163.170.225:26656,bd7c6c83af99edf0ee5b857a99997fb9fc8f40a7@65.109.116.204:20556,7e0acc9368640587d09fe0b2ef9cba3549b0ba44@65.108.9.164:20556,a8e74ebf033def6fbb28d1b846d7a6c275ad2ef1@65.109.65.163:20556,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:27036,7da6c90fe420bca73b5274884236134acf49d565@35.168.32.254:26656,820024c34989e7605d9367847e1fc2d01ad763bd@65.109.92.235:30656,399d4e19186577b04c23296c4f7ecc53e61080cb@34.143.189.236:26656,eaa9978430e55663346eb61312cd5ecc21448b25@38.242.139.153:656,b745e0c6a1e0c7ec248ec274cfd038ed4bc4c2cf@65.21.134.202:26356,4cd60a4dd4211d38d948a86a614f1fd8d3d274eb@75.119.153.139:656,9c265cb98c21d6748822ca2bed0accacdd8449db@38.242.205.25:26656,88ce80cb509fd973e06a552e1a5075d1292545d6@46.166.172.226:26656,1f0f03a1c845e810e5cfeb0d960639c637d049fe@154.26.131.130:36656,a6f4fd8efe8a575a15e25652ecebce3fa1ed62a0@213.239.217.52:35656,d9d59b442e46f142394fcdf2f246ca8c7b2b7ce9@149.102.146.36:26656,9cd6d2477d278ef6ccffa5cc4e22fd0d9489cd23@85.10.199.157:34656,f0b8227e40f25eaec0e25b9e91ca199d2d9a1ecb@167.86.94.177:656,247dbc8048be7c024c5f5deee45c18bd2f19bc93@116.203.35.46:36656,023c6a86fbd8b8368503c92bd612a8c0379a26e5@194.146.13.251:656,53b421af01f3260e949d6a9c2dc09e3b1dbf9fb6@109.205.181.30:41656,f3f72cf59352deed9a59eecef4884e12710c2177@65.109.85.225:7040,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,2236a75a7557d8633d06ac6f036c1b47c1fd1598@149.102.158.166:41656,c2beb74ebaf76137702732f6076c9a319bf15262@159.69.72.247:41656,52098a0fdd0dc566615ad37492019d252635bdda@45.85.249.131:656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gitopia/config/config.toml
```
