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
peers="8e667c0759bfb20ec42b939956706301a4f2a10d@65.109.92.8:26656,7fc44e2651006fb2ddb4a56132e738da2845715f@65.108.6.45:61256,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,63d971a42e323f9411ef702d1f268f9862781c1f@194.163.165.176:40656,0996622e0d51b51cdfb2e8bed752968693f87e10@109.205.180.254:26656,965694b051742c2da0ea66502dd9bfeea38de265@198.244.228.235:26656,747d05bfe9f3e0c2e0462ac351c577699e1d9b8c@207.244.244.194:26656,3c937029e41e3f7b92b8b87d787be0ddc2a3f13c@70.34.214.236:26656,35e67a6199b44a58697653a14b6ca9c75974c57d@89.117.56.126:24756,fe02e0280c6aedfeaea6f0d8e828dbc53f34e69a@91.107.232.129:26656,ba2ef45240cc997443df795b801a34602ba68b55@65.109.92.241:17886,55f233c7c4bea21a47d266921ca5fce657f3adf7@168.119.240.200:26656,f433653cef597b3f0dd5f4e3e46c05fd121246bb@95.216.149.50:26656,8f84d324a2d266e612d06db4a793b0d001ee62a0@38.146.3.200:20556,77791ee9b1eb56682335c451c296f450ee649c01@44.209.89.17:26656,b8d08951d68da03af8f9272bf77684811197c289@95.216.41.160:26656,6cf94ed068c7401ba8e6f9a49143fd90df415e83@195.201.237.198:46656,ae509356c743a12259248fa8df23e42dae885e05@78.46.84.144:26656,43426e98064694d407b2165fb24d52980d38f1c9@88.99.3.158:20556"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
