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
peers="1ed89bd1d280c4c6eb7d9134bb238d97fbb3f4b2@88.99.104.180:36656,fc827d9c55d49f0adb31720c134bd8f675ca7b27@95.216.193.163:26656,146802c665668aa34647f55e2d97d682801bb40a@65.109.157.236:36656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14656,d2b841acdcabb622e9033fe685a395eef091f2fe@65.108.199.62:46656,e4dec3315020ac14bc82e6f4b0696d1b0f65d999@138.201.204.5:40656,b921655e6c66235915e7d4465ea2146e537f13e4@167.235.6.228:26636,96ffe4b68c3f97cbeae4b4362634bf1054c7aeeb@142.132.151.99:15658,877f82353e8cd6e2586ea37a6d16064eae081a74@192.95.30.128:31656,5dbbb68e0c8a86bdc372cf1de0691f1cdc6a96ad@82.208.23.223:27656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
