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
peers="ba30fc812452dfcf0f82ccdf9c6942a1153682b0@161.97.65.105:18656,e998e27320bbef8f008cce775f7ca353f6434770@212.90.121.110:26656,c2ef0140958982dae978e8830003158bade2a1c6@185.249.225.63:26656,5f1bcdfe67b0cd55ed12a06454206c7f1ab4b35b@95.216.160.203:26656,32bcc51674dd83a316323a67918c1cee25163291@65.109.72.12:26656,5d563f5d882904f89b929fde2d1cf2342c8cba7c@185.209.223.64:36656,a43ea5363065a8a485488d06b2b4e2a971011d7a@95.111.234.147:18656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15556,8a5caaaad14a554d71a8765e71b9f61da099efe2@65.109.39.113:26656,8c3848f0f610b6fb82e4861660162b2fdabe755b@185.193.66.217:26656,d3e1ce95ac1e2830296eff1c952b89d6c3d84f7a@217.197.117.53:61256"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.cascadiad/config/config.toml
```
