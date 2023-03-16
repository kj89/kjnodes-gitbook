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
peers="ec843a4aea197837c13f13612a525bd7377443b1@167.235.250.107:26656,63d971a42e323f9411ef702d1f268f9862781c1f@194.163.165.176:40656,65242d54d20a6c16a401004a8fb936343d9cae99@65.109.106.91:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,b921655e6c66235915e7d4465ea2146e537f13e4@167.235.6.228:26636,56e0f891f8312e239a631aea2f8b0e64c9f7d824@135.181.95.145:36656,0996622e0d51b51cdfb2e8bed752968693f87e10@109.205.180.254:26656,747d05bfe9f3e0c2e0462ac351c577699e1d9b8c@207.244.244.194:26656,26dc1602cfb6fac8a58ea621cc859403fb100b04@178.44.116.188:36656,1135bf4bf8ffad1b9b508ea6c7408085ec87563a@134.122.16.44:26656,af6787b3273dd60e0f809c7e5e2a2a9fd379045e@195.201.195.61:27656,18da7db008aa30ac6fb837323c608c286bf87b25@178.128.82.254:26656,c1008d2d05c56254e95d19ab7e9fe459dad2de3d@159.223.57.238:26656,1fa5bb085e8f52c21bc71c39afbba2851bee3e18@43.157.48.181:26656,7fc44e2651006fb2ddb4a56132e738da2845715f@65.108.6.45:61256,a85420b25181bdb9b3a38741c48dafd5fb3b922f@209.34.206.42:26656,88e09de4c713ecb3497f39f6e6c599aea7a10750@65.109.38.111:20556,43426e98064694d407b2165fb24d52980d38f1c9@88.99.3.158:20556,236b71988898dff63cef139f83a64f5fbfd9d8d7@135.181.18.112:55696"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
