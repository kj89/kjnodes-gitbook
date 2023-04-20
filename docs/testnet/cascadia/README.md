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
peers="f075e82ca89acfbbd8ef845c95bd3d50574904f5@159.69.110.238:36656,5d563f5d882904f89b929fde2d1cf2342c8cba7c@185.209.223.64:36656,1d61222b7b8e180aacebfd57fbd2d8ab95ebdc4c@65.109.93.152:35656,24c3bd618c6c6c0df40968382e6b408429a020c7@95.217.217.253:50656,45d9fba9830260e6ee302ab3b3802f354aa3e5d8@65.109.69.240:36656,5623331ab53459146cbb60efadf42899373f844b@37.27.6.70:26656,330ca39af5825785df4f863fed4cb2194d2b9dbc@149.102.141.140:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:55656,138c612b4297a5c089e4a8653b670c4dcb2ab79f@5.161.86.210:11656,c9256e4f42a23bbdc9ea79805f497a1923a4beac@65.108.230.113:17096"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.cascadiad/config/config.toml
```
