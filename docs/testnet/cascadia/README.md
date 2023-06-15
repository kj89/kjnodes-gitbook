# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/cascadia.png" alt=""><figcaption></figcaption></figure>

Cascadia is a layer-1 blockchain built to explore the  nature of incentives on network effects, starting  with ve-tokenomics.

**Chain ID**: cascadia_6102-1 | **Latest Version Tag**: v0.1.2 | **Wasm**: OFF

[Website](https://www.cascadia.foundation) | [Discord](https://discord.gg/cascadia) | [Twitter](https://twitter.com/CascadiaSystems)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/cascadia-testnet](https://explorer.kjnodes.com/cascadia-testnet)

## Public endpoints

* api: [https://cascadia-testnet.api.kjnodes.com](https://cascadia-testnet.api.kjnodes.com)
* rpc: [https://cascadia-testnet.rpc.kjnodes.com](https://cascadia-testnet.rpc.kjnodes.com)
* grpc: cascadia-testnet.grpc.kjnodes.com:15590

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@cascadia-testnet.rpc.kjnodes.com:15556
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@cascadia-testnet.rpc.kjnodes.com:15559
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/cascadia-testnet/addrbook.json > $HOME/.cascadiad/config/addrbook.json
```

**live-peers** (11)
```bash
peers="af8b5486e4938c3bd9ab56fd5ee03d26857089a1@31.220.95.213:26656,c8d5ed2ce985364551b2bf11fe78770d5caafa62@82.208.22.200:26656,e25bf22448e62faca2359985303ec4557f662444@95.217.11.20:26656,4e5472f6fa35d86e1fed32bb0e2a65ec1f241f91@65.109.239.29:18656,24c3bd618c6c6c0df40968382e6b408429a020c7@95.217.217.253:50656,740b9d21195a434f10efd7796ea1406e6a713247@149.102.143.16:26656,5f1bcdfe67b0cd55ed12a06454206c7f1ab4b35b@95.216.160.203:26656,d17909ba856a9d6e307a9dcba1c199ab4211101e@46.101.182.62:18656,f38f2ee5ed756a748df20e1ed17ae3894b105849@167.86.115.178:26656,8a0e76b9cdfe2e80bca2e9ea270d57af17cfaf06@65.108.146.240:18656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15556"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.cascadiad/config/config.toml
```
