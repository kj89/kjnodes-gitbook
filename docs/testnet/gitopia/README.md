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

**live-peers** (28)
```bash
peers="ef8bf45c54182573c9a852e8181f43838e198467@185.245.183.253:41656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,38b327ce97c670014d52701e3a26eaa16fee1f7f@149.102.151.204:26656,7e0acc9368640587d09fe0b2ef9cba3549b0ba44@65.108.9.164:20556,a8e74ebf033def6fbb28d1b846d7a6c275ad2ef1@65.109.65.163:20556,bd7c6c83af99edf0ee5b857a99997fb9fc8f40a7@65.109.116.204:20556,6b09dc9b3722ffa4d4da52ae3efee0af8afa72a0@65.109.90.171:26656,f7fcda07044dc64cec2f6dca9da0c37a254bbae8@138.201.127.91:26676,1cf3826ccd9a24caa549cbea061446716858133e@154.26.130.95:36656,f0b8227e40f25eaec0e25b9e91ca199d2d9a1ecb@167.86.94.177:656,399d4e19186577b04c23296c4f7ecc53e61080cb@34.143.189.236:26656,9c265cb98c21d6748822ca2bed0accacdd8449db@38.242.205.25:26656,6ea375302fdd319ef64e013f469e286faf739da8@213.239.207.165:20086,ffb4f7d43d6449c292d4e60c8a48eb3d31c39691@38.242.139.100:656,b745e0c6a1e0c7ec248ec274cfd038ed4bc4c2cf@65.21.134.202:26356,63381c5528ed8ca93f9ba31008a9630d21b29a97@142.132.152.46:46656,05182a9b6121c9fcbb493f9bb3843e20e076e479@38.242.231.113:656,98bdfc67810bf7ac8f5c45b2c677b4bf199eb42e@185.193.67.65:41656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:27036,9912d5c8d59b7736b0702b18aeb386efe7e46f3f@164.68.111.239:656,1f0f03a1c845e810e5cfeb0d960639c637d049fe@154.26.131.130:36656,314ee8896c9f9e39450dc25623f8019cf316ed60@38.242.135.124:26656,247dbc8048be7c024c5f5deee45c18bd2f19bc93@116.203.35.46:36656,f0a82f850a0da74c32836b125a52bdfd9a78fdd7@65.108.105.48:11356,e28ab99ea7db98c5dfd7225d1623959f27805d93@34.143.211.179:26656,4cd60a4dd4211d38d948a86a614f1fd8d3d274eb@75.119.153.139:656,8bec864d68a2542233ba37ac94c723fdf0b8e175@45.151.122.136:656,7da6c90fe420bca73b5274884236134acf49d565@35.168.32.254:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gitopia/config/config.toml
```
