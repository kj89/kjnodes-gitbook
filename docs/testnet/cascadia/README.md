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
peers="349d92de7d6e23ff4ce6dfbf6628a04da3483245@194.163.155.195:26656,5d563f5d882904f89b929fde2d1cf2342c8cba7c@185.209.223.64:36656,4affb0923e1be1f18818db3ababe682c63f6a1e3@65.109.144.236:30656,fd92709f34b393b01b329c11dc0c41c7c4a2fcef@65.21.200.54:38656,d10fae49b6fa0a3dbfdca205807f79b3d53ece98@94.103.92.112:26656,c9256e4f42a23bbdc9ea79805f497a1923a4beac@65.108.230.113:17096,30408b285f4989484dff0a273d5221c583e5eff3@164.92.82.243:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15556,793f9456b853f0d36e8e9636dcad5cc27a169292@91.230.110.100:26656,11af344d9db6f971aed22a873a6a69a3ff2c6db8@86.48.2.121:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.cascadiad/config/config.toml
```
