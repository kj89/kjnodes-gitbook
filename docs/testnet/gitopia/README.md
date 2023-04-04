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
peers="63381c5528ed8ca93f9ba31008a9630d21b29a97@142.132.152.46:46656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:27036,9bb344d83fc1fafc4bce6b8e4a95b82f37ac4f31@82.208.20.136:26656,f9b892ea2e8ed8aa83f7b98e7e47371c23b01924@213.239.207.175:36656,43739b82ac0a52697543fff3ac00d267399c1d2d@84.54.23.4:41656,1cf3826ccd9a24caa549cbea061446716858133e@154.26.130.95:36656,ac606e28c081c679dc23d9a94c29842be8f8b1f1@45.85.249.133:656,943dbf5b8694620c1e0cce336d6a8a3327929c77@65.109.122.105:60656,53b421af01f3260e949d6a9c2dc09e3b1dbf9fb6@109.205.181.30:41656,35c829910f80387ee825da9fb69efbcbf8e2149e@164.68.118.227:26656,3b0956b482f89b361dd350f1c6b3743096897446@65.108.124.219:35656,399d4e19186577b04c23296c4f7ecc53e61080cb@34.143.189.236:26656,eccdf1d5bf33bc1733838562b4d4a4a45869c3a8@135.181.183.93:41656,03073657e8bc5bcf71e7fd8df281ab8dcbc8821a@45.151.122.130:656,4e0e57bcac8aa2bc3188d5b7845eeee61a61f3f0@194.163.170.165:26656,4ed110a5b1ebad62d1e92e8cdabfc9160e2ca4db@65.109.92.148:46656,9912d5c8d59b7736b0702b18aeb386efe7e46f3f@164.68.111.239:656,99a730ccb60933b5f9a282e899af7eb2e61d6ccc@81.30.157.35:26656,4cd60a4dd4211d38d948a86a614f1fd8d3d274eb@75.119.153.139:656,820024c34989e7605d9367847e1fc2d01ad763bd@65.109.92.235:30656,df5b61e51ab2f6c3bf1f3c387ba1586a84b41b25@135.181.116.109:27956,eaa9978430e55663346eb61312cd5ecc21448b25@38.242.139.153:656,8bec864d68a2542233ba37ac94c723fdf0b8e175@45.151.122.136:656,b745e0c6a1e0c7ec248ec274cfd038ed4bc4c2cf@65.21.134.202:26356,ed177ff3cf334df1a6c190438b0c7b5dd64b423a@45.151.122.140:656,24453bdf119b17550849851d69c50cde7b140460@84.46.253.3:41656,34d3ee88e9f3d677ca93c084e701d43e188f68c5@65.108.224.156:26656,5c45e8920c5094827ec5afaca9ab469aaa0b4eaf@65.109.88.254:28656,7da6c90fe420bca73b5274884236134acf49d565@35.168.32.254:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gitopia/config/config.toml
```
