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
* grpc: gitopia-testnet.grpc.kjnodes.com:14190

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@gitopia-testnet.rpc.kjnodes.com:14156
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@gitopia-testnet.rpc.kjnodes.com:14159
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/gitopia-testnet/addrbook.json > $HOME/.gitopia/config/addrbook.json
```

**live-peers** (10)
```bash
peers="93c4c73375b5f52020e7e7bd3f901ee28f07e6b7@109.123.243.66:41656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14156,66f94651fb02f277c90c605a38df549d3c0a9269@75.119.151.217:26656,4e4f87cfa1993f4f3f7645c41f469987cafdf960@85.10.202.135:12656,619a23818cddd40d0b9f57e9754b719da13609bc@65.108.108.52:24656,5b1c25f4dff541f77f1532c457f73ca7ee2e4c18@194.163.170.225:26656,6e586e45f8a9d73333d24cd0fa7f64abc8be6d2b@65.108.226.183:11356,f13a4cb3ca18c1de6232e901c8feb209f0945954@65.109.65.248:26656,37c3d29df83da59e5a258d413e2f89365ab05711@85.239.243.12:656,66116d559390844588c67db54b894779cf00d559@5.9.61.237:41656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gitopia/config/config.toml
```
