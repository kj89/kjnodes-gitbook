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
peers="cba6972c94694648181ffa9492e46cd5e2d9d7ac@34.32.130.159:26656,a48a05eeab4265e92cf8d4cb8fbd5c27829f5fe6@144.91.94.88:26656,e10667304e9a3ccdc8139e49f4e3fad7d1f9f454@89.117.51.248:18656,740b9d21195a434f10efd7796ea1406e6a713247@149.102.143.16:26656,565899a1b074310c8e7acb9924fbe65cb04c8e33@185.229.119.8:26656,e998e27320bbef8f008cce775f7ca353f6434770@212.90.121.110:26656,2c06556bb9c65ef272d76d869ac405212f1975dc@31.220.92.243:26656,2f0f98db7eb4addb2895085962c70f1fde29f80d@217.76.50.195:26656,cc42f2077c770816514e0e4d3076189d743752a2@65.109.163.85:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15556,d3e1ce95ac1e2830296eff1c952b89d6c3d84f7a@217.197.117.53:61256"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.cascadiad/config/config.toml
```
