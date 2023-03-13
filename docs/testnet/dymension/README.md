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

**live-peers** (18)
```bash
peers="63d971a42e323f9411ef702d1f268f9862781c1f@194.163.165.176:40656,80cce834fc749c0a9f47182665f833f97170ff4b@65.108.104.167:46656,8e667c0759bfb20ec42b939956706301a4f2a10d@65.109.92.8:26656,ee2fa87279bc626f9c979093389bd1d6568d96ff@65.109.37.228:36656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,6cf94ed068c7401ba8e6f9a49143fd90df415e83@195.201.237.198:46656,35e67a6199b44a58697653a14b6ca9c75974c57d@89.117.56.126:24756,8f84d324a2d266e612d06db4a793b0d001ee62a0@38.146.3.200:20556,ec843a4aea197837c13f13612a525bd7377443b1@167.235.250.107:26656,e46b42d50947795f681cf9bfd601ae806e7a8d49@188.34.178.190:46656,77791ee9b1eb56682335c451c296f450ee649c01@44.209.89.17:26656,55f233c7c4bea21a47d266921ca5fce657f3adf7@168.119.240.200:26656,0f1045fd8c81a8ad843cf0f96a73ed34865322a7@3.145.180.81:26656,a85420b25181bdb9b3a38741c48dafd5fb3b922f@209.34.206.42:26656,43426e98064694d407b2165fb24d52980d38f1c9@88.99.3.158:20556,747d05bfe9f3e0c2e0462ac351c577699e1d9b8c@207.244.244.194:26656,3c937029e41e3f7b92b8b87d787be0ddc2a3f13c@70.34.214.236:26656,965694b051742c2da0ea66502dd9bfeea38de265@198.244.228.235:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
