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
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,c7a36d7abeea5704290f99c1608b50ff1f5e3e47@79.143.188.183:26656,af97c76448e6a5d7671c6523f38fc48cc7273da7@217.76.59.46:26656,77c42c2b2702437981976f7a648c26cd37911f7b@65.108.9.230:46656,747d05bfe9f3e0c2e0462ac351c577699e1d9b8c@207.244.244.194:26656,c1008d2d05c56254e95d19ab7e9fe459dad2de3d@159.223.57.238:26656,7fc44e2651006fb2ddb4a56132e738da2845715f@65.108.6.45:61256,77791ee9b1eb56682335c451c296f450ee649c01@44.209.89.17:26656,43a46e2fbe871246e8fee045749d0a4677042b0c@95.217.216.88:46656,8f84d324a2d266e612d06db4a793b0d001ee62a0@38.146.3.200:20556,63d971a42e323f9411ef702d1f268f9862781c1f@194.163.165.176:40656,6204710a0d089566b6df85ae4aee595afdd23cbb@146.190.40.115:26656,c36184fec2fb60bf7be775390c1cd6619c0201ef@209.126.81.240:26656,6ebe5856a7617cb9309a923a3935687903d2607d@141.95.97.28:15256,e678f78d3250fef1e6e0afcdb1ebdc5fe0d7138c@5.161.76.147:46656,dddc76ca6279ac90b12cf35b39c46a2fc2c2ce52@5.161.78.48:46656,1135bf4bf8ffad1b9b508ea6c7408085ec87563a@134.122.16.44:26656,965694b051742c2da0ea66502dd9bfeea38de265@198.244.228.235:26656,56e0f891f8312e239a631aea2f8b0e64c9f7d824@135.181.95.145:36656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
