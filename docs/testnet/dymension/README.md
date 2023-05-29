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
peers="877f82353e8cd6e2586ea37a6d16064eae081a74@192.95.30.128:31656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14656,0d7ec1ea841e763267f197e2e0aa89467da24064@94.19.249.187:35656,547cf669555bd611ba57b37bb0f288793ea4ec49@141.94.138.48:26673,7f928378eecafe22fe1e93d9f63db181cec3f8a3@145.239.143.76:11256,d2b841acdcabb622e9033fe685a395eef091f2fe@65.108.199.62:46656,77c42c2b2702437981976f7a648c26cd37911f7b@65.108.9.230:46656,bb8615bb51139c05fd59020fc2aa7eac210690b4@135.181.221.186:27656,8f84d324a2d266e612d06db4a793b0d001ee62a0@38.146.3.200:20556,8c4da005c8a68682402293f951449f042e6f3dbf@164.92.190.234:21456"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
