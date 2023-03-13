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
peers="e46b42d50947795f681cf9bfd601ae806e7a8d49@188.34.178.190:46656,55f233c7c4bea21a47d266921ca5fce657f3adf7@168.119.240.200:26656,63d971a42e323f9411ef702d1f268f9862781c1f@194.163.165.176:40656,6c0ddab56755cd010f65f1f1201d29120a2d9092@38.242.202.200:31656,88e09de4c713ecb3497f39f6e6c599aea7a10750@65.109.38.111:20556,ec843a4aea197837c13f13612a525bd7377443b1@167.235.250.107:26656,3c937029e41e3f7b92b8b87d787be0ddc2a3f13c@70.34.214.236:26656,94b63fddfc78230f51aeb7ac34b9fb86bd042a77@146.19.24.43:30585,869d03182da215ae0171ac37ee69a77ed59d1a38@135.181.253.11:46656,56e0f891f8312e239a631aea2f8b0e64c9f7d824@135.181.95.145:36656,7fc44e2651006fb2ddb4a56132e738da2845715f@65.108.6.45:61256,4d2ec1e61d61550fc5bfacc57e971ff9b6181152@135.181.180.29:26656,6204710a0d089566b6df85ae4aee595afdd23cbb@146.190.40.115:26656,965694b051742c2da0ea66502dd9bfeea38de265@198.244.228.235:26656,f433653cef597b3f0dd5f4e3e46c05fd121246bb@95.216.149.50:26656,015c628c6975befaaec912a88f19c0566f37173e@95.217.133.45:46656,1ed89bd1d280c4c6eb7d9134bb238d97fbb3f4b2@88.99.104.180:36656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,8e667c0759bfb20ec42b939956706301a4f2a10d@65.109.92.8:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
