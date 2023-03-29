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

**live-peers** (34)
```bash
peers="66116d559390844588c67db54b894779cf00d559@5.9.61.237:41656,eccdf1d5bf33bc1733838562b4d4a4a45869c3a8@135.181.183.93:41656,e88708f6bda2af195f0ec48b9868e588ead964fb@144.91.82.239:26656,f4a2a6b840d1bad6f09c726d51f81d03f41c9ecc@194.146.13.246:656,7da6c90fe420bca73b5274884236134acf49d565@35.168.32.254:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,37ba718e5cec3c1034dbda32e1e6c73ab6f6278d@143.110.224.162:26656,1cf3826ccd9a24caa549cbea061446716858133e@154.26.130.95:36656,098c8f3e70fa1f1bbb447903aea96b8e1f025f13@141.95.145.41:26656,9bb344d83fc1fafc4bce6b8e4a95b82f37ac4f31@82.208.20.136:26656,eaa9978430e55663346eb61312cd5ecc21448b25@38.242.139.153:656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:27036,37c3d29df83da59e5a258d413e2f89365ab05711@85.239.243.12:656,f314268ef1886e4ad2801c8443ea0b0c8143a246@95.214.55.25:30656,4cd60a4dd4211d38d948a86a614f1fd8d3d274eb@75.119.153.139:656,399d4e19186577b04c23296c4f7ecc53e61080cb@34.143.189.236:26656,1f0f03a1c845e810e5cfeb0d960639c637d049fe@154.26.131.130:36656,4e0e57bcac8aa2bc3188d5b7845eeee61a61f3f0@194.163.170.165:26656,f0b8227e40f25eaec0e25b9e91ca199d2d9a1ecb@167.86.94.177:656,8bec864d68a2542233ba37ac94c723fdf0b8e175@45.151.122.136:656,ffb4f7d43d6449c292d4e60c8a48eb3d31c39691@38.242.139.100:656,292c099fc654a1331d3b62a1b939f867b62ef434@45.85.147.242:656,5f045d143cdf9ac78821e848cb10f9c861f5e272@89.117.56.126:24256,66f94651fb02f277c90c605a38df549d3c0a9269@75.119.151.217:26656,023c6a86fbd8b8368503c92bd612a8c0379a26e5@194.146.13.251:656,deca8c5aed2d1e617789d80927394a1d4d1c7360@149.102.146.123:26656,95fbdc6d62be17db6688222b15b57d3e795ed07a@167.86.84.102:656,98bdfc67810bf7ac8f5c45b2c677b4bf199eb42e@185.193.67.65:41656,f235119c7a14d2bfca013c4835056bd748177104@194.146.13.247:656,b745e0c6a1e0c7ec248ec274cfd038ed4bc4c2cf@65.21.134.202:26356,7d819fa869f7c5b42c2c7a9538e1a9e7a52cfdee@65.108.226.26:24656,f026faf0dfc8a19f8029c6ec08d1e8454a2c9475@149.102.133.56:26656,a3689d27a8905f46275623a135a29b991a37b39f@167.235.227.127:41656,9c265cb98c21d6748822ca2bed0accacdd8449db@38.242.205.25:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gitopia/config/config.toml
```
