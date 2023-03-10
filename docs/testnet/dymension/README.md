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
peers="ee2fa87279bc626f9c979093389bd1d6568d96ff@65.109.37.228:36656,55f233c7c4bea21a47d266921ca5fce657f3adf7@168.119.240.200:26656,547cf669555bd611ba57b37bb0f288793ea4ec49@141.94.138.48:26673,c7a36d7abeea5704290f99c1608b50ff1f5e3e47@79.143.188.183:26656,c5db84267f7dce8fa249b0d5365d59a7abeb0164@95.217.211.32:46656,0996622e0d51b51cdfb2e8bed752968693f87e10@109.205.180.254:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,77791ee9b1eb56682335c451c296f450ee649c01@44.209.89.17:26656,8f84d324a2d266e612d06db4a793b0d001ee62a0@38.146.3.200:20556,747d05bfe9f3e0c2e0462ac351c577699e1d9b8c@207.244.244.194:26656,48bdb78c51e56b651c938d075e1077dab2c6197c@43.157.22.223:26656,af6787b3273dd60e0f809c7e5e2a2a9fd379045e@195.201.195.61:27656,147a0021cff3c34251adb3ad7194574011fa3192@176.57.189.36:11656,6204710a0d089566b6df85ae4aee595afdd23cbb@146.190.40.115:26656,acb69c31cac6140a1a9570e683de5e26dd008cff@51.222.44.116:32656,68f6c52147c9423300f5b503348bbb02b229820c@51.159.153.211:26656,8d5eac1042bac34cddd25d7601789fc03cb3f3a9@168.119.213.113:46656,ec843a4aea197837c13f13612a525bd7377443b1@167.235.250.107:26656,43426e98064694d407b2165fb24d52980d38f1c9@88.99.3.158:20556"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
