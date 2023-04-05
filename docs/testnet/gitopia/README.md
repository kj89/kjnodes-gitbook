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
peers="63381c5528ed8ca93f9ba31008a9630d21b29a97@142.132.152.46:46656,e1ab0573d55ff92fad55d2929e353904f1bbe36f@135.181.16.252:31656,46dbff2358dddd99acc26c2d2ee5f204ccc347c7@217.76.61.242:26656,820024c34989e7605d9367847e1fc2d01ad763bd@65.109.92.235:30656,95fbdc6d62be17db6688222b15b57d3e795ed07a@167.86.84.102:656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:27036,f314268ef1886e4ad2801c8443ea0b0c8143a246@95.214.55.25:30656,399d4e19186577b04c23296c4f7ecc53e61080cb@34.143.189.236:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,4e0e57bcac8aa2bc3188d5b7845eeee61a61f3f0@194.163.170.165:26656,24453bdf119b17550849851d69c50cde7b140460@84.46.253.3:41656,f0b8227e40f25eaec0e25b9e91ca199d2d9a1ecb@167.86.94.177:656,9bb344d83fc1fafc4bce6b8e4a95b82f37ac4f31@82.208.20.136:26656,9ae4e6f0123fc1ad47846c83132df9d3b124fe49@89.117.50.250:41656,926b47f8d786e544ec3a9200c61b5b04729a9d57@199.175.98.127:41656,1cf3826ccd9a24caa549cbea061446716858133e@154.26.130.95:36656,9912d5c8d59b7736b0702b18aeb386efe7e46f3f@164.68.111.239:656,66f94651fb02f277c90c605a38df549d3c0a9269@75.119.151.217:26656,f31bc5f2b948c2a063d46d3b6b35da97d6f7cf5b@149.102.148.153:26656,ac606e28c081c679dc23d9a94c29842be8f8b1f1@45.85.249.133:656,ee812a11525cf7e2de4bd63e66aed8b8de337902@38.242.235.199:41656,9c265cb98c21d6748822ca2bed0accacdd8449db@38.242.205.25:26656,b745e0c6a1e0c7ec248ec274cfd038ed4bc4c2cf@65.21.134.202:26356,b2f764694d52e09793d68259d584ece0c194b6fe@65.108.229.93:28656,8d45cada398e1035e220857a84021fabfa723248@2.58.82.21:26656,f235119c7a14d2bfca013c4835056bd748177104@194.146.13.247:656,4cd60a4dd4211d38d948a86a614f1fd8d3d274eb@75.119.153.139:656,8f5935761a8bc93c7eaf9fc8bb29b4b184269447@46.8.210.144:26656,7da6c90fe420bca73b5274884236134acf49d565@35.168.32.254:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gitopia/config/config.toml
```
