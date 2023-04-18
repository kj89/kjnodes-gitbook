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
peers="6ea375302fdd319ef64e013f469e286faf739da8@213.239.207.165:20086,619a23818cddd40d0b9f57e9754b719da13609bc@65.108.108.52:24656,8bec864d68a2542233ba37ac94c723fdf0b8e175@45.151.122.136:656,a8e74ebf033def6fbb28d1b846d7a6c275ad2ef1@65.109.65.163:20556,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,bd7c6c83af99edf0ee5b857a99997fb9fc8f40a7@65.109.116.204:20556,f2bca9113807369ff96cfed3639bc6d65467e76d@149.102.159.81:26656,7e0acc9368640587d09fe0b2ef9cba3549b0ba44@65.108.9.164:20556,3e5ba61e8481c6c71d3f2cc022dd6671ed7cacf8@65.21.170.3:41656,f0b8227e40f25eaec0e25b9e91ca199d2d9a1ecb@167.86.94.177:656,1f0f03a1c845e810e5cfeb0d960639c637d049fe@154.26.131.130:36656,c84906b19dc7dc7bda94ab2167d4b0af64a28b49@45.151.122.191:656,1cf3826ccd9a24caa549cbea061446716858133e@154.26.130.95:36656,b745e0c6a1e0c7ec248ec274cfd038ed4bc4c2cf@65.21.134.202:26356,d9d59b442e46f142394fcdf2f246ca8c7b2b7ce9@149.102.146.36:26656,399d4e19186577b04c23296c4f7ecc53e61080cb@34.143.189.236:26656,59cdd2944de1d9eccdbb013123f2dc8b6a5770f8@178.18.254.33:26656,ef8bf45c54182573c9a852e8181f43838e198467@185.245.183.253:41656,93c4c73375b5f52020e7e7bd3f901ee28f07e6b7@109.123.243.66:41656,397cf4db87961e3a92f54b460300fc01d4dfa8f4@142.132.202.50:37656,006be929170f69951b08c7f839952776e3f7f4b4@109.123.253.67:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:27036,9912d5c8d59b7736b0702b18aeb386efe7e46f3f@164.68.111.239:656,6b09dc9b3722ffa4d4da52ae3efee0af8afa72a0@65.109.90.171:26656,46dbff2358dddd99acc26c2d2ee5f204ccc347c7@217.76.61.242:26656,082e95b5d5351e68dcfb24dff802f9064cfd5a4c@65.109.92.241:51056,4cd60a4dd4211d38d948a86a614f1fd8d3d274eb@75.119.153.139:656,f7fcda07044dc64cec2f6dca9da0c37a254bbae8@138.201.127.91:26676,cf97c77d4f28c3bd619efe10f4f9aa404f246853@161.97.154.51:26656,8f5935761a8bc93c7eaf9fc8bb29b4b184269447@46.8.210.144:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gitopia/config/config.toml
```
