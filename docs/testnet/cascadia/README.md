# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/cascadia.png" width="150" alt=""><figcaption></figcaption></figure>

Cascadia is a layer-1 blockchain built to explore the  nature of incentives on network effects, starting  with ve-tokenomics.

**Chain ID**: cascadia_6102-1 | **Latest Version Tag**: v0.1.1 | **Wasm**: OFF

[Website](https://www.cascadia.foundation) | [Discord](https://discord.gg/cascadia) | [Twitter](https://twitter.com/CascadiaSystems)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/cascadia-testnet](https://explorer.kjnodes.com/cascadia-testnet)

## Public endpoints

* api: [https://cascadia-testnet.api.kjnodes.com](https://cascadia-testnet.api.kjnodes.com)
* rpc: [https://cascadia-testnet.rpc.kjnodes.com](https://cascadia-testnet.rpc.kjnodes.com)
* grpc: cascadia-testnet.grpc.kjnodes.com:55090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@cascadia-testnet.rpc.kjnodes.com:55656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@cascadia-testnet.rpc.kjnodes.com:55659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/cascadia-testnet/addrbook.json > $HOME/.cascadiad/config/addrbook.json
```

**live-peers** (10)
```bash
peers="d1469dbfc3becdf0ec1640d6812793f6d33a6eda@5.9.121.55:41956,ad417c4efa59e21b43e8e256c73b9939f1c22a0e@23.88.42.28:31656,f075e82ca89acfbbd8ef845c95bd3d50574904f5@159.69.110.238:36656,c6e3921222655345d8296353994e917f13a1b4a1@65.109.92.79:40656,21ca2712116138429aed3d72422379397c53fa86@65.109.65.248:34656,45d9fba9830260e6ee302ab3b3802f354aa3e5d8@65.109.69.240:36656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:55656,de11c79dab6ea248fb72f9d93c2ff0eace14a5ac@94.250.201.130:26656,f53586a6b4f77f3fea3f61fde904be3c8956f6e3@31.220.74.8:26656,b71287a85b70df75e1405c6831634738e6b957ab@65.108.72.253:15656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.cascadiad/config/config.toml
```
