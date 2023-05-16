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
peers="ee2fa87279bc626f9c979093389bd1d6568d96ff@65.109.37.228:36656,f433653cef597b3f0dd5f4e3e46c05fd121246bb@95.216.149.50:26656,ba2ef45240cc997443df795b801a34602ba68b55@65.109.92.241:17886,77c42c2b2702437981976f7a648c26cd37911f7b@65.108.9.230:46656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14656,7fc44e2651006fb2ddb4a56132e738da2845715f@65.108.6.45:61256,747d05bfe9f3e0c2e0462ac351c577699e1d9b8c@207.244.244.194:26656,57a66a59cc291887f35e231b4469e2c957728862@46.4.5.45:20556,146802c665668aa34647f55e2d97d682801bb40a@65.109.157.236:36656,0d7ec1ea841e763267f197e2e0aa89467da24064@94.19.249.187:35656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
