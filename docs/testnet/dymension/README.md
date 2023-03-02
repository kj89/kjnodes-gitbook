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

**live-peers** (19)
```bash
peers="147a0021cff3c34251adb3ad7194574011fa3192@176.57.189.36:11656,76fb074cb54791afa399979ca863da211404bad6@65.109.86.236:27656,43a46e2fbe871246e8fee045749d0a4677042b0c@95.217.216.88:46656,77791ee9b1eb56682335c451c296f450ee649c01@44.209.89.17:26656,7b4621b7744a2c3ea5ec9453980e1d555109a746@139.162.138.158:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,6204710a0d089566b6df85ae4aee595afdd23cbb@146.190.40.115:26656,48bdb78c51e56b651c938d075e1077dab2c6197c@43.157.22.223:26656,3c937029e41e3f7b92b8b87d787be0ddc2a3f13c@70.34.214.236:26656,c1008d2d05c56254e95d19ab7e9fe459dad2de3d@159.223.57.238:26656,74cfbc9e923784d1ca73188053561ea8b09e13d4@146.190.127.9:26656,6cf94ed068c7401ba8e6f9a49143fd90df415e83@195.201.237.198:46656,acb69c31cac6140a1a9570e683de5e26dd008cff@51.222.44.116:32656,8e667c0759bfb20ec42b939956706301a4f2a10d@65.109.92.8:26656,48ea1c8c62e9eb193a317096339b22f4a4452c8c@185.144.99.22:26656,36a242b6f2d779aeea4811e4e4c635a55d5274f1@45.151.123.72:26656,e46b42d50947795f681cf9bfd601ae806e7a8d49@188.34.178.190:46656,af6787b3273dd60e0f809c7e5e2a2a9fd379045e@195.201.195.61:27656,965694b051742c2da0ea66502dd9bfeea38de265@198.244.228.235:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
