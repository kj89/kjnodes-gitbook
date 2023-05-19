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
peers="5e00a5323aa21b54669be868f2d2ab1e9d581207@135.181.183.62:18656,cf6a547ccbf10e9461dae917c118fdd50bdd3ff8@149.102.154.1:18656,4165e807320f795900f6e590f90be16a76a7ed94@65.109.174.94:18656,cf1a8643134d7c5378d7af1e426e1ada46881f6c@5.78.78.201:18656,5623331ab53459146cbb60efadf42899373f844b@37.27.6.70:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15556,380341a9ce9d81af66b6628217fe5c953cd8edd1@167.86.83.127:26656,21ca2712116138429aed3d72422379397c53fa86@65.109.65.248:34656,de11c79dab6ea248fb72f9d93c2ff0eace14a5ac@94.250.201.130:26656,0dd9fd700c09030a926d333662493b0d334bc6c5@38.242.146.228:18656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.cascadiad/config/config.toml
```
