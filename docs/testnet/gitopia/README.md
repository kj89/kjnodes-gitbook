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
peers="a6f4fd8efe8a575a15e25652ecebce3fa1ed62a0@213.239.217.52:35656,d9b86c9459ac8bb4760d37095732ccd2746aca1f@65.21.131.215:26356,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,bd7c6c83af99edf0ee5b857a99997fb9fc8f40a7@65.109.116.204:20556,52098a0fdd0dc566615ad37492019d252635bdda@45.85.249.131:656,a8e74ebf033def6fbb28d1b846d7a6c275ad2ef1@65.109.65.163:20556,7e0acc9368640587d09fe0b2ef9cba3549b0ba44@65.108.9.164:20556,53b421af01f3260e949d6a9c2dc09e3b1dbf9fb6@109.205.181.30:41656,820024c34989e7605d9367847e1fc2d01ad763bd@65.109.92.235:30656,9c265cb98c21d6748822ca2bed0accacdd8449db@38.242.205.25:26656,6e586e45f8a9d73333d24cd0fa7f64abc8be6d2b@65.108.226.183:11356,082e95b5d5351e68dcfb24dff802f9064cfd5a4c@65.109.92.241:51056,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:27036,f0b8227e40f25eaec0e25b9e91ca199d2d9a1ecb@167.86.94.177:656,52ba59360cfc90c8beb1c3704a4c9ed9b38e597d@65.109.65.126:41656,1f0f03a1c845e810e5cfeb0d960639c637d049fe@154.26.131.130:36656,399d4e19186577b04c23296c4f7ecc53e61080cb@34.143.189.236:26656,3e757ff8f7388393af67809a5646142965bc6808@80.65.211.229:656,b745e0c6a1e0c7ec248ec274cfd038ed4bc4c2cf@65.21.134.202:26356,06d87468fe35522abb186dd569d3beea579fc74c@5.78.42.204:26656,4e0e57bcac8aa2bc3188d5b7845eeee61a61f3f0@194.163.170.165:26656,6ea375302fdd319ef64e013f469e286faf739da8@213.239.207.165:20086,943dbf5b8694620c1e0cce336d6a8a3327929c77@65.109.122.105:60656,5c74fe6868cda2003926c0a6299c9cebec5c4d1a@65.21.239.60:41656,d9d59b442e46f142394fcdf2f246ca8c7b2b7ce9@149.102.146.36:26656,007d2419fea80aee707d009af0153f5105c53379@38.242.139.164:656,cf97c77d4f28c3bd619efe10f4f9aa404f246853@161.97.154.51:26656,4cd60a4dd4211d38d948a86a614f1fd8d3d274eb@75.119.153.139:656,8bec864d68a2542233ba37ac94c723fdf0b8e175@45.151.122.136:656,eaa9978430e55663346eb61312cd5ecc21448b25@38.242.139.153:656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gitopia/config/config.toml
```
