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
peers="6204710a0d089566b6df85ae4aee595afdd23cbb@146.190.40.115:26656,43a46e2fbe871246e8fee045749d0a4677042b0c@95.217.216.88:46656,26dc1602cfb6fac8a58ea621cc859403fb100b04@178.44.116.188:36656,77791ee9b1eb56682335c451c296f450ee649c01@44.209.89.17:26656,877f82353e8cd6e2586ea37a6d16064eae081a74@192.95.30.128:31656,c1008d2d05c56254e95d19ab7e9fe459dad2de3d@159.223.57.238:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,ed26b4f13a7f388064aa89e5d6419b0e78e3e94e@209.126.81.190:26656,7fc44e2651006fb2ddb4a56132e738da2845715f@65.108.6.45:61256,39794289e20cf80eba0a720eed58e7097e5686c1@136.243.103.53:46656,ec843a4aea197837c13f13612a525bd7377443b1@167.235.250.107:26656,88e09de4c713ecb3497f39f6e6c599aea7a10750@65.109.38.111:20556,36a242b6f2d779aeea4811e4e4c635a55d5274f1@45.151.123.72:26656,1fa5bb085e8f52c21bc71c39afbba2851bee3e18@43.157.48.181:26656,63d971a42e323f9411ef702d1f268f9862781c1f@194.163.165.176:40656,77c42c2b2702437981976f7a648c26cd37911f7b@65.108.9.230:46656,adf394846dc942b1fd03f6e310eda60b5eda7848@195.201.197.4:32656,6011e62596d177073f3bed476622162652ab4310@164.68.105.143:26656,e374d21e689d4e1832ef72e0dae2a9bca435ba36@95.217.114.220:46656,55f233c7c4bea21a47d266921ca5fce657f3adf7@168.119.240.200:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
