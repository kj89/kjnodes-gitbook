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

**live-peers** (20)
```bash
peers="e46b42d50947795f681cf9bfd601ae806e7a8d49@188.34.178.190:46656,547cf669555bd611ba57b37bb0f288793ea4ec49@141.94.138.48:26673,dddc76ca6279ac90b12cf35b39c46a2fc2c2ce52@5.161.78.48:46656,acb69c31cac6140a1a9570e683de5e26dd008cff@51.222.44.116:32656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,56e0f891f8312e239a631aea2f8b0e64c9f7d824@135.181.95.145:36656,88e09de4c713ecb3497f39f6e6c599aea7a10750@65.109.38.111:20556,63d971a42e323f9411ef702d1f268f9862781c1f@194.163.165.176:40656,af97c76448e6a5d7671c6523f38fc48cc7273da7@217.76.59.46:26656,94b63fddfc78230f51aeb7ac34b9fb86bd042a77@146.19.24.43:30585,ae509356c743a12259248fa8df23e42dae885e05@78.46.84.144:26656,7fc44e2651006fb2ddb4a56132e738da2845715f@65.108.6.45:61256,6ebe5856a7617cb9309a923a3935687903d2607d@141.95.97.28:15256,965694b051742c2da0ea66502dd9bfeea38de265@198.244.228.235:26656,8f84d324a2d266e612d06db4a793b0d001ee62a0@38.146.3.200:20556,f433653cef597b3f0dd5f4e3e46c05fd121246bb@95.216.149.50:26656,3c937029e41e3f7b92b8b87d787be0ddc2a3f13c@70.34.214.236:26656,0f1045fd8c81a8ad843cf0f96a73ed34865322a7@3.145.180.81:26656,39794289e20cf80eba0a720eed58e7097e5686c1@136.243.103.53:46656,488a1665d94f257733b04f7b4fbcef058cbb11cd@65.108.199.206:31656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
