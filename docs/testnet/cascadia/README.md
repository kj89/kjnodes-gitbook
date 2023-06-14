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
peers="42ec68fe0eeeff1bb0ef64e1ae74c99c8d58c293@78.46.106.75:15656,ba30fc812452dfcf0f82ccdf9c6942a1153682b0@161.97.65.105:18656,c94df794fdee1bf67ac7789a50159390c1580530@38.242.221.76:26656,a8157f96618f0febc42c4e337cd1c42e3958d7ef@38.242.213.35:18656,040d0b6ffefba3283b5763e26c352c7b1b232c1f@65.109.90.171:34656,21ca2712116138429aed3d72422379397c53fa86@65.109.65.248:34656,4b1b5e4a8f3a0cbaf235b13e68184a2d9d376b2b@178.20.44.156:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15556,ad9513b4b05bc5decc678367f0fbdbbed474f8c2@217.76.54.239:18656,9119177769a7fd09447c0c9d819215c15440c6c9@77.120.115.146:15556"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.cascadiad/config/config.toml
```
