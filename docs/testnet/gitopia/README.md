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
peers="c78af3c8a2fa3d398dedb1ad9052eaf60dc27434@95.216.163.254:41656,03073657e8bc5bcf71e7fd8df281ab8dcbc8821a@45.151.122.130:656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,66f94651fb02f277c90c605a38df549d3c0a9269@75.119.151.217:26656,24453bdf119b17550849851d69c50cde7b140460@84.46.253.3:41656,4e0e57bcac8aa2bc3188d5b7845eeee61a61f3f0@194.163.170.165:26656,399d4e19186577b04c23296c4f7ecc53e61080cb@34.143.189.236:26656,f0b8227e40f25eaec0e25b9e91ca199d2d9a1ecb@167.86.94.177:656,5c45e8920c5094827ec5afaca9ab469aaa0b4eaf@65.109.88.254:28656,52098a0fdd0dc566615ad37492019d252635bdda@45.85.249.131:656,1f0f03a1c845e810e5cfeb0d960639c637d049fe@154.26.131.130:36656,8bec864d68a2542233ba37ac94c723fdf0b8e175@45.151.122.136:656,ffb4f7d43d6449c292d4e60c8a48eb3d31c39691@38.242.139.100:656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:27036,292c099fc654a1331d3b62a1b939f867b62ef434@45.85.147.242:656,d2975b49708dc92ee3b7da1d72e3eee3119d1d0c@167.86.105.216:656,9912d5c8d59b7736b0702b18aeb386efe7e46f3f@164.68.111.239:656,b745e0c6a1e0c7ec248ec274cfd038ed4bc4c2cf@65.21.134.202:26356,deca8c5aed2d1e617789d80927394a1d4d1c7360@149.102.146.123:26656,9c265cb98c21d6748822ca2bed0accacdd8449db@38.242.205.25:26656,4cd60a4dd4211d38d948a86a614f1fd8d3d274eb@75.119.153.139:656,1403980403d63c055aa13dd500ab384e32785af2@95.217.214.8:26656,ed177ff3cf334df1a6c190438b0c7b5dd64b423a@45.151.122.140:656,59a99a10a28baeda8535598acef9abb706ec5dbc@45.85.249.132:656,c84906b19dc7dc7bda94ab2167d4b0af64a28b49@45.151.122.191:656,76895e84873db23aa366296acc6900e1dd980f43@144.76.176.154:41656,1cf3826ccd9a24caa549cbea061446716858133e@154.26.130.95:36656,f1a47d469460fb0a70b12d7739afbc0bf78eadda@78.47.195.69:656,81f9bdd0e1e01390b70df7544b45efdccb52e41c@84.54.23.199:26656,7da6c90fe420bca73b5274884236134acf49d565@35.168.32.254:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gitopia/config/config.toml
```
