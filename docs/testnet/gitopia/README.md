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
peers="a52dcd34843340a4df6dcb93e8a8d6eb78d796fa@85.10.193.246:26656,619a23818cddd40d0b9f57e9754b719da13609bc@65.108.108.52:24656,0c31077af45cb4f0424e58c91b0a917c36a90fd9@65.108.195.235:16656,3b0956b482f89b361dd350f1c6b3743096897446@65.108.124.219:35656,ac606e28c081c679dc23d9a94c29842be8f8b1f1@45.85.249.133:656,63381c5528ed8ca93f9ba31008a9630d21b29a97@142.132.152.46:46656,f13a4cb3ca18c1de6232e901c8feb209f0945954@65.109.65.248:26656,98bdfc67810bf7ac8f5c45b2c677b4bf199eb42e@185.193.67.65:41656,023c6a86fbd8b8368503c92bd612a8c0379a26e5@194.146.13.251:656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14156"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gitopia/config/config.toml
```
