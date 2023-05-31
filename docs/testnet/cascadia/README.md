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
peers="ba30fc812452dfcf0f82ccdf9c6942a1153682b0@161.97.65.105:18656,a4fa41f9104a77cbf5310e3890a64499b8e866e4@91.230.110.190:26656,8ec57a5df11286f36908cce951edb730ce188ea2@86.48.1.140:55656,21ca2712116138429aed3d72422379397c53fa86@65.109.65.248:34656,5623331ab53459146cbb60efadf42899373f844b@37.27.6.70:26656,794f20c290e46840479a51f760e67adbfb6915e2@65.109.137.4:18656,fdc2bb3b58a6e4a376f58b87e5e4510af00776d8@45.67.217.22:18656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15556,7747e3e580aab42827a947cad5f1ccd7d9530954@149.102.139.80:26656,11af344d9db6f971aed22a873a6a69a3ff2c6db8@86.48.2.121:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.cascadiad/config/config.toml
```
