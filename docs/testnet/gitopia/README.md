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
peers="4e4f87cfa1993f4f3f7645c41f469987cafdf960@85.10.202.135:12656,619a23818cddd40d0b9f57e9754b719da13609bc@65.108.108.52:24656,7d819fa869f7c5b42c2c7a9538e1a9e7a52cfdee@65.108.226.26:24656,95fbdc6d62be17db6688222b15b57d3e795ed07a@167.86.84.102:656,f7fcda07044dc64cec2f6dca9da0c37a254bbae8@138.201.127.91:26676,0c31077af45cb4f0424e58c91b0a917c36a90fd9@65.108.195.235:16656,0e9f303834a5d1f3be0babd5466725b3609ebc82@65.21.141.246:28656,4cd60a4dd4211d38d948a86a614f1fd8d3d274eb@75.119.153.139:656,ae5d5b47ea732ff509114f405967f61eb3d86ac6@75.119.146.171:656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14156"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gitopia/config/config.toml
```
