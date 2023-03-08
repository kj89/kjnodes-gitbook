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
peers="43426e98064694d407b2165fb24d52980d38f1c9@88.99.3.158:20556,6cf94ed068c7401ba8e6f9a49143fd90df415e83@195.201.237.198:46656,0996622e0d51b51cdfb2e8bed752968693f87e10@109.205.180.254:26656,77791ee9b1eb56682335c451c296f450ee649c01@44.209.89.17:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,c7a36d7abeea5704290f99c1608b50ff1f5e3e47@79.143.188.183:26656,adf394846dc942b1fd03f6e310eda60b5eda7848@195.201.197.4:32656,88fdaf5ff074dc2010ccb0416e421f3819201eb6@212.23.222.125:30586,eb524a9ed0e080ec4fa9a21df3f5f56e94e0e811@51.89.7.235:26652,6011e62596d177073f3bed476622162652ab4310@164.68.105.143:26656,8f84d324a2d266e612d06db4a793b0d001ee62a0@38.146.3.200:20556,b921655e6c66235915e7d4465ea2146e537f13e4@167.235.6.228:26636,48bdb78c51e56b651c938d075e1077dab2c6197c@43.157.22.223:26656,6204710a0d089566b6df85ae4aee595afdd23cbb@146.190.40.115:26656,63d971a42e323f9411ef702d1f268f9862781c1f@194.163.165.176:40656,09927421cd3aa47bc81f8f981e15c547bc490121@5.9.83.110:26656,95041e09bfcf7e5e7c01cd8bab5876680504693b@65.109.52.169:20556,b473a649e58b49bc62b557e94d35a2c8c0ee9375@95.214.53.46:36656,af97c76448e6a5d7671c6523f38fc48cc7273da7@217.76.59.46:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
