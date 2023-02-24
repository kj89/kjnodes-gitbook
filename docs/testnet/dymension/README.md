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
peers="7c5507fbb33f846c0d8860ca80833a4d6602360a@185.197.251.5:46656,488a1665d94f257733b04f7b4fbcef058cbb11cd@65.108.199.206:31656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,43a46e2fbe871246e8fee045749d0a4677042b0c@95.217.216.88:46656,77791ee9b1eb56682335c451c296f450ee649c01@44.209.89.17:26656,9e1ea4938f0112c1477827344e2f9d0792710575@185.252.232.189:30656,7fc44e2651006fb2ddb4a56132e738da2845715f@65.108.6.45:61256,258018061069908a045d3777a7a2079588d712cf@38.242.234.6:26656,c5db84267f7dce8fa249b0d5365d59a7abeb0164@95.217.211.32:46656,f11d87d4d7ed4497b446b0071ca59096126da671@165.22.96.174:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
