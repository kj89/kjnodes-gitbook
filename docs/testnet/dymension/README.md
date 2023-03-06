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

**live-peers** (20)
```bash
peers="7fc44e2651006fb2ddb4a56132e738da2845715f@65.108.6.45:61256,c7a36d7abeea5704290f99c1608b50ff1f5e3e47@79.143.188.183:26656,8e667c0759bfb20ec42b939956706301a4f2a10d@65.109.92.8:26656,43a46e2fbe871246e8fee045749d0a4677042b0c@95.217.216.88:46656,bb8615bb51139c05fd59020fc2aa7eac210690b4@135.181.221.186:27656,77791ee9b1eb56682335c451c296f450ee649c01@44.209.89.17:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,35e67a6199b44a58697653a14b6ca9c75974c57d@89.117.56.126:24756,0996622e0d51b51cdfb2e8bed752968693f87e10@109.205.180.254:26656,1ed89bd1d280c4c6eb7d9134bb238d97fbb3f4b2@88.99.104.180:36656,af97c76448e6a5d7671c6523f38fc48cc7273da7@217.76.59.46:26656,6ee2e6550cd3510c0fc912bf0632a894148a79a7@38.242.202.174:31656,9e1ea4938f0112c1477827344e2f9d0792710575@185.252.232.189:30656,63d971a42e323f9411ef702d1f268f9862781c1f@194.163.165.176:40656,8f84d324a2d266e612d06db4a793b0d001ee62a0@38.146.3.200:20556,965694b051742c2da0ea66502dd9bfeea38de265@198.244.228.235:26656,6c0ddab56755cd010f65f1f1201d29120a2d9092@38.242.202.200:31656,6cf94ed068c7401ba8e6f9a49143fd90df415e83@195.201.237.198:46656,a85420b25181bdb9b3a38741c48dafd5fb3b922f@209.34.206.42:26656,f11d87d4d7ed4497b446b0071ca59096126da671@165.22.96.174:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
