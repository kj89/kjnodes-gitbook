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
peers="39794289e20cf80eba0a720eed58e7097e5686c1@136.243.103.53:46656,7fc44e2651006fb2ddb4a56132e738da2845715f@65.108.6.45:61256,77791ee9b1eb56682335c451c296f450ee649c01@44.209.89.17:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,258018061069908a045d3777a7a2079588d712cf@38.242.234.6:26656,8e667c0759bfb20ec42b939956706301a4f2a10d@65.109.92.8:26656,747d05bfe9f3e0c2e0462ac351c577699e1d9b8c@207.244.244.194:26656,b1e1e5a9dbf2e03b456668c2f2d9164ae090ba0c@109.123.244.56:46656,4bf2dcaf4620ae8b6ef4e75b5d511e2c8841a840@162.55.39.16:26656,70bab3120f49ce5244bbbf97edffb2d26dca2d8d@185.190.140.74:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
