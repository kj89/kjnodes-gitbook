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
peers="63d971a42e323f9411ef702d1f268f9862781c1f@194.163.165.176:40656,1f9bca661f7f9e2048f78107409e70d9ff4616f0@185.146.148.109:26656,48bdb78c51e56b651c938d075e1077dab2c6197c@43.157.22.223:26656,ee2fa87279bc626f9c979093389bd1d6568d96ff@65.109.37.228:36656,acb69c31cac6140a1a9570e683de5e26dd008cff@51.222.44.116:32656,0996622e0d51b51cdfb2e8bed752968693f87e10@109.205.180.254:26656,af6787b3273dd60e0f809c7e5e2a2a9fd379045e@195.201.195.61:27656,877f82353e8cd6e2586ea37a6d16064eae081a74@192.95.30.128:31656,965694b051742c2da0ea66502dd9bfeea38de265@198.244.228.235:26656,e46b42d50947795f681cf9bfd601ae806e7a8d49@188.34.178.190:46656,1ed89bd1d280c4c6eb7d9134bb238d97fbb3f4b2@88.99.104.180:36656,1bffcd1690806b5796415ff72f02157ce048bcdd@144.76.67.53:2580,7fc44e2651006fb2ddb4a56132e738da2845715f@65.108.6.45:61256,f433653cef597b3f0dd5f4e3e46c05fd121246bb@95.216.149.50:26656,43426e98064694d407b2165fb24d52980d38f1c9@88.99.3.158:20556,a85420b25181bdb9b3a38741c48dafd5fb3b922f@209.34.206.42:26656,3a8bb83d5c5afb13ae2c1c3b91c97928e277f6a5@142.132.205.94:15658,c7a36d7abeea5704290f99c1608b50ff1f5e3e47@79.143.188.183:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,5d689e09a129c03c003f05850262f03b2433a384@51.79.30.141:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
