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
peers="b921655e6c66235915e7d4465ea2146e537f13e4@167.235.6.228:26636,ee2fa87279bc626f9c979093389bd1d6568d96ff@65.109.37.228:36656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,e1d6bdf47f76bdfdba90d4bedc780539d9766bbe@172.104.199.176:26656,e5226fa166386f9055908194a4942c06b7003ab5@65.108.192.123:42656,ba2ef45240cc997443df795b801a34602ba68b55@65.109.92.241:17886,258018061069908a045d3777a7a2079588d712cf@38.242.234.6:26656,c1008d2d05c56254e95d19ab7e9fe459dad2de3d@159.223.57.238:26656,77791ee9b1eb56682335c451c296f450ee649c01@44.209.89.17:26656,9b90de7b55ac060d618786f478ee7d79256a8429@51.255.67.78:26701"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
