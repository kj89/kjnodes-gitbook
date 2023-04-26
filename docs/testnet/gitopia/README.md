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
peers="63381c5528ed8ca93f9ba31008a9630d21b29a97@142.132.152.46:46656,bc688b2be879ba5bfa34587e096a9c9a4df2e6d4@45.151.122.116:656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,7e0acc9368640587d09fe0b2ef9cba3549b0ba44@65.108.9.164:20556,a8e74ebf033def6fbb28d1b846d7a6c275ad2ef1@65.109.65.163:20556,bd7c6c83af99edf0ee5b857a99997fb9fc8f40a7@65.109.116.204:20556,76895e84873db23aa366296acc6900e1dd980f43@144.76.176.154:41656,d2975b49708dc92ee3b7da1d72e3eee3119d1d0c@167.86.105.216:656,1f0f03a1c845e810e5cfeb0d960639c637d049fe@154.26.131.130:36656,6b09dc9b3722ffa4d4da52ae3efee0af8afa72a0@65.109.90.171:26656,9912d5c8d59b7736b0702b18aeb386efe7e46f3f@164.68.111.239:656,b745e0c6a1e0c7ec248ec274cfd038ed4bc4c2cf@65.21.134.202:26356,53b421af01f3260e949d6a9c2dc09e3b1dbf9fb6@109.205.181.30:41656,ac606e28c081c679dc23d9a94c29842be8f8b1f1@45.85.249.133:656,399d4e19186577b04c23296c4f7ecc53e61080cb@34.143.189.236:26656,5f4aee494e44d65f31753d7122f074f27b3ed8a2@95.216.162.25:656,3e5ba61e8481c6c71d3f2cc022dd6671ed7cacf8@65.21.170.3:41656,082e95b5d5351e68dcfb24dff802f9064cfd5a4c@65.109.92.241:51056,820024c34989e7605d9367847e1fc2d01ad763bd@65.109.92.235:30656,88ce80cb509fd973e06a552e1a5075d1292545d6@46.166.172.226:26656,4cd60a4dd4211d38d948a86a614f1fd8d3d274eb@75.119.153.139:656,314ee8896c9f9e39450dc25623f8019cf316ed60@38.242.135.124:26656,ef8bf45c54182573c9a852e8181f43838e198467@185.245.183.253:41656,d9d59b442e46f142394fcdf2f246ca8c7b2b7ce9@149.102.146.36:26656,9c265cb98c21d6748822ca2bed0accacdd8449db@38.242.205.25:26656,98bdfc67810bf7ac8f5c45b2c677b4bf199eb42e@185.193.67.65:41656,eaa9978430e55663346eb61312cd5ecc21448b25@38.242.139.153:656,5c74fe6868cda2003926c0a6299c9cebec5c4d1a@65.21.239.60:41656,66f94651fb02f277c90c605a38df549d3c0a9269@75.119.151.217:26656,7da6c90fe420bca73b5274884236134acf49d565@35.168.32.254:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gitopia/config/config.toml
```
