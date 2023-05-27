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

**live-peers** (12)
```bash
peers="513557be25d2edc51481be90c808f72cd662e1d2@167.235.250.107:26656,8c3d6e4d065c6c171e2620f8ed8be5404fa61923@162.55.1.176:26656,bb8615bb51139c05fd59020fc2aa7eac210690b4@135.181.221.186:27656,d2b841acdcabb622e9033fe685a395eef091f2fe@65.108.199.62:46656,b8d08951d68da03af8f9272bf77684811197c289@95.216.41.160:26656,77791ee9b1eb56682335c451c296f450ee649c01@44.209.89.17:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14656,802b8783727af8094d81f9cb0bf2ad9cc3d32aa0@193.46.243.144:26656,c97117a21f7163a1ec354ac5e09e5e544a67b785@51.68.204.169:26646,3df2154255d44bee7f036531e7575bdff152207f@51.178.65.184:27656,8a66c13470c05acbd4d8711d21adbb67cc03dd1f@45.151.123.238:26656,8c4da005c8a68682402293f951449f042e6f3dbf@164.92.190.234:21456"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
