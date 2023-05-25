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
peers="b46b4294d80ef0d197e33cc94c6bd57fe5bce3f9@138.201.155.226:19656,349d92de7d6e23ff4ce6dfbf6628a04da3483245@194.163.155.195:26656,dd6836e921c1ddc7b87d8c3dd87929dab80a9aaf@77.105.138.110:26656,47058eb9ee90cfb0b994a4a82767d3844934ee39@65.108.41.155:26656,950f69c2e21b39357c1aad3ddbb654ac2de4bb3d@161.97.134.203:18656,fc80d9960383e9b441d5217550bf7cbcd2aacbca@38.242.154.155:18656,475a271d79a41a952a83e914ff3c1d59fa48e76b@5.180.186.25:18656,fdc2bb3b58a6e4a376f58b87e5e4510af00776d8@45.67.217.22:18656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15556,17391122b771491e041064f10014fcdc840d89b0@95.217.105.22:18656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.cascadiad/config/config.toml
```
