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
peers="8f84d324a2d266e612d06db4a793b0d001ee62a0@38.146.3.200:20556,48bdb78c51e56b651c938d075e1077dab2c6197c@43.157.22.223:26656,c7a36d7abeea5704290f99c1608b50ff1f5e3e47@79.143.188.183:26656,ee2fa87279bc626f9c979093389bd1d6568d96ff@65.109.37.228:36656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,877f82353e8cd6e2586ea37a6d16064eae081a74@192.95.30.128:31656,e46b42d50947795f681cf9bfd601ae806e7a8d49@188.34.178.190:46656,7fc44e2651006fb2ddb4a56132e738da2845715f@65.108.6.45:61256,0996622e0d51b51cdfb2e8bed752968693f87e10@109.205.180.254:26656,965694b051742c2da0ea66502dd9bfeea38de265@198.244.228.235:26656,b473a649e58b49bc62b557e94d35a2c8c0ee9375@95.214.53.46:36656,1f9bca661f7f9e2048f78107409e70d9ff4616f0@185.146.148.109:26656,547cf669555bd611ba57b37bb0f288793ea4ec49@141.94.138.48:26673,747d05bfe9f3e0c2e0462ac351c577699e1d9b8c@207.244.244.194:26656,af6787b3273dd60e0f809c7e5e2a2a9fd379045e@195.201.195.61:27656,63d971a42e323f9411ef702d1f268f9862781c1f@194.163.165.176:40656,a85420b25181bdb9b3a38741c48dafd5fb3b922f@209.34.206.42:26656,09927421cd3aa47bc81f8f981e15c547bc490121@5.9.83.110:26656,55f233c7c4bea21a47d266921ca5fce657f3adf7@168.119.240.200:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
