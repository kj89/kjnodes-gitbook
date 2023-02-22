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
peers="ec843a4aea197837c13f13612a525bd7377443b1@167.235.250.107:26656,6ebe5856a7617cb9309a923a3935687903d2607d@141.95.97.28:15256,6c0ddab56755cd010f65f1f1201d29120a2d9092@38.242.202.200:31656,b8d08951d68da03af8f9272bf77684811197c289@95.216.41.160:26656,77791ee9b1eb56682335c451c296f450ee649c01@44.209.89.17:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,9e1ea4938f0112c1477827344e2f9d0792710575@185.252.232.189:30656,c5db84267f7dce8fa249b0d5365d59a7abeb0164@95.217.211.32:46656,65242d54d20a6c16a401004a8fb936343d9cae99@65.109.106.91:26656,258018061069908a045d3777a7a2079588d712cf@38.242.234.6:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
