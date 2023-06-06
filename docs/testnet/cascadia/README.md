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
peers="0afb151c68024f54a88671a6bd677437d28ff270@65.108.243.99:26656,417e5565608968e10c88be36b13fcb03e00e48ee@95.217.199.48:26656,2df457ff41088898610484152207f35a945220b8@65.109.227.154:18656,1fa47c9fa214bcd7b6c2f900b11f831371c411e3@31.220.87.33:26656,32d5f7b07655421ff71a459fd85e77c62a8277b8@94.26.141.111:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15556,3c11edc1470d8affafc275761bd97483193b4df8@161.97.74.13:26656,4023a7cb78b2d3cadd3dc186a0a7735c09cd7c33@38.242.129.4:18656,2f0f98db7eb4addb2895085962c70f1fde29f80d@217.76.50.195:26656,d3e1ce95ac1e2830296eff1c952b89d6c3d84f7a@217.197.117.53:61256,96fa0a28f5ca7f0263e91ce81be554f7ebb1d85a@167.114.172.204:55656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.cascadiad/config/config.toml
```
