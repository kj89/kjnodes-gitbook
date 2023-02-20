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
peers="6c0ddab56755cd010f65f1f1201d29120a2d9092@38.242.202.200:31656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,77c42c2b2702437981976f7a648c26cd37911f7b@65.108.9.230:46656,77791ee9b1eb56682335c451c296f450ee649c01@44.209.89.17:26656,7fc44e2651006fb2ddb4a56132e738da2845715f@65.108.6.45:61256,39794289e20cf80eba0a720eed58e7097e5686c1@136.243.103.53:46656,877f82353e8cd6e2586ea37a6d16064eae081a74@192.95.30.128:31656,8d5eac1042bac34cddd25d7601789fc03cb3f3a9@168.119.213.113:46656,869d03182da215ae0171ac37ee69a77ed59d1a38@135.181.253.11:46656,c1008d2d05c56254e95d19ab7e9fe459dad2de3d@159.223.57.238:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
