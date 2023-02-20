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
peers="8d5eac1042bac34cddd25d7601789fc03cb3f3a9@168.119.213.113:46656,39794289e20cf80eba0a720eed58e7097e5686c1@136.243.103.53:46656,877f82353e8cd6e2586ea37a6d16064eae081a74@192.95.30.128:31656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,c1008d2d05c56254e95d19ab7e9fe459dad2de3d@159.223.57.238:26656,36a242b6f2d779aeea4811e4e4c635a55d5274f1@45.151.123.72:26656,5cb8118bd9f6356e52a6c0a68b2860c28c49f422@34.229.146.239:26656,6011e62596d177073f3bed476622162652ab4310@164.68.105.143:26656,33ed8cb97aa678c7e4578ab39ac93ac94db426bb@95.217.236.79:46656,c70357b388d145471b0e68afe5a1a5c97fe9f38b@109.205.180.254:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
