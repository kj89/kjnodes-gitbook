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
peers="09927421cd3aa47bc81f8f981e15c547bc490121@5.9.83.110:26656,b921655e6c66235915e7d4465ea2146e537f13e4@167.235.6.228:26636,43426e98064694d407b2165fb24d52980d38f1c9@88.99.3.158:20556,c7a36d7abeea5704290f99c1608b50ff1f5e3e47@79.143.188.183:26656,547cf669555bd611ba57b37bb0f288793ea4ec49@141.94.138.48:26673,63d971a42e323f9411ef702d1f268f9862781c1f@194.163.165.176:40656,965694b051742c2da0ea66502dd9bfeea38de265@198.244.228.235:26656,e8a706e3a81a36a6dded6cc02eabaf5d355f4c1d@80.79.5.171:28656,adf394846dc942b1fd03f6e310eda60b5eda7848@195.201.197.4:32656,6b00d8b9ad49cc2aa8d76416613bbbb10e6f56f7@65.109.108.150:26656,ee2fa87279bc626f9c979093389bd1d6568d96ff@65.109.37.228:36656,77791ee9b1eb56682335c451c296f450ee649c01@44.209.89.17:26656,6cf94ed068c7401ba8e6f9a49143fd90df415e83@195.201.237.198:46656,8e667c0759bfb20ec42b939956706301a4f2a10d@65.109.92.8:26656,8f84d324a2d266e612d06db4a793b0d001ee62a0@38.146.3.200:20556,6229800969107d039254a8e6888aaeb464cda44d@167.99.186.186:26656,48bdb78c51e56b651c938d075e1077dab2c6197c@43.157.22.223:26656,7fc44e2651006fb2ddb4a56132e738da2845715f@65.108.6.45:61256,1fa5bb085e8f52c21bc71c39afbba2851bee3e18@43.157.48.181:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
