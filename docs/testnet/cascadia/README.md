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

**live-peers** (10)
```bash
peers="f075e82ca89acfbbd8ef845c95bd3d50574904f5@159.69.110.238:36656,e0dcea0df3c5e31458ba855358b08cc804ddb287@144.91.122.14:26656,85b0fba108b64481b025262c1fea99d32037654b@75.119.147.244:26656,67f25e7edb2fb19bd2a933f5ba7a87a01312eb90@89.117.49.52:26656,21ca2712116138429aed3d72422379397c53fa86@65.109.65.248:34656,040d0b6ffefba3283b5763e26c352c7b1b232c1f@65.109.90.171:34656,e25bf22448e62faca2359985303ec4557f662444@95.217.11.20:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15556,4a9e0815abb9891bc59eef58920d03c47e1b9be0@45.84.0.185:26656,5f1bcdfe67b0cd55ed12a06454206c7f1ab4b35b@95.216.160.203:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.cascadiad/config/config.toml
```
