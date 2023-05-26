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
peers="780b02fd73b698834c4cdd0c7d7123586b71ece1@209.38.243.102:18656,a48a05eeab4265e92cf8d4cb8fbd5c27829f5fe6@144.91.94.88:26656,4ec51eeff609e98100beb77bfb34fec9add6057d@45.14.194.130:18656,2f0f98db7eb4addb2895085962c70f1fde29f80d@217.76.50.195:26656,bd798e85f2e58cd0da70e6266014841dd79aaf04@65.109.160.90:18656,2fb0a8dd1c16b363d779229ab009479e0e60b7c1@95.129.57.179:36656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15556,77ae41601b06b3ca611e51047df04d3e35908aff@5.78.79.229:18656,cd9b30d8839e0633249ab9b5e00eb9544cdf701d@65.109.122.93:26656,cf1a8643134d7c5378d7af1e426e1ada46881f6c@5.78.78.201:18656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.cascadiad/config/config.toml
```
