# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/dymension.png" width="150" alt=""><figcaption></figcaption></figure>

Dymension is a network of modular blockchains called RollApps  and at the center of it all is the Dymension Hub. Dymension  allows anyone to build and deploy their own consensus-free blockchain, a RollApp.

**Chain ID**: 35-C | **Latest Version Tag**: v0.2.0-beta | **Wasm**: OFF

[Website](https://dymension.xyz/) | [Discord](https://discord.gg/dymension) | [Twitter](https://twitter.com/dymensionXYZ)




## Chain explorer
[https://explorer.kjnodes.com/dymension-testnet](https://explorer.kjnodes.com/dymension-testnet)

## Public endpoints

* api: [https://dymension-testnet.api.kjnodes.com](https://dymension-testnet.api.kjnodes.com)
* rpc: [https://dymension-testnet.rpc.kjnodes.com](https://dymension-testnet.rpc.kjnodes.com)
* grpc: [https://dymension-testnet.grpc.kjnodes.com](https://dymension-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@dymension-testnet.rpc.kjnodes.com:46656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@dymension-testnet.rpc.kjnodes.com:46659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/dymension-testnet/addrbook.json > $HOME/.dymension/config/addrbook.json
```

**live-peers** (10)
```bash
peers="e5226fa166386f9055908194a4942c06b7003ab5@65.108.192.123:42656,76fb074cb54791afa399979ca863da211404bad6@65.109.86.236:27656,747d05bfe9f3e0c2e0462ac351c577699e1d9b8c@207.244.244.194:26656,af97c76448e6a5d7671c6523f38fc48cc7273da7@217.76.59.46:26656,5cb8118bd9f6356e52a6c0a68b2860c28c49f422@34.229.146.239:26656,77791ee9b1eb56682335c451c296f450ee649c01@44.209.89.17:26656,f8175ce7bc19d015ec17083fe19b80eae2bd2a9c@65.21.239.60:46656,0996622e0d51b51cdfb2e8bed752968693f87e10@109.205.180.254:26656,139340424dddf85e54e0a54179d06875013e1e39@65.109.87.88:24656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
