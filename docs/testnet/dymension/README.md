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
peers="48bdb78c51e56b651c938d075e1077dab2c6197c@43.157.22.223:26656,7b4621b7744a2c3ea5ec9453980e1d555109a746@139.162.138.158:26656,1f9bca661f7f9e2048f78107409e70d9ff4616f0@185.146.148.109:26656,147a0021cff3c34251adb3ad7194574011fa3192@176.57.189.36:11656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,c7a36d7abeea5704290f99c1608b50ff1f5e3e47@79.143.188.183:26656,76fb074cb54791afa399979ca863da211404bad6@65.109.86.236:27656,cffb2a5e8fe08ba5ce46a8f56a4a1cdf636cbf8e@5.231.205.142:26656,6204710a0d089566b6df85ae4aee595afdd23cbb@146.190.40.115:26656,1bffcd1690806b5796415ff72f02157ce048bcdd@144.76.67.53:2580,3c937029e41e3f7b92b8b87d787be0ddc2a3f13c@70.34.214.236:26656,ee2fa87279bc626f9c979093389bd1d6568d96ff@65.109.37.228:36656,0996622e0d51b51cdfb2e8bed752968693f87e10@109.205.180.254:26656,af6787b3273dd60e0f809c7e5e2a2a9fd379045e@195.201.195.61:27656,f433653cef597b3f0dd5f4e3e46c05fd121246bb@95.216.149.50:26656,e678f78d3250fef1e6e0afcdb1ebdc5fe0d7138c@5.161.76.147:46656,74cfbc9e923784d1ca73188053561ea8b09e13d4@146.190.127.9:26656,95041e09bfcf7e5e7c01cd8bab5876680504693b@65.109.52.169:20556,1ed89bd1d280c4c6eb7d9134bb238d97fbb3f4b2@88.99.104.180:36656,a85420b25181bdb9b3a38741c48dafd5fb3b922f@209.34.206.42:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
