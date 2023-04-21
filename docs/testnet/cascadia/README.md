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
peers="2a7eae11dc3af3d70b295e6d1e61412a4ffb8d97@136.243.103.32:26656,6caf73a184fdec6f2b5ec43fe1218e4bd6c2bee9@178.63.52.213:36656,45d9fba9830260e6ee302ab3b3802f354aa3e5d8@65.109.69.240:36656,138c612b4297a5c089e4a8653b670c4dcb2ab79f@5.161.86.210:11656,36ca8d32631eeb973322aec9b8a9b810d5344cd4@91.201.113.194:56656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:55656,ad417c4efa59e21b43e8e256c73b9939f1c22a0e@23.88.42.28:31656,b71287a85b70df75e1405c6831634738e6b957ab@65.108.72.253:15656,3314288924c02fd0c983ef99cf2d1d607b620b80@46.4.90.188:26656,893b6d4be8b527b0eb1ab4c1b2f0128945f5b241@185.213.27.91:36656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.cascadiad/config/config.toml
```
