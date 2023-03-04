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

**live-peers** (14)
```bash
peers="6204710a0d089566b6df85ae4aee595afdd23cbb@146.190.40.115:26656,b921655e6c66235915e7d4465ea2146e537f13e4@167.235.6.228:26636,48bdb78c51e56b651c938d075e1077dab2c6197c@43.157.22.223:26656,4d2ec1e61d61550fc5bfacc57e971ff9b6181152@135.181.180.29:26656,488a1665d94f257733b04f7b4fbcef058cbb11cd@65.108.199.206:31656,965694b051742c2da0ea66502dd9bfeea38de265@198.244.228.235:26656,77791ee9b1eb56682335c451c296f450ee649c01@44.209.89.17:26656,877f82353e8cd6e2586ea37a6d16064eae081a74@192.95.30.128:31656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,0996622e0d51b51cdfb2e8bed752968693f87e10@109.205.180.254:26656,f11d87d4d7ed4497b446b0071ca59096126da671@165.22.96.174:26656,3c937029e41e3f7b92b8b87d787be0ddc2a3f13c@70.34.214.236:26656,4bf2dcaf4620ae8b6ef4e75b5d511e2c8841a840@162.55.39.16:26656,39794289e20cf80eba0a720eed58e7097e5686c1@136.243.103.53:46656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
