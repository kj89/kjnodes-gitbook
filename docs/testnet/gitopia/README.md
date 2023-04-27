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
peers="6ea375302fdd319ef64e013f469e286faf739da8@213.239.207.165:20086,3e5ba61e8481c6c71d3f2cc022dd6671ed7cacf8@65.21.170.3:41656,6b09dc9b3722ffa4d4da52ae3efee0af8afa72a0@65.109.90.171:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,1cf3826ccd9a24caa549cbea061446716858133e@154.26.130.95:36656,a8e74ebf033def6fbb28d1b846d7a6c275ad2ef1@65.109.65.163:20556,bd7c6c83af99edf0ee5b857a99997fb9fc8f40a7@65.109.116.204:20556,399d4e19186577b04c23296c4f7ecc53e61080cb@34.143.189.236:26656,b745e0c6a1e0c7ec248ec274cfd038ed4bc4c2cf@65.21.134.202:26356,1f0f03a1c845e810e5cfeb0d960639c637d049fe@154.26.131.130:36656,63381c5528ed8ca93f9ba31008a9630d21b29a97@142.132.152.46:46656,f13a4cb3ca18c1de6232e901c8feb209f0945954@65.109.65.248:26656,8bec864d68a2542233ba37ac94c723fdf0b8e175@45.151.122.136:656,247dbc8048be7c024c5f5deee45c18bd2f19bc93@116.203.35.46:36656,4ed110a5b1ebad62d1e92e8cdabfc9160e2ca4db@65.109.92.148:46656,820024c34989e7605d9367847e1fc2d01ad763bd@65.109.92.235:30656,082e95b5d5351e68dcfb24dff802f9064cfd5a4c@65.109.92.241:51056,4e0e57bcac8aa2bc3188d5b7845eeee61a61f3f0@194.163.170.165:26656,d2975b49708dc92ee3b7da1d72e3eee3119d1d0c@167.86.105.216:656,0e9f303834a5d1f3be0babd5466725b3609ebc82@65.21.141.246:28656,88ce80cb509fd973e06a552e1a5075d1292545d6@46.166.172.226:26656,ee598d227438a0c68bea18ec1e1ba606c6be4cd3@193.34.217.174:26656,f0a82f850a0da74c32836b125a52bdfd9a78fdd7@65.108.105.48:11356,1989ced6b71ce676a5ab4d0586d85e38fd41fbd2@136.243.88.91:7070,9c265cb98c21d6748822ca2bed0accacdd8449db@38.242.205.25:26656,a8ab2588c7070d93f98c27cc6ac062046627260d@84.21.171.80:26656,d9d59b442e46f142394fcdf2f246ca8c7b2b7ce9@149.102.146.36:26656,52098a0fdd0dc566615ad37492019d252635bdda@45.85.249.131:656,449bd33a10f36244ecfb4ada6f2628137190fbf7@38.242.239.157:26656,7da6c90fe420bca73b5274884236134acf49d565@35.168.32.254:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gitopia/config/config.toml
```
