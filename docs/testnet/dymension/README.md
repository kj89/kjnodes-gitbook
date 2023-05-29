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

**live-peers** (11)
```bash
peers="82b51653205df40d43f257041db2da0f9f1644fa@178.63.26.94:46656,8c4da005c8a68682402293f951449f042e6f3dbf@164.92.190.234:21456,747d05bfe9f3e0c2e0462ac351c577699e1d9b8c@207.244.244.194:26656,d4a66d01b1d109d842a7f1d51f541033c653ea03@116.202.227.117:46656,d2b841acdcabb622e9033fe685a395eef091f2fe@65.108.199.62:46656,937de939b495ea75b74306ef3a112f90cb414508@65.108.69.151:26656,877f82353e8cd6e2586ea37a6d16064eae081a74@192.95.30.128:31656,7f928378eecafe22fe1e93d9f63db181cec3f8a3@145.239.143.76:11256,8d5eac1042bac34cddd25d7601789fc03cb3f3a9@168.119.213.113:46656,e678f78d3250fef1e6e0afcdb1ebdc5fe0d7138c@5.161.76.147:46656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
