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
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,77791ee9b1eb56682335c451c296f450ee649c01@44.209.89.17:26656,018cc15aa343bfc1054f83da520324ce84a4e537@88.99.161.162:19656,965694b051742c2da0ea66502dd9bfeea38de265@198.244.228.235:26656,8e667c0759bfb20ec42b939956706301a4f2a10d@65.109.92.8:26656,7fc44e2651006fb2ddb4a56132e738da2845715f@65.108.6.45:61256,ee2fa87279bc626f9c979093389bd1d6568d96ff@65.109.37.228:36656,1fa5bb085e8f52c21bc71c39afbba2851bee3e18@43.157.48.181:26656,3a8bb83d5c5afb13ae2c1c3b91c97928e277f6a5@142.132.205.94:15658,0d30a0790a216d01c9759ab48192d9154381e6c0@136.243.88.91:3240"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
