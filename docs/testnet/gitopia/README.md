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
peers="eccdf1d5bf33bc1733838562b4d4a4a45869c3a8@135.181.183.93:41656,ac606e28c081c679dc23d9a94c29842be8f8b1f1@45.85.249.133:656,d9d59b442e46f142394fcdf2f246ca8c7b2b7ce9@149.102.146.36:26656,d9b86c9459ac8bb4760d37095732ccd2746aca1f@65.21.131.215:26356,bd7c6c83af99edf0ee5b857a99997fb9fc8f40a7@65.109.116.204:20556,a8e74ebf033def6fbb28d1b846d7a6c275ad2ef1@65.109.65.163:20556,9cd6d2477d278ef6ccffa5cc4e22fd0d9489cd23@85.10.199.157:34656,1cf3826ccd9a24caa549cbea061446716858133e@154.26.130.95:36656,b745e0c6a1e0c7ec248ec274cfd038ed4bc4c2cf@65.21.134.202:26356,415a1aebc5d2895d5191925b4ced76f2a295da60@185.250.36.176:41656,1f0f03a1c845e810e5cfeb0d960639c637d049fe@154.26.131.130:36656,5c74fe6868cda2003926c0a6299c9cebec5c4d1a@65.21.239.60:41656,247dbc8048be7c024c5f5deee45c18bd2f19bc93@116.203.35.46:36656,399d4e19186577b04c23296c4f7ecc53e61080cb@34.143.189.236:26656,3b0956b482f89b361dd350f1c6b3743096897446@65.108.124.219:35656,9c265cb98c21d6748822ca2bed0accacdd8449db@38.242.205.25:26656,f0b8227e40f25eaec0e25b9e91ca199d2d9a1ecb@167.86.94.177:656,820024c34989e7605d9367847e1fc2d01ad763bd@65.109.92.235:30656,5c45e8920c5094827ec5afaca9ab469aaa0b4eaf@65.109.88.254:28656,52ba59360cfc90c8beb1c3704a4c9ed9b38e597d@65.109.65.126:41656,59a99a10a28baeda8535598acef9abb706ec5dbc@45.85.249.132:656,98b64c1c1e2ec061337863653ffb937fc109a6b6@85.239.243.85:26656,95fbdc6d62be17db6688222b15b57d3e795ed07a@167.86.84.102:656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,88ce80cb509fd973e06a552e1a5075d1292545d6@46.166.172.226:26656,eaa9978430e55663346eb61312cd5ecc21448b25@38.242.139.153:656,66116d559390844588c67db54b894779cf00d559@5.9.61.237:41656,8bec864d68a2542233ba37ac94c723fdf0b8e175@45.151.122.136:656,f0a82f850a0da74c32836b125a52bdfd9a78fdd7@65.108.105.48:11356,7da6c90fe420bca73b5274884236134acf49d565@35.168.32.254:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gitopia/config/config.toml
```
