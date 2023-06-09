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

**live-peers** (12)
```bash
peers="77319825e184e924bd30c5bcd0a3dc0abf181f31@178.63.26.94:55656,de11c79dab6ea248fb72f9d93c2ff0eace14a5ac@94.250.201.130:26656,9b001d0659be174ae662709e3cbcd8c6b1d3254d@184.174.33.18:26656,cd9b30d8839e0633249ab9b5e00eb9544cdf701d@65.109.122.93:26656,c6e3921222655345d8296353994e917f13a1b4a1@65.109.92.79:40656,4acd189e415b563c486fb6063410c23ea75f4971@38.242.139.243:55656,2fb0a8dd1c16b363d779229ab009479e0e60b7c1@95.129.57.179:36656,d3e1ce95ac1e2830296eff1c952b89d6c3d84f7a@217.197.117.53:61256,e998e27320bbef8f008cce775f7ca353f6434770@212.90.121.110:26656,7c6d883b40b52ac245f74555a9d8cdcf9419ebaa@65.21.7.51:26656,97a5c1de5dc145baf35e92ad56cd8015a3d4c2bb@45.10.154.249:18656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15556"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.cascadiad/config/config.toml
```
