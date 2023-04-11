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
peers="943dbf5b8694620c1e0cce336d6a8a3327929c77@65.109.122.105:60656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,7e0acc9368640587d09fe0b2ef9cba3549b0ba44@65.108.9.164:20556,9bb344d83fc1fafc4bce6b8e4a95b82f37ac4f31@82.208.20.136:26656,399d4e19186577b04c23296c4f7ecc53e61080cb@34.143.189.236:26656,397cf4db87961e3a92f54b460300fc01d4dfa8f4@142.132.202.50:37656,7d39b009b329fc1a36457e814378872e67aef5c8@84.46.252.93:26656,15bb9edc16710d321163e7ef8b9a44959dd7e657@65.108.126.46:30656,c311e578c8b4e0f496f1d395473e74967c5b502c@164.92.197.50:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:27036,63381c5528ed8ca93f9ba31008a9630d21b29a97@142.132.152.46:46656,95c263a8bc8ef6dadbbeeeb242de4f89cf3c9657@193.34.217.154:26656,4ed110a5b1ebad62d1e92e8cdabfc9160e2ca4db@65.109.92.148:46656,8bec864d68a2542233ba37ac94c723fdf0b8e175@45.151.122.136:656,66116d559390844588c67db54b894779cf00d559@5.9.61.237:41656,95203479677e2ab00b1fb0bc1359294d4612e684@85.239.231.0:26656,1cf3826ccd9a24caa549cbea061446716858133e@154.26.130.95:36656,b745e0c6a1e0c7ec248ec274cfd038ed4bc4c2cf@65.21.134.202:26356,4e0e57bcac8aa2bc3188d5b7845eeee61a61f3f0@194.163.170.165:26656,f0b8227e40f25eaec0e25b9e91ca199d2d9a1ecb@167.86.94.177:656,d9d59b442e46f142394fcdf2f246ca8c7b2b7ce9@149.102.146.36:26656,6ea375302fdd319ef64e013f469e286faf739da8@213.239.207.165:20086,4cd60a4dd4211d38d948a86a614f1fd8d3d274eb@75.119.153.139:656,1f0f03a1c845e810e5cfeb0d960639c637d049fe@154.26.131.130:36656,43739b82ac0a52697543fff3ac00d267399c1d2d@84.54.23.4:41656,082e95b5d5351e68dcfb24dff802f9064cfd5a4c@65.109.92.241:51056,5ed24b6ace024919dc5035a7e650af0e5a2166d5@144.76.97.251:38816,eaa9978430e55663346eb61312cd5ecc21448b25@38.242.139.153:656,007d2419fea80aee707d009af0153f5105c53379@38.242.139.164:656,7da6c90fe420bca73b5274884236134acf49d565@35.168.32.254:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gitopia/config/config.toml
```
