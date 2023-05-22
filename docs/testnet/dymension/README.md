# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/dymension.png" alt=""><figcaption></figcaption></figure>

Dymension is a network of modular blockchains called RollApps  and at the center of it all is the Dymension Hub. Dymension  allows anyone to build and deploy their own consensus-free blockchain, a RollApp.

**Chain ID**: 35-C | **Latest Version Tag**: v0.2.0-beta | **Wasm**: OFF

[Website](https://dymension.xyz/) | [Discord](https://discord.gg/dymension) | [Twitter](https://twitter.com/dymensionXYZ)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/dymension-testnet](https://explorer.kjnodes.com/dymension-testnet)

## Public endpoints

* api: [https://dymension-testnet.api.kjnodes.com](https://dymension-testnet.api.kjnodes.com)
* rpc: [https://dymension-testnet.rpc.kjnodes.com](https://dymension-testnet.rpc.kjnodes.com)
* grpc: dymension-testnet.grpc.kjnodes.com:14690

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@dymension-testnet.rpc.kjnodes.com:14656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@dymension-testnet.rpc.kjnodes.com:14659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/dymension-testnet/addrbook.json > $HOME/.dymension/config/addrbook.json
```

**live-peers** (10)
```bash
peers="747d05bfe9f3e0c2e0462ac351c577699e1d9b8c@207.244.244.194:26656,b921655e6c66235915e7d4465ea2146e537f13e4@167.235.6.228:26636,ba2ef45240cc997443df795b801a34602ba68b55@65.109.92.241:17886,d2b841acdcabb622e9033fe685a395eef091f2fe@65.108.199.62:46656,db0264c412618949ce3a63cb07328d027e433372@146.19.24.101:26646,a0cb3fba615a75460360fd894922e8b53ba6686b@176.57.189.36:11656,8f84d324a2d266e612d06db4a793b0d001ee62a0@38.146.3.200:20556,796d7ccb570c93e778aaa26f80ee93c5dcf924e6@65.108.238.147:31656,146802c665668aa34647f55e2d97d682801bb40a@65.109.157.236:36656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
