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
peers="f9b892ea2e8ed8aa83f7b98e7e47371c23b01924@213.239.207.175:36656,f1c042fca05e4bfb9a6da1cccaa5108a26ea1e0f@65.108.104.167:28656,6b09dc9b3722ffa4d4da52ae3efee0af8afa72a0@65.109.90.171:26656,619a23818cddd40d0b9f57e9754b719da13609bc@65.108.108.52:24656,81f9bdd0e1e01390b70df7544b45efdccb52e41c@84.54.23.199:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,7e0acc9368640587d09fe0b2ef9cba3549b0ba44@65.108.9.164:20556,a8e74ebf033def6fbb28d1b846d7a6c275ad2ef1@65.109.65.163:20556,bd7c6c83af99edf0ee5b857a99997fb9fc8f40a7@65.109.116.204:20556,399d4e19186577b04c23296c4f7ecc53e61080cb@34.143.189.236:26656,9c265cb98c21d6748822ca2bed0accacdd8449db@38.242.205.25:26656,820024c34989e7605d9367847e1fc2d01ad763bd@65.109.92.235:30656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:27036,0e9f303834a5d1f3be0babd5466725b3609ebc82@65.21.141.246:28656,7d39b009b329fc1a36457e814378872e67aef5c8@84.46.252.93:26656,d318a60a25b7a84322a8083709ff8e8bbe82ddb7@65.108.13.154:26656,53b421af01f3260e949d6a9c2dc09e3b1dbf9fb6@109.205.181.30:41656,4cd60a4dd4211d38d948a86a614f1fd8d3d274eb@75.119.153.139:656,52098a0fdd0dc566615ad37492019d252635bdda@45.85.249.131:656,247dbc8048be7c024c5f5deee45c18bd2f19bc93@116.203.35.46:36656,b745e0c6a1e0c7ec248ec274cfd038ed4bc4c2cf@65.21.134.202:26356,cf97c77d4f28c3bd619efe10f4f9aa404f246853@161.97.154.51:26656,1f0f03a1c845e810e5cfeb0d960639c637d049fe@154.26.131.130:36656,f0b8227e40f25eaec0e25b9e91ca199d2d9a1ecb@167.86.94.177:656,d9b86c9459ac8bb4760d37095732ccd2746aca1f@65.21.131.215:26356,59cdd2944de1d9eccdbb013123f2dc8b6a5770f8@178.18.254.33:26656,37c3d29df83da59e5a258d413e2f89365ab05711@85.239.243.12:656,9cd6d2477d278ef6ccffa5cc4e22fd0d9489cd23@85.10.199.157:34656,9912d5c8d59b7736b0702b18aeb386efe7e46f3f@164.68.111.239:656,7da6c90fe420bca73b5274884236134acf49d565@35.168.32.254:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gitopia/config/config.toml
```
