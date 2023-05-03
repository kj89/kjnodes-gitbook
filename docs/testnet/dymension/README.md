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
peers="d4a66d01b1d109d842a7f1d51f541033c653ea03@116.202.227.117:46656,4c23a702f7ba893cb6dc73e2e2c500aa22909dee@159.65.82.47:32656,7fc44e2651006fb2ddb4a56132e738da2845715f@65.108.6.45:61256,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14656,af6787b3273dd60e0f809c7e5e2a2a9fd379045e@195.201.195.61:27656,965694b051742c2da0ea66502dd9bfeea38de265@198.244.228.235:26656,5a0cee849e4a909b42c8b9b2df4a1e737ff2b715@194.233.90.134:26656,c5db84267f7dce8fa249b0d5365d59a7abeb0164@95.217.211.32:46656,e46b42d50947795f681cf9bfd601ae806e7a8d49@188.34.178.190:46656,147a0021cff3c34251adb3ad7194574011fa3192@176.57.189.36:11656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
