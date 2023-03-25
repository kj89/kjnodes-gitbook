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
peers="39794289e20cf80eba0a720eed58e7097e5686c1@136.243.103.53:46656,77791ee9b1eb56682335c451c296f450ee649c01@44.209.89.17:26656,e678f78d3250fef1e6e0afcdb1ebdc5fe0d7138c@5.161.76.147:46656,ed26b4f13a7f388064aa89e5d6419b0e78e3e94e@209.126.81.190:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,965694b051742c2da0ea66502dd9bfeea38de265@198.244.228.235:26656,26dc1602cfb6fac8a58ea621cc859403fb100b04@178.44.116.188:36656,ca2cfea3c48640c094ad740bb41c2aeb81b5dcc6@194.163.187.175:46656,ee2fa87279bc626f9c979093389bd1d6568d96ff@65.109.37.228:36656,ae509356c743a12259248fa8df23e42dae885e05@78.46.84.144:26656,747d05bfe9f3e0c2e0462ac351c577699e1d9b8c@207.244.244.194:26656,77c42c2b2702437981976f7a648c26cd37911f7b@65.108.9.230:46656,61863c811eee3b601319b13286a087ddd07466fc@34.170.183.11:26656,7fc44e2651006fb2ddb4a56132e738da2845715f@65.108.6.45:61256,6204710a0d089566b6df85ae4aee595afdd23cbb@146.190.40.115:26656,43a46e2fbe871246e8fee045749d0a4677042b0c@95.217.216.88:46656,6011e62596d177073f3bed476622162652ab4310@164.68.105.143:26656,6ee2e6550cd3510c0fc912bf0632a894148a79a7@38.242.202.174:31656,b473a649e58b49bc62b557e94d35a2c8c0ee9375@95.214.53.46:36656,48bdb78c51e56b651c938d075e1077dab2c6197c@43.157.22.223:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
