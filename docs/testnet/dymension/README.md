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
peers="1ed89bd1d280c4c6eb7d9134bb238d97fbb3f4b2@88.99.104.180:36656,3fdba29b1d02066f6406c611e1ae42e9ec76bbf2@185.197.194.227:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14656,e4dec3315020ac14bc82e6f4b0696d1b0f65d999@138.201.204.5:40656,513557be25d2edc51481be90c808f72cd662e1d2@167.235.250.107:26656,7555547f1a8be4706d80312b0f6383d1a7fb546e@167.235.7.34:45656,d4a66d01b1d109d842a7f1d51f541033c653ea03@116.202.227.117:46656,48ea1c8c62e9eb193a317096339b22f4a4452c8c@185.144.99.22:26656,11fe4c887e890c03cd109f61e8a80ecb77873013@134.209.184.190:26656,877f82353e8cd6e2586ea37a6d16064eae081a74@192.95.30.128:31656,8c4da005c8a68682402293f951449f042e6f3dbf@164.92.190.234:21456"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
