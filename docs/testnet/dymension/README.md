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
peers="5dbbb68e0c8a86bdc372cf1de0691f1cdc6a96ad@82.208.23.223:27656,11fe4c887e890c03cd109f61e8a80ecb77873013@134.209.184.190:26656,513557be25d2edc51481be90c808f72cd662e1d2@167.235.250.107:26656,8c4da005c8a68682402293f951449f042e6f3dbf@164.92.190.234:21456,77c42c2b2702437981976f7a648c26cd37911f7b@65.108.9.230:46656,d2b841acdcabb622e9033fe685a395eef091f2fe@65.108.199.62:46656,68f6c52147c9423300f5b503348bbb02b229820c@51.159.153.211:26656,747d05bfe9f3e0c2e0462ac351c577699e1d9b8c@207.244.244.194:26656,4e94581e03f46c2bda293fa47db05c2fa8883256@190.102.106.50:29656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14656,c5db84267f7dce8fa249b0d5365d59a7abeb0164@95.217.211.32:46656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
