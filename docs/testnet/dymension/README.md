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

**live-peers** (19)
```bash
peers="0996622e0d51b51cdfb2e8bed752968693f87e10@109.205.180.254:26656,7fc44e2651006fb2ddb4a56132e738da2845715f@65.108.6.45:61256,64acca240c1149f94b8986ffea3ee1b4e0bd5fbe@45.150.64.115:26656,77791ee9b1eb56682335c451c296f450ee649c01@44.209.89.17:26656,747d05bfe9f3e0c2e0462ac351c577699e1d9b8c@207.244.244.194:26656,6204710a0d089566b6df85ae4aee595afdd23cbb@146.190.40.115:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,11fe4c887e890c03cd109f61e8a80ecb77873013@134.209.184.190:26656,22acf9a303e825ce04171ef26e2326c09aeb238b@47.147.226.228:55656,3a8bb83d5c5afb13ae2c1c3b91c97928e277f6a5@142.132.205.94:15658,8f84d324a2d266e612d06db4a793b0d001ee62a0@38.146.3.200:20556,1fa5bb085e8f52c21bc71c39afbba2851bee3e18@43.157.48.181:26656,48bdb78c51e56b651c938d075e1077dab2c6197c@43.157.22.223:26656,adf394846dc942b1fd03f6e310eda60b5eda7848@195.201.197.4:32656,ed26b4f13a7f388064aa89e5d6419b0e78e3e94e@209.126.81.190:26656,ec843a4aea197837c13f13612a525bd7377443b1@167.235.250.107:26656,e5226fa166386f9055908194a4942c06b7003ab5@65.108.192.123:42656,55f233c7c4bea21a47d266921ca5fce657f3adf7@168.119.240.200:26656,a85420b25181bdb9b3a38741c48dafd5fb3b922f@209.34.206.42:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
