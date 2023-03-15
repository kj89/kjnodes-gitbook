# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/dymension.png" width="150" alt=""><figcaption></figcaption></figure>

Dymension is a network of modular blockchains called RollApps  and at the center of it all is the Dymension Hub. Dymension  allows anyone to build and deploy their own consensus-free blockchain, a RollApp.

**Chain ID**: 35-C | **Latest Version Tag**: v0.2.0-beta | **Wasm**: OFF

[Website](https://dymension.xyz/) | [Discord](https://discord.gg/dymension) | [Twitter](https://twitter.com/dymensionXYZ)




## Chain explorer
[https://explorer.kjnodes.com/dymension-testnet](https://explorer.kjnodes.com/dymension-testnet)

## Public endpoints

* api: [https://dymension-testnet.api.kjnodes.com](https://dymension-testnet.api.kjnodes.com)
* rpc: [https://dymension-testnet.rpc.kjnodes.com](https://dymension-testnet.rpc.kjnodes.com)
* grpc: dymension-testnet.grpc.kjnodes.com:46090

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

**live-peers** (17)
```bash
peers="80cce834fc749c0a9f47182665f833f97170ff4b@65.108.104.167:46656,7fc44e2651006fb2ddb4a56132e738da2845715f@65.108.6.45:61256,88e09de4c713ecb3497f39f6e6c599aea7a10750@65.109.38.111:20556,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,b473a649e58b49bc62b557e94d35a2c8c0ee9375@95.214.53.46:36656,ee2fa87279bc626f9c979093389bd1d6568d96ff@65.109.37.228:36656,8f84d324a2d266e612d06db4a793b0d001ee62a0@38.146.3.200:20556,0f1045fd8c81a8ad843cf0f96a73ed34865322a7@3.145.180.81:26656,63d971a42e323f9411ef702d1f268f9862781c1f@194.163.165.176:40656,39794289e20cf80eba0a720eed58e7097e5686c1@136.243.103.53:46656,ec843a4aea197837c13f13612a525bd7377443b1@167.235.250.107:26656,56e0f891f8312e239a631aea2f8b0e64c9f7d824@135.181.95.145:36656,b921655e6c66235915e7d4465ea2146e537f13e4@167.235.6.228:26636,877f82353e8cd6e2586ea37a6d16064eae081a74@192.95.30.128:31656,1fa5bb085e8f52c21bc71c39afbba2851bee3e18@43.157.48.181:26656,965694b051742c2da0ea66502dd9bfeea38de265@198.244.228.235:26656,c1008d2d05c56254e95d19ab7e9fe459dad2de3d@159.223.57.238:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
