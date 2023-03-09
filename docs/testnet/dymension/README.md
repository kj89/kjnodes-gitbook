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
peers="b921655e6c66235915e7d4465ea2146e537f13e4@167.235.6.228:26636,9e1ea4938f0112c1477827344e2f9d0792710575@185.252.232.189:30656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,adf394846dc942b1fd03f6e310eda60b5eda7848@195.201.197.4:32656,43426e98064694d407b2165fb24d52980d38f1c9@88.99.3.158:20556,eb524a9ed0e080ec4fa9a21df3f5f56e94e0e811@51.89.7.235:26652,af97c76448e6a5d7671c6523f38fc48cc7273da7@217.76.59.46:26656,b473a649e58b49bc62b557e94d35a2c8c0ee9375@95.214.53.46:36656,ee2fa87279bc626f9c979093389bd1d6568d96ff@65.109.37.228:36656,77791ee9b1eb56682335c451c296f450ee649c01@44.209.89.17:26656,b1e1e5a9dbf2e03b456668c2f2d9164ae090ba0c@109.123.244.56:46656,48bdb78c51e56b651c938d075e1077dab2c6197c@43.157.22.223:26656,0996622e0d51b51cdfb2e8bed752968693f87e10@109.205.180.254:26656,af6787b3273dd60e0f809c7e5e2a2a9fd379045e@195.201.195.61:27656,65242d54d20a6c16a401004a8fb936343d9cae99@65.109.106.91:26656,63d971a42e323f9411ef702d1f268f9862781c1f@194.163.165.176:40656,f433653cef597b3f0dd5f4e3e46c05fd121246bb@95.216.149.50:26656,6204710a0d089566b6df85ae4aee595afdd23cbb@146.190.40.115:26656,869d03182da215ae0171ac37ee69a77ed59d1a38@135.181.253.11:46656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
