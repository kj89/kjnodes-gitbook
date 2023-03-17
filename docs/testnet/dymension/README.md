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
peers="e46b42d50947795f681cf9bfd601ae806e7a8d49@188.34.178.190:46656,747d05bfe9f3e0c2e0462ac351c577699e1d9b8c@207.244.244.194:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,77791ee9b1eb56682335c451c296f450ee649c01@44.209.89.17:26656,b921655e6c66235915e7d4465ea2146e537f13e4@167.235.6.228:26636,63d971a42e323f9411ef702d1f268f9862781c1f@194.163.165.176:40656,3a8bb83d5c5afb13ae2c1c3b91c97928e277f6a5@142.132.205.94:15658,7fc44e2651006fb2ddb4a56132e738da2845715f@65.108.6.45:61256,56e0f891f8312e239a631aea2f8b0e64c9f7d824@135.181.95.145:36656,43426e98064694d407b2165fb24d52980d38f1c9@88.99.3.158:20556,eb524a9ed0e080ec4fa9a21df3f5f56e94e0e811@51.89.7.235:26652,ec843a4aea197837c13f13612a525bd7377443b1@167.235.250.107:26656,4c25618c9465c0aaea91d936be446d5db04be3d1@195.201.237.185:46656,ee2fa87279bc626f9c979093389bd1d6568d96ff@65.109.37.228:36656,a85420b25181bdb9b3a38741c48dafd5fb3b922f@209.34.206.42:26656,8f84d324a2d266e612d06db4a793b0d001ee62a0@38.146.3.200:20556,f2d185a19f27e8290163d63a28846601662b50f1@138.201.204.5:40656,af6787b3273dd60e0f809c7e5e2a2a9fd379045e@195.201.195.61:27656,8e667c0759bfb20ec42b939956706301a4f2a10d@65.109.92.8:26656,18da7db008aa30ac6fb837323c608c286bf87b25@178.128.82.254:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
