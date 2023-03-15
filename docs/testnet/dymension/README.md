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
peers="4c25618c9465c0aaea91d936be446d5db04be3d1@195.201.237.185:46656,88e09de4c713ecb3497f39f6e6c599aea7a10750@65.109.38.111:20556,b473a649e58b49bc62b557e94d35a2c8c0ee9375@95.214.53.46:36656,ec843a4aea197837c13f13612a525bd7377443b1@167.235.250.107:26656,4d2ec1e61d61550fc5bfacc57e971ff9b6181152@135.181.180.29:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,ae509356c743a12259248fa8df23e42dae885e05@78.46.84.144:26656,c1008d2d05c56254e95d19ab7e9fe459dad2de3d@159.223.57.238:26656,8f84d324a2d266e612d06db4a793b0d001ee62a0@38.146.3.200:20556,877f82353e8cd6e2586ea37a6d16064eae081a74@192.95.30.128:31656,7fc44e2651006fb2ddb4a56132e738da2845715f@65.108.6.45:61256,d4a66d01b1d109d842a7f1d51f541033c653ea03@116.202.227.117:46656,ee2fa87279bc626f9c979093389bd1d6568d96ff@65.109.37.228:36656,77791ee9b1eb56682335c451c296f450ee649c01@44.209.89.17:26656,63d971a42e323f9411ef702d1f268f9862781c1f@194.163.165.176:40656,56e0f891f8312e239a631aea2f8b0e64c9f7d824@135.181.95.145:36656,547cf669555bd611ba57b37bb0f288793ea4ec49@141.94.138.48:26673,80cce834fc749c0a9f47182665f833f97170ff4b@65.108.104.167:46656,36a242b6f2d779aeea4811e4e4c635a55d5274f1@45.151.123.72:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
