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
peers="f433653cef597b3f0dd5f4e3e46c05fd121246bb@95.216.149.50:26656,65242d54d20a6c16a401004a8fb936343d9cae99@65.109.106.91:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,ec843a4aea197837c13f13612a525bd7377443b1@167.235.250.107:26656,965694b051742c2da0ea66502dd9bfeea38de265@198.244.228.235:26656,80cce834fc749c0a9f47182665f833f97170ff4b@65.108.104.167:46656,77791ee9b1eb56682335c451c296f450ee649c01@44.209.89.17:26656,63d971a42e323f9411ef702d1f268f9862781c1f@194.163.165.176:40656,0996622e0d51b51cdfb2e8bed752968693f87e10@109.205.180.254:26656,6204710a0d089566b6df85ae4aee595afdd23cbb@146.190.40.115:26656,d4a66d01b1d109d842a7f1d51f541033c653ea03@116.202.227.117:46656,8f84d324a2d266e612d06db4a793b0d001ee62a0@38.146.3.200:20556,747d05bfe9f3e0c2e0462ac351c577699e1d9b8c@207.244.244.194:26656,5d689e09a129c03c003f05850262f03b2433a384@51.79.30.141:26656,3c937029e41e3f7b92b8b87d787be0ddc2a3f13c@70.34.214.236:26656,e5226fa166386f9055908194a4942c06b7003ab5@65.108.192.123:42656,b8d08951d68da03af8f9272bf77684811197c289@95.216.41.160:26656,55f233c7c4bea21a47d266921ca5fce657f3adf7@168.119.240.200:26656,36a242b6f2d779aeea4811e4e4c635a55d5274f1@45.151.123.72:26656,39794289e20cf80eba0a720eed58e7097e5686c1@136.243.103.53:46656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
