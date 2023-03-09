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
peers="b921655e6c66235915e7d4465ea2146e537f13e4@167.235.6.228:26636,af6787b3273dd60e0f809c7e5e2a2a9fd379045e@195.201.195.61:27656,eb524a9ed0e080ec4fa9a21df3f5f56e94e0e811@51.89.7.235:26652,b473a649e58b49bc62b557e94d35a2c8c0ee9375@95.214.53.46:36656,63d971a42e323f9411ef702d1f268f9862781c1f@194.163.165.176:40656,7fc44e2651006fb2ddb4a56132e738da2845715f@65.108.6.45:61256,b1e1e5a9dbf2e03b456668c2f2d9164ae090ba0c@109.123.244.56:46656,ee2fa87279bc626f9c979093389bd1d6568d96ff@65.109.37.228:36656,0996622e0d51b51cdfb2e8bed752968693f87e10@109.205.180.254:26656,77791ee9b1eb56682335c451c296f450ee649c01@44.209.89.17:26656,869d03182da215ae0171ac37ee69a77ed59d1a38@135.181.253.11:46656,877f82353e8cd6e2586ea37a6d16064eae081a74@192.95.30.128:31656,6cf94ed068c7401ba8e6f9a49143fd90df415e83@195.201.237.198:46656,1fa5bb085e8f52c21bc71c39afbba2851bee3e18@43.157.48.181:26656,6204710a0d089566b6df85ae4aee595afdd23cbb@146.190.40.115:26656,965694b051742c2da0ea66502dd9bfeea38de265@198.244.228.235:26656,747d05bfe9f3e0c2e0462ac351c577699e1d9b8c@207.244.244.194:26656,43426e98064694d407b2165fb24d52980d38f1c9@88.99.3.158:20556,8f84d324a2d266e612d06db4a793b0d001ee62a0@38.146.3.200:20556,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
