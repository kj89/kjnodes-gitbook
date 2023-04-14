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
peers="9645f93ac2b57431a8ca32ac56b0ff63fe9c10ed@144.76.164.139:10656,bce720f986092e4fb804655400cea1dbf29b594f@116.202.227.117:41656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,7e0acc9368640587d09fe0b2ef9cba3549b0ba44@65.108.9.164:20556,247dbc8048be7c024c5f5deee45c18bd2f19bc93@116.203.35.46:36656,d2975b49708dc92ee3b7da1d72e3eee3119d1d0c@167.86.105.216:656,8bec864d68a2542233ba37ac94c723fdf0b8e175@45.151.122.136:656,b745e0c6a1e0c7ec248ec274cfd038ed4bc4c2cf@65.21.134.202:26356,9c265cb98c21d6748822ca2bed0accacdd8449db@38.242.205.25:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:27036,1989ced6b71ce676a5ab4d0586d85e38fd41fbd2@136.243.88.91:7070,399d4e19186577b04c23296c4f7ecc53e61080cb@34.143.189.236:26656,1f0f03a1c845e810e5cfeb0d960639c637d049fe@154.26.131.130:36656,e7027bab63132e05d2183bdd754faa668cd95259@149.102.159.72:26656,4cd60a4dd4211d38d948a86a614f1fd8d3d274eb@75.119.153.139:656,820024c34989e7605d9367847e1fc2d01ad763bd@65.109.92.235:30656,082e95b5d5351e68dcfb24dff802f9064cfd5a4c@65.109.92.241:51056,eaa9978430e55663346eb61312cd5ecc21448b25@38.242.139.153:656,0e9f303834a5d1f3be0babd5466725b3609ebc82@65.21.141.246:28656,943dbf5b8694620c1e0cce336d6a8a3327929c77@65.109.122.105:60656,3e5ba61e8481c6c71d3f2cc022dd6671ed7cacf8@65.21.170.3:41656,4ed110a5b1ebad62d1e92e8cdabfc9160e2ca4db@65.109.92.148:46656,1cf3826ccd9a24caa549cbea061446716858133e@154.26.130.95:36656,63381c5528ed8ca93f9ba31008a9630d21b29a97@142.132.152.46:46656,f0b8227e40f25eaec0e25b9e91ca199d2d9a1ecb@167.86.94.177:656,5f045d143cdf9ac78821e848cb10f9c861f5e272@89.117.56.126:24256,eccdf1d5bf33bc1733838562b4d4a4a45869c3a8@135.181.183.93:41656,a6f4fd8efe8a575a15e25652ecebce3fa1ed62a0@213.239.217.52:35656,006be929170f69951b08c7f839952776e3f7f4b4@109.123.253.67:26656,59a99a10a28baeda8535598acef9abb706ec5dbc@45.85.249.132:656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gitopia/config/config.toml
```
