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
peers="48bdb78c51e56b651c938d075e1077dab2c6197c@43.157.22.223:26656,77c42c2b2702437981976f7a648c26cd37911f7b@65.108.9.230:46656,77791ee9b1eb56682335c451c296f450ee649c01@44.209.89.17:26656,747d05bfe9f3e0c2e0462ac351c577699e1d9b8c@207.244.244.194:26656,c1008d2d05c56254e95d19ab7e9fe459dad2de3d@159.223.57.238:26656,965694b051742c2da0ea66502dd9bfeea38de265@198.244.228.235:26656,43a46e2fbe871246e8fee045749d0a4677042b0c@95.217.216.88:46656,3928de1971d20dd711a8695d628e036d85bea1d3@65.109.85.221:3240,26dc1602cfb6fac8a58ea621cc859403fb100b04@178.44.116.188:36656,6204710a0d089566b6df85ae4aee595afdd23cbb@146.190.40.115:26656,af6787b3273dd60e0f809c7e5e2a2a9fd379045e@195.201.195.61:27656,ee2fa87279bc626f9c979093389bd1d6568d96ff@65.109.37.228:36656,e374d21e689d4e1832ef72e0dae2a9bca435ba36@95.217.114.220:46656,b921655e6c66235915e7d4465ea2146e537f13e4@167.235.6.228:26636,e46b42d50947795f681cf9bfd601ae806e7a8d49@188.34.178.190:46656,61863c811eee3b601319b13286a087ddd07466fc@34.170.183.11:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,ed76fabd897c8911942ac4fa1c91f3f0afa7fdda@65.108.225.70:26656,ca2cfea3c48640c094ad740bb41c2aeb81b5dcc6@194.163.187.175:46656,80cce834fc749c0a9f47182665f833f97170ff4b@65.108.104.167:46656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
