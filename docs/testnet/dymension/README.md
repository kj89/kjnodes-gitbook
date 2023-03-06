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
peers="9e1ea4938f0112c1477827344e2f9d0792710575@185.252.232.189:30656,63d971a42e323f9411ef702d1f268f9862781c1f@194.163.165.176:40656,35e67a6199b44a58697653a14b6ca9c75974c57d@89.117.56.126:24756,f433653cef597b3f0dd5f4e3e46c05fd121246bb@95.216.149.50:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,77791ee9b1eb56682335c451c296f450ee649c01@44.209.89.17:26656,39794289e20cf80eba0a720eed58e7097e5686c1@136.243.103.53:46656,965694b051742c2da0ea66502dd9bfeea38de265@198.244.228.235:26656,8f84d324a2d266e612d06db4a793b0d001ee62a0@38.146.3.200:20556,0ee31ef97ba6b6c13b25b5c528163f2092821c2d@65.21.132.27:24856,6c0ddab56755cd010f65f1f1201d29120a2d9092@38.242.202.200:31656,b8d08951d68da03af8f9272bf77684811197c289@95.216.41.160:26656,55f233c7c4bea21a47d266921ca5fce657f3adf7@168.119.240.200:26656,36a242b6f2d779aeea4811e4e4c635a55d5274f1@45.151.123.72:26656,7fc44e2651006fb2ddb4a56132e738da2845715f@65.108.6.45:61256,0996622e0d51b51cdfb2e8bed752968693f87e10@109.205.180.254:26656,43a46e2fbe871246e8fee045749d0a4677042b0c@95.217.216.88:46656,6204710a0d089566b6df85ae4aee595afdd23cbb@146.190.40.115:26656,ba2ef45240cc997443df795b801a34602ba68b55@65.109.92.241:17886"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
