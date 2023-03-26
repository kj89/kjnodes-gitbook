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
peers="7fc44e2651006fb2ddb4a56132e738da2845715f@65.108.6.45:61256,77791ee9b1eb56682335c451c296f450ee649c01@44.209.89.17:26656,ed26b4f13a7f388064aa89e5d6419b0e78e3e94e@209.126.81.190:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,6ee2e6550cd3510c0fc912bf0632a894148a79a7@38.242.202.174:31656,ee2fa87279bc626f9c979093389bd1d6568d96ff@65.109.37.228:36656,1135bf4bf8ffad1b9b508ea6c7408085ec87563a@134.122.16.44:26656,ca2cfea3c48640c094ad740bb41c2aeb81b5dcc6@194.163.187.175:46656,55f233c7c4bea21a47d266921ca5fce657f3adf7@168.119.240.200:26656,26dc1602cfb6fac8a58ea621cc859403fb100b04@178.44.116.188:36656,48bdb78c51e56b651c938d075e1077dab2c6197c@43.157.22.223:26656,94b63fddfc78230f51aeb7ac34b9fb86bd042a77@146.19.24.43:30585,63d971a42e323f9411ef702d1f268f9862781c1f@194.163.165.176:40656,61863c811eee3b601319b13286a087ddd07466fc@34.170.183.11:26656,1ed89bd1d280c4c6eb7d9134bb238d97fbb3f4b2@88.99.104.180:36656,09927421cd3aa47bc81f8f981e15c547bc490121@5.9.83.110:26656,43a46e2fbe871246e8fee045749d0a4677042b0c@95.217.216.88:46656,998b19ed2c580acaa2fdb5057e2930a38f041750@65.109.122.105:60556,af6787b3273dd60e0f809c7e5e2a2a9fd379045e@195.201.195.61:27656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
