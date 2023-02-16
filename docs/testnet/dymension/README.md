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
peers="1ed89bd1d280c4c6eb7d9134bb238d97fbb3f4b2@88.99.104.180:36656,be789ab36bc298b491735f2313d5f99abf452d1f@162.55.246.165:26656,e5226fa166386f9055908194a4942c06b7003ab5@65.108.192.123:42656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,7fc44e2651006fb2ddb4a56132e738da2845715f@65.108.6.45:61256,77791ee9b1eb56682335c451c296f450ee649c01@44.209.89.17:26656,f11d87d4d7ed4497b446b0071ca59096126da671@165.22.96.174:26656,a85420b25181bdb9b3a38741c48dafd5fb3b922f@209.34.206.42:26656,0ee31ef97ba6b6c13b25b5c528163f2092821c2d@65.21.132.27:24856,94b63fddfc78230f51aeb7ac34b9fb86bd042a77@146.19.24.43:30585"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
