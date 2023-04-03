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

**live-peers** (29)
```bash
peers="0c31077af45cb4f0424e58c91b0a917c36a90fd9@65.108.195.235:16656,03073657e8bc5bcf71e7fd8df281ab8dcbc8821a@45.151.122.130:656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,59a99a10a28baeda8535598acef9abb706ec5dbc@45.85.249.132:656,0e9f303834a5d1f3be0babd5466725b3609ebc82@65.21.141.246:28656,c78af3c8a2fa3d398dedb1ad9052eaf60dc27434@95.216.163.254:41656,0eb70bf5e2403694109f9bba184570074c2dfdd5@38.242.235.255:26656,4e0e57bcac8aa2bc3188d5b7845eeee61a61f3f0@194.163.170.165:26656,bbc6a1e115185d5bffcbbf5520dca1c3d626e599@109.123.255.50:26656,399d4e19186577b04c23296c4f7ecc53e61080cb@34.143.189.236:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:27036,4cd60a4dd4211d38d948a86a614f1fd8d3d274eb@75.119.153.139:656,eaa9978430e55663346eb61312cd5ecc21448b25@38.242.139.153:656,8e20add7ed774bfd8600c628bb8fce87bacb207b@194.163.143.98:26656,9c265cb98c21d6748822ca2bed0accacdd8449db@38.242.205.25:26656,9912d5c8d59b7736b0702b18aeb386efe7e46f3f@164.68.111.239:656,f0b8227e40f25eaec0e25b9e91ca199d2d9a1ecb@167.86.94.177:656,d6b7f1a8d7572a63d3d84c8d36003ffe46ea6647@75.119.149.221:26656,a6f4fd8efe8a575a15e25652ecebce3fa1ed62a0@213.239.217.52:35656,ed177ff3cf334df1a6c190438b0c7b5dd64b423a@45.151.122.140:656,5b1c25f4dff541f77f1532c457f73ca7ee2e4c18@194.163.170.225:26656,9ae4e6f0123fc1ad47846c83132df9d3b124fe49@89.117.50.250:41656,bce720f986092e4fb804655400cea1dbf29b594f@116.202.227.117:41656,9bb344d83fc1fafc4bce6b8e4a95b82f37ac4f31@82.208.20.136:26656,f0a82f850a0da74c32836b125a52bdfd9a78fdd7@65.108.105.48:11356,007d2419fea80aee707d009af0153f5105c53379@38.242.139.164:656,8bec864d68a2542233ba37ac94c723fdf0b8e175@45.151.122.136:656,24453bdf119b17550849851d69c50cde7b140460@84.46.253.3:41656,34d3ee88e9f3d677ca93c084e701d43e188f68c5@65.108.224.156:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gitopia/config/config.toml
```
