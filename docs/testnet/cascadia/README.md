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
peers="6f44ab7ad9d6a4366a80c8fd8f904e6ab2f6e535@5.9.48.90:26656,fc698cb2ca4daff21f0e4c377503343cc72dd5eb@64.225.100.42:26656,de11c79dab6ea248fb72f9d93c2ff0eace14a5ac@94.250.201.130:26656,4affb0923e1be1f18818db3ababe682c63f6a1e3@65.109.144.236:30656,5623331ab53459146cbb60efadf42899373f844b@37.27.6.70:26656,f55eaf24fe87dfe4c5feb64ba2e2f5b730901927@185.255.131.190:26656,af8b5486e4938c3bd9ab56fd5ee03d26857089a1@31.220.95.213:26656,d527aed8bb6361293748ff4fcf442d9823b80b59@207.180.229.183:26656,349d92de7d6e23ff4ce6dfbf6628a04da3483245@194.163.155.195:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15556"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.cascadiad/config/config.toml
```
