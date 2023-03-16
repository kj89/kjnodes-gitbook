# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/dymension.png" width="150" alt=""><figcaption></figcaption></figure>

Dymension is a network of modular blockchains called RollApps  and at the center of it all is the Dymension Hub. Dymension  allows anyone to build and deploy their own consensus-free blockchain, a RollApp.

**Chain ID**: 35-C | **Latest Version Tag**: v0.2.0-beta | **Wasm**: OFF

[Website](https://dymension.xyz/) | [Discord](https://discord.gg/dymension) | [Twitter](https://twitter.com/dymensionXYZ)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/dymension-testnet](https://explorer.kjnodes.com/dymension-testnet)

## Public endpoints

* api: [https://dymension-testnet.api.kjnodes.com](https://dymension-testnet.api.kjnodes.com)
* rpc: [https://dymension-testnet.rpc.kjnodes.com](https://dymension-testnet.rpc.kjnodes.com)
* grpc: dymension-testnet.grpc.kjnodes.com:46090

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
peers="b921655e6c66235915e7d4465ea2146e537f13e4@167.235.6.228:26636,965694b051742c2da0ea66502dd9bfeea38de265@198.244.228.235:26656,acb69c31cac6140a1a9570e683de5e26dd008cff@51.222.44.116:32656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,6204710a0d089566b6df85ae4aee595afdd23cbb@146.190.40.115:26656,7fc44e2651006fb2ddb4a56132e738da2845715f@65.108.6.45:61256,3a8bb83d5c5afb13ae2c1c3b91c97928e277f6a5@142.132.205.94:15658,36a242b6f2d779aeea4811e4e4c635a55d5274f1@45.151.123.72:26656,ee2fa87279bc626f9c979093389bd1d6568d96ff@65.109.37.228:36656,c7a36d7abeea5704290f99c1608b50ff1f5e3e47@79.143.188.183:26656,3c937029e41e3f7b92b8b87d787be0ddc2a3f13c@70.34.214.236:26656,e374d21e689d4e1832ef72e0dae2a9bca435ba36@95.217.114.220:46656,56e0f891f8312e239a631aea2f8b0e64c9f7d824@135.181.95.145:36656,63d971a42e323f9411ef702d1f268f9862781c1f@194.163.165.176:40656,9e1ea4938f0112c1477827344e2f9d0792710575@185.252.232.189:30656,26dc1602cfb6fac8a58ea621cc859403fb100b04@178.44.116.188:36656,c1008d2d05c56254e95d19ab7e9fe459dad2de3d@159.223.57.238:26656,1ed89bd1d280c4c6eb7d9134bb238d97fbb3f4b2@88.99.104.180:36656,18da7db008aa30ac6fb837323c608c286bf87b25@178.128.82.254:26656,0f1045fd8c81a8ad843cf0f96a73ed34865322a7@3.145.180.81:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
