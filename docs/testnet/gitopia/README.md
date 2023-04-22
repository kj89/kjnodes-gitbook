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
peers="63381c5528ed8ca93f9ba31008a9630d21b29a97@142.132.152.46:46656,619a23818cddd40d0b9f57e9754b719da13609bc@65.108.108.52:24656,820024c34989e7605d9367847e1fc2d01ad763bd@65.109.92.235:30656,9c265cb98c21d6748822ca2bed0accacdd8449db@38.242.205.25:26656,52a2fb0aa22551b1ef0155824228924d41c1daa6@85.239.230.213:26656,b745e0c6a1e0c7ec248ec274cfd038ed4bc4c2cf@65.21.134.202:26356,8bec864d68a2542233ba37ac94c723fdf0b8e175@45.151.122.136:656,bd7c6c83af99edf0ee5b857a99997fb9fc8f40a7@65.109.116.204:20556,a8e74ebf033def6fbb28d1b846d7a6c275ad2ef1@65.109.65.163:20556,7e0acc9368640587d09fe0b2ef9cba3549b0ba44@65.108.9.164:20556,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:27036,93c4c73375b5f52020e7e7bd3f901ee28f07e6b7@109.123.243.66:41656,66116d559390844588c67db54b894779cf00d559@5.9.61.237:41656,f13a4cb3ca18c1de6232e901c8feb209f0945954@65.109.65.248:26656,f0a82f850a0da74c32836b125a52bdfd9a78fdd7@65.108.105.48:11356,399d4e19186577b04c23296c4f7ecc53e61080cb@34.143.189.236:26656,4cd60a4dd4211d38d948a86a614f1fd8d3d274eb@75.119.153.139:656,63690ab7cb14823c70f0e6a7f699c6cbbbde529b@1.15.72.152:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,7d39b009b329fc1a36457e814378872e67aef5c8@84.46.252.93:26656,f0b8227e40f25eaec0e25b9e91ca199d2d9a1ecb@167.86.94.177:656,89d6b496813ea8f268b8410b34ddb2c86a726b6f@193.34.217.151:26656,247dbc8048be7c024c5f5deee45c18bd2f19bc93@116.203.35.46:36656,03073657e8bc5bcf71e7fd8df281ab8dcbc8821a@45.151.122.130:656,98bdfc67810bf7ac8f5c45b2c677b4bf199eb42e@185.193.67.65:41656,082e95b5d5351e68dcfb24dff802f9064cfd5a4c@65.109.92.241:51056,88ce80cb509fd973e06a552e1a5075d1292545d6@46.166.172.226:26656,ef8bf45c54182573c9a852e8181f43838e198467@185.245.183.253:41656,66f94651fb02f277c90c605a38df549d3c0a9269@75.119.151.217:26656,7da6c90fe420bca73b5274884236134acf49d565@35.168.32.254:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gitopia/config/config.toml
```
