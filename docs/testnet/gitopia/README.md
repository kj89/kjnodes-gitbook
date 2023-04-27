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
peers="d2975b49708dc92ee3b7da1d72e3eee3119d1d0c@167.86.105.216:656,a8e74ebf033def6fbb28d1b846d7a6c275ad2ef1@65.109.65.163:20556,9477e9810bc79d41666276804296d2a853996e22@167.86.89.182:656,53b421af01f3260e949d6a9c2dc09e3b1dbf9fb6@109.205.181.30:41656,bd7c6c83af99edf0ee5b857a99997fb9fc8f40a7@65.109.116.204:20556,399d4e19186577b04c23296c4f7ecc53e61080cb@34.143.189.236:26656,820024c34989e7605d9367847e1fc2d01ad763bd@65.109.92.235:30656,4e0e57bcac8aa2bc3188d5b7845eeee61a61f3f0@194.163.170.165:26656,b745e0c6a1e0c7ec248ec274cfd038ed4bc4c2cf@65.21.134.202:26356,1cf3826ccd9a24caa549cbea061446716858133e@154.26.130.95:36656,1f0f03a1c845e810e5cfeb0d960639c637d049fe@154.26.131.130:36656,9c265cb98c21d6748822ca2bed0accacdd8449db@38.242.205.25:26656,c2beb74ebaf76137702732f6076c9a319bf15262@159.69.72.247:41656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,eaa9978430e55663346eb61312cd5ecc21448b25@38.242.139.153:656,1983d3cbcbc281232b5946ba9a2487e8f6976817@149.102.148.141:26656,082e95b5d5351e68dcfb24dff802f9064cfd5a4c@65.109.92.241:51056,ee812a11525cf7e2de4bd63e66aed8b8de337902@38.242.235.199:41656,88ce80cb509fd973e06a552e1a5075d1292545d6@46.166.172.226:26656,247dbc8048be7c024c5f5deee45c18bd2f19bc93@116.203.35.46:36656,9912d5c8d59b7736b0702b18aeb386efe7e46f3f@164.68.111.239:656,f13a4cb3ca18c1de6232e901c8feb209f0945954@65.109.65.248:26656,5b1c25f4dff541f77f1532c457f73ca7ee2e4c18@194.163.170.225:26656,7334166688a52b1adc9d72aaa4a3b56139ad1da2@109.123.255.116:26656,8bec864d68a2542233ba37ac94c723fdf0b8e175@45.151.122.136:656,66f94651fb02f277c90c605a38df549d3c0a9269@75.119.151.217:26656,37c3d29df83da59e5a258d413e2f89365ab05711@85.239.243.12:656,4ed110a5b1ebad62d1e92e8cdabfc9160e2ca4db@65.109.92.148:46656,6da2faa11e21db872cc64a975160a55b5fc9166d@149.102.128.203:26656,7d39b009b329fc1a36457e814378872e67aef5c8@84.46.252.93:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gitopia/config/config.toml
```
