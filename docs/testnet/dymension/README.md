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
peers="7fc44e2651006fb2ddb4a56132e738da2845715f@65.108.6.45:61256,869d03182da215ae0171ac37ee69a77ed59d1a38@135.181.253.11:46656,56e0f891f8312e239a631aea2f8b0e64c9f7d824@135.181.95.145:36656,ca2cfea3c48640c094ad740bb41c2aeb81b5dcc6@194.163.187.175:46656,88e09de4c713ecb3497f39f6e6c599aea7a10750@65.109.38.111:20556,64acca240c1149f94b8986ffea3ee1b4e0bd5fbe@45.150.64.115:26656,77791ee9b1eb56682335c451c296f450ee649c01@44.209.89.17:26656,22acf9a303e825ce04171ef26e2326c09aeb238b@47.147.226.228:55656,1fa5bb085e8f52c21bc71c39afbba2851bee3e18@43.157.48.181:26656,ec843a4aea197837c13f13612a525bd7377443b1@167.235.250.107:26656,39794289e20cf80eba0a720eed58e7097e5686c1@136.243.103.53:46656,88fdaf5ff074dc2010ccb0416e421f3819201eb6@212.23.222.125:30586,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,4d2ec1e61d61550fc5bfacc57e971ff9b6181152@135.181.180.29:26656,b8d08951d68da03af8f9272bf77684811197c289@95.216.41.160:26656,63996f52b1dc68259ff64bb2546625c71fc9d546@176.9.48.38:26656,1ed89bd1d280c4c6eb7d9134bb238d97fbb3f4b2@88.99.104.180:36656,77c42c2b2702437981976f7a648c26cd37911f7b@65.108.9.230:46656,877f82353e8cd6e2586ea37a6d16064eae081a74@192.95.30.128:31656,fe02e0280c6aedfeaea6f0d8e828dbc53f34e69a@91.107.232.129:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
