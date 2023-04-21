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
peers="f13a4cb3ca18c1de6232e901c8feb209f0945954@65.109.65.248:26656,9cd6d2477d278ef6ccffa5cc4e22fd0d9489cd23@85.10.199.157:34656,a8e74ebf033def6fbb28d1b846d7a6c275ad2ef1@65.109.65.163:20556,bd7c6c83af99edf0ee5b857a99997fb9fc8f40a7@65.109.116.204:20556,7e0acc9368640587d09fe0b2ef9cba3549b0ba44@65.108.9.164:20556,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:27036,f0b8227e40f25eaec0e25b9e91ca199d2d9a1ecb@167.86.94.177:656,399d4e19186577b04c23296c4f7ecc53e61080cb@34.143.189.236:26656,619a23818cddd40d0b9f57e9754b719da13609bc@65.108.108.52:24656,5f4aee494e44d65f31753d7122f074f27b3ed8a2@95.216.162.25:656,ed177ff3cf334df1a6c190438b0c7b5dd64b423a@45.151.122.140:656,37677351ed74a5ced46a99217d19e30d5bcacc1d@5.75.147.138:26656,4cd60a4dd4211d38d948a86a614f1fd8d3d274eb@75.119.153.139:656,03073657e8bc5bcf71e7fd8df281ab8dcbc8821a@45.151.122.130:656,975a3ade04fc92d00c7ad59d536506fde46169e7@167.86.96.233:656,52098a0fdd0dc566615ad37492019d252635bdda@45.85.249.131:656,b745e0c6a1e0c7ec248ec274cfd038ed4bc4c2cf@65.21.134.202:26356,1f0f03a1c845e810e5cfeb0d960639c637d049fe@154.26.131.130:36656,eaa9978430e55663346eb61312cd5ecc21448b25@38.242.139.153:656,247dbc8048be7c024c5f5deee45c18bd2f19bc93@116.203.35.46:36656,1f7f58f130ea9c89be44fd60554d5e97da56c395@206.221.181.234:56656,820024c34989e7605d9367847e1fc2d01ad763bd@65.109.92.235:30656,9c265cb98c21d6748822ca2bed0accacdd8449db@38.242.205.25:26656,ee812a11525cf7e2de4bd63e66aed8b8de337902@38.242.235.199:41656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,59a99a10a28baeda8535598acef9abb706ec5dbc@45.85.249.132:656,06d87468fe35522abb186dd569d3beea579fc74c@5.78.42.204:26656,6ea375302fdd319ef64e013f469e286faf739da8@213.239.207.165:20086,95fbdc6d62be17db6688222b15b57d3e795ed07a@167.86.84.102:656,7da6c90fe420bca73b5274884236134acf49d565@35.168.32.254:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gitopia/config/config.toml
```
