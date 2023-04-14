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
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,820024c34989e7605d9367847e1fc2d01ad763bd@65.109.92.235:30656,7e0acc9368640587d09fe0b2ef9cba3549b0ba44@65.108.9.164:20556,eaa9978430e55663346eb61312cd5ecc21448b25@38.242.139.153:656,9645f93ac2b57431a8ca32ac56b0ff63fe9c10ed@144.76.164.139:10656,975a3ade04fc92d00c7ad59d536506fde46169e7@167.86.96.233:656,ee812a11525cf7e2de4bd63e66aed8b8de337902@38.242.235.199:41656,399d4e19186577b04c23296c4f7ecc53e61080cb@34.143.189.236:26656,b745e0c6a1e0c7ec248ec274cfd038ed4bc4c2cf@65.21.134.202:26356,66f94651fb02f277c90c605a38df549d3c0a9269@75.119.151.217:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:27036,9bb344d83fc1fafc4bce6b8e4a95b82f37ac4f31@82.208.20.136:26656,1f0f03a1c845e810e5cfeb0d960639c637d049fe@154.26.131.130:36656,1cf3826ccd9a24caa549cbea061446716858133e@154.26.130.95:36656,95203479677e2ab00b1fb0bc1359294d4612e684@85.239.231.0:26656,f06f794dcc5964197da0e13709d71ea5e0f5b7f1@88.99.3.158:11156,9c265cb98c21d6748822ca2bed0accacdd8449db@38.242.205.25:26656,4cd60a4dd4211d38d948a86a614f1fd8d3d274eb@75.119.153.139:656,f7fcda07044dc64cec2f6dca9da0c37a254bbae8@138.201.127.91:26676,95fbdc6d62be17db6688222b15b57d3e795ed07a@167.86.84.102:656,bbc6a1e115185d5bffcbbf5520dca1c3d626e599@109.123.255.50:26656,61188ec3494908fc74f05a02c05cc86e4e587d9e@178.18.241.103:41656,8f5935761a8bc93c7eaf9fc8bb29b4b184269447@46.8.210.144:26656,1f7f58f130ea9c89be44fd60554d5e97da56c395@206.221.181.234:56656,03073657e8bc5bcf71e7fd8df281ab8dcbc8821a@45.151.122.130:656,0150c41282284a9546f8fe0f2531fc6b9d9128a3@65.109.23.114:11356,46dbff2358dddd99acc26c2d2ee5f204ccc347c7@217.76.61.242:26656,082e95b5d5351e68dcfb24dff802f9064cfd5a4c@65.109.92.241:51056,9e5b27c34a1302084a5946eeaf920effd897fc05@81.0.220.178:26656,7da6c90fe420bca73b5274884236134acf49d565@35.168.32.254:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gitopia/config/config.toml
```
