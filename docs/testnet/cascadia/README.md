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
peers="2aa27e0a6952b333b06df43d071126de2f4ce490@185.182.185.171:26656,af8b5486e4938c3bd9ab56fd5ee03d26857089a1@31.220.95.213:26656,4ead67f38f3163a5c849333faaaf760b6d9eda8e@185.237.253.88:26656,47058eb9ee90cfb0b994a4a82767d3844934ee39@65.108.41.155:26656,c9256e4f42a23bbdc9ea79805f497a1923a4beac@65.108.230.113:17096,48a9d7407149515b40206aedeb489ea82518e839@5.189.185.27:18656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15556,565899a1b074310c8e7acb9924fbe65cb04c8e33@185.229.119.8:26656,475a271d79a41a952a83e914ff3c1d59fa48e76b@5.180.186.25:18656,68aacce2ffd504c14ed811b4b7d5de40b2c35d35@194.163.160.127:18656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.cascadiad/config/config.toml
```
