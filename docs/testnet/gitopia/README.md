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
peers="c2beb74ebaf76137702732f6076c9a319bf15262@159.69.72.247:41656,3e5ba61e8481c6c71d3f2cc022dd6671ed7cacf8@65.21.170.3:41656,f7fcda07044dc64cec2f6dca9da0c37a254bbae8@138.201.127.91:26676,9cd6d2477d278ef6ccffa5cc4e22fd0d9489cd23@85.10.199.157:34656,bd7c6c83af99edf0ee5b857a99997fb9fc8f40a7@65.109.116.204:20556,a8e74ebf033def6fbb28d1b846d7a6c275ad2ef1@65.109.65.163:20556,7a755a2d4d5d609fed651662ebe37997256cff46@193.34.217.183:26656,f314268ef1886e4ad2801c8443ea0b0c8143a246@95.214.55.25:30656,247dbc8048be7c024c5f5deee45c18bd2f19bc93@116.203.35.46:36656,eaa9978430e55663346eb61312cd5ecc21448b25@38.242.139.153:656,820024c34989e7605d9367847e1fc2d01ad763bd@65.109.92.235:30656,399d4e19186577b04c23296c4f7ecc53e61080cb@34.143.189.236:26656,1cf3826ccd9a24caa549cbea061446716858133e@154.26.130.95:36656,415a1aebc5d2895d5191925b4ced76f2a295da60@185.250.36.176:41656,4e0e57bcac8aa2bc3188d5b7845eeee61a61f3f0@194.163.170.165:26656,98bdfc67810bf7ac8f5c45b2c677b4bf199eb42e@185.193.67.65:41656,6e586e45f8a9d73333d24cd0fa7f64abc8be6d2b@65.108.226.183:11356,0150c41282284a9546f8fe0f2531fc6b9d9128a3@65.109.23.114:11356,b745e0c6a1e0c7ec248ec274cfd038ed4bc4c2cf@65.21.134.202:26356,8d45cada398e1035e220857a84021fabfa723248@2.58.82.21:26656,f0b8227e40f25eaec0e25b9e91ca199d2d9a1ecb@167.86.94.177:656,88ce80cb509fd973e06a552e1a5075d1292545d6@46.166.172.226:26656,9c265cb98c21d6748822ca2bed0accacdd8449db@38.242.205.25:26656,f760d4e2f650e5c95b128399cb6f9c87e0dc09cb@89.117.48.180:656,5ed24b6ace024919dc5035a7e650af0e5a2166d5@144.76.97.251:38816,c84906b19dc7dc7bda94ab2167d4b0af64a28b49@45.151.122.191:656,ee598d227438a0c68bea18ec1e1ba606c6be4cd3@193.34.217.174:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,59a99a10a28baeda8535598acef9abb706ec5dbc@45.85.249.132:656,7da6c90fe420bca73b5274884236134acf49d565@35.168.32.254:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gitopia/config/config.toml
```
