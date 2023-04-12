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
peers="0c31077af45cb4f0424e58c91b0a917c36a90fd9@65.108.195.235:16656,619a23818cddd40d0b9f57e9754b719da13609bc@65.108.108.52:24656,4cd60a4dd4211d38d948a86a614f1fd8d3d274eb@75.119.153.139:656,c84906b19dc7dc7bda94ab2167d4b0af64a28b49@45.151.122.191:656,7e0acc9368640587d09fe0b2ef9cba3549b0ba44@65.108.9.164:20556,abff0d16ee379200e806cfc544ee8c2c9d0ab5dc@38.242.251.77:26656,d6b7f1a8d7572a63d3d84c8d36003ffe46ea6647@75.119.149.221:26656,399d4e19186577b04c23296c4f7ecc53e61080cb@34.143.189.236:26656,81f9bdd0e1e01390b70df7544b45efdccb52e41c@84.54.23.199:26656,f9b892ea2e8ed8aa83f7b98e7e47371c23b01924@213.239.207.175:36656,eccdf1d5bf33bc1733838562b4d4a4a45869c3a8@135.181.183.93:41656,f1a47d469460fb0a70b12d7739afbc0bf78eadda@78.47.195.69:656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:27036,05182a9b6121c9fcbb493f9bb3843e20e076e479@38.242.231.113:656,f0b8227e40f25eaec0e25b9e91ca199d2d9a1ecb@167.86.94.177:656,95fbdc6d62be17db6688222b15b57d3e795ed07a@167.86.84.102:656,66f94651fb02f277c90c605a38df549d3c0a9269@75.119.151.217:26656,9bb344d83fc1fafc4bce6b8e4a95b82f37ac4f31@82.208.20.136:26656,b745e0c6a1e0c7ec248ec274cfd038ed4bc4c2cf@65.21.134.202:26356,6ea375302fdd319ef64e013f469e286faf739da8@213.239.207.165:20086,77cf0280cec16e6cf51ac3a767fc1cccd238694f@176.9.121.109:41156,84e6cb2368217e6e375f2c60ba40ac2e547dd220@165.232.115.195:26656,d9d59b442e46f142394fcdf2f246ca8c7b2b7ce9@149.102.146.36:26656,1cf3826ccd9a24caa549cbea061446716858133e@154.26.130.95:36656,820024c34989e7605d9367847e1fc2d01ad763bd@65.109.92.235:30656,8bec864d68a2542233ba37ac94c723fdf0b8e175@45.151.122.136:656,eaa9978430e55663346eb61312cd5ecc21448b25@38.242.139.153:656,8f5935761a8bc93c7eaf9fc8bb29b4b184269447@46.8.210.144:26656,1f0f03a1c845e810e5cfeb0d960639c637d049fe@154.26.131.130:36656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gitopia/config/config.toml
```
