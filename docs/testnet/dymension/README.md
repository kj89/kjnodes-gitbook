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
peers="e46b42d50947795f681cf9bfd601ae806e7a8d49@188.34.178.190:46656,b921655e6c66235915e7d4465ea2146e537f13e4@167.235.6.228:26636,ec843a4aea197837c13f13612a525bd7377443b1@167.235.250.107:26656,56e0f891f8312e239a631aea2f8b0e64c9f7d824@135.181.95.145:36656,747d05bfe9f3e0c2e0462ac351c577699e1d9b8c@207.244.244.194:26656,af6787b3273dd60e0f809c7e5e2a2a9fd379045e@195.201.195.61:27656,43426e98064694d407b2165fb24d52980d38f1c9@88.99.3.158:20556,1135bf4bf8ffad1b9b508ea6c7408085ec87563a@134.122.16.44:26656,18da7db008aa30ac6fb837323c608c286bf87b25@178.128.82.254:26656,c1008d2d05c56254e95d19ab7e9fe459dad2de3d@159.223.57.238:26656,a85420b25181bdb9b3a38741c48dafd5fb3b922f@209.34.206.42:26656,cffb2a5e8fe08ba5ce46a8f56a4a1cdf636cbf8e@5.231.205.142:26656,236b71988898dff63cef139f83a64f5fbfd9d8d7@135.181.18.112:55696,8f84d324a2d266e612d06db4a793b0d001ee62a0@38.146.3.200:20556,5d689e09a129c03c003f05850262f03b2433a384@51.79.30.141:26656,0d30a0790a216d01c9759ab48192d9154381e6c0@136.243.88.91:3240,3c937029e41e3f7b92b8b87d787be0ddc2a3f13c@70.34.214.236:26656,77791ee9b1eb56682335c451c296f450ee649c01@44.209.89.17:26656,6ee2e6550cd3510c0fc912bf0632a894148a79a7@38.242.202.174:31656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
