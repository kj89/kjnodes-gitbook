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
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,747d05bfe9f3e0c2e0462ac351c577699e1d9b8c@207.244.244.194:26656,af6787b3273dd60e0f809c7e5e2a2a9fd379045e@195.201.195.61:27656,e374d21e689d4e1832ef72e0dae2a9bca435ba36@95.217.114.220:46656,965694b051742c2da0ea66502dd9bfeea38de265@198.244.228.235:26656,8e667c0759bfb20ec42b939956706301a4f2a10d@65.109.92.8:26656,7fc44e2651006fb2ddb4a56132e738da2845715f@65.108.6.45:61256,e46b42d50947795f681cf9bfd601ae806e7a8d49@188.34.178.190:46656,ec843a4aea197837c13f13612a525bd7377443b1@167.235.250.107:26656,88fdaf5ff074dc2010ccb0416e421f3819201eb6@212.23.222.125:30586,4d2ec1e61d61550fc5bfacc57e971ff9b6181152@135.181.180.29:26656,8f84d324a2d266e612d06db4a793b0d001ee62a0@38.146.3.200:20556,77791ee9b1eb56682335c451c296f450ee649c01@44.209.89.17:26656,ee2fa87279bc626f9c979093389bd1d6568d96ff@65.109.37.228:36656,3c937029e41e3f7b92b8b87d787be0ddc2a3f13c@70.34.214.236:26656,b921655e6c66235915e7d4465ea2146e537f13e4@167.235.6.228:26636,39794289e20cf80eba0a720eed58e7097e5686c1@136.243.103.53:46656,6229800969107d039254a8e6888aaeb464cda44d@167.99.186.186:26656,acb69c31cac6140a1a9570e683de5e26dd008cff@51.222.44.116:32656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
