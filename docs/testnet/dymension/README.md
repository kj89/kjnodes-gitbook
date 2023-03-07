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

**live-peers** (21)
```bash
peers="48ea1c8c62e9eb193a317096339b22f4a4452c8c@185.144.99.22:26656,80cce834fc749c0a9f47182665f833f97170ff4b@65.108.104.167:46656,ee2fa87279bc626f9c979093389bd1d6568d96ff@65.109.37.228:36656,a85420b25181bdb9b3a38741c48dafd5fb3b922f@209.34.206.42:26656,55f233c7c4bea21a47d266921ca5fce657f3adf7@168.119.240.200:26656,65242d54d20a6c16a401004a8fb936343d9cae99@65.109.106.91:26656,7fc44e2651006fb2ddb4a56132e738da2845715f@65.108.6.45:61256,36a242b6f2d779aeea4811e4e4c635a55d5274f1@45.151.123.72:26656,965694b051742c2da0ea66502dd9bfeea38de265@198.244.228.235:26656,b8d08951d68da03af8f9272bf77684811197c289@95.216.41.160:26656,747d05bfe9f3e0c2e0462ac351c577699e1d9b8c@207.244.244.194:26656,63d971a42e323f9411ef702d1f268f9862781c1f@194.163.165.176:40656,8f84d324a2d266e612d06db4a793b0d001ee62a0@38.146.3.200:20556,6204710a0d089566b6df85ae4aee595afdd23cbb@146.190.40.115:26656,e46b42d50947795f681cf9bfd601ae806e7a8d49@188.34.178.190:46656,5cb8118bd9f6356e52a6c0a68b2860c28c49f422@34.229.146.239:26656,5d689e09a129c03c003f05850262f03b2433a384@51.79.30.141:26656,ec843a4aea197837c13f13612a525bd7377443b1@167.235.250.107:26656,ba2ef45240cc997443df795b801a34602ba68b55@65.109.92.241:17886,6b00d8b9ad49cc2aa8d76416613bbbb10e6f56f7@65.109.108.150:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
