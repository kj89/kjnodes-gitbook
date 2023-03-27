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

**live-peers** (20)
```bash
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,7fc44e2651006fb2ddb4a56132e738da2845715f@65.108.6.45:61256,77c42c2b2702437981976f7a648c26cd37911f7b@65.108.9.230:46656,77791ee9b1eb56682335c451c296f450ee649c01@44.209.89.17:26656,39794289e20cf80eba0a720eed58e7097e5686c1@136.243.103.53:46656,d8b1bcfc123e63b24d0ebf86ab674a0fc5cb3b06@51.159.97.212:26656,c1008d2d05c56254e95d19ab7e9fe459dad2de3d@159.223.57.238:26656,26dc1602cfb6fac8a58ea621cc859403fb100b04@178.44.116.188:36656,877f82353e8cd6e2586ea37a6d16064eae081a74@192.95.30.128:31656,c36184fec2fb60bf7be775390c1cd6619c0201ef@209.126.81.240:26656,eb524a9ed0e080ec4fa9a21df3f5f56e94e0e811@51.89.7.235:26652,6ebe5856a7617cb9309a923a3935687903d2607d@141.95.97.28:15256,747d05bfe9f3e0c2e0462ac351c577699e1d9b8c@207.244.244.194:26656,3c937029e41e3f7b92b8b87d787be0ddc2a3f13c@70.34.214.236:26656,55f233c7c4bea21a47d266921ca5fce657f3adf7@168.119.240.200:26656,4c25618c9465c0aaea91d936be446d5db04be3d1@195.201.237.185:46656,a85420b25181bdb9b3a38741c48dafd5fb3b922f@209.34.206.42:26656,88e09de4c713ecb3497f39f6e6c599aea7a10750@65.109.38.111:20556,a9444e3bca5023eaaa6b670258bedfa8dcbaf7cf@116.202.170.159:24256,1ed89bd1d280c4c6eb7d9134bb238d97fbb3f4b2@88.99.104.180:36656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
