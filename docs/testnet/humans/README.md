# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/humans.png" alt=""><figcaption></figcaption></figure>

Humans is Blockchain of AIs. It is the first blockchain network  from the Cosmos ecosystem capable of managing, deploying and  executing artificial intelligence on the blockchain.

**Chain ID**: humans_3000-23 | **Latest Version Tag**: v0.2.2 | **Wasm**: OFF

[Website](https://humans.ai) | [Discord](https://discord.gg/humansdotai) | [Twitter](https://twitter.com/humansdotai)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/humans-testnet](https://explorer.kjnodes.com/humans-testnet)

## Public endpoints

* api: [https://humans-testnet.api.kjnodes.com](https://humans-testnet.api.kjnodes.com)
* rpc: [https://humans-testnet.rpc.kjnodes.com](https://humans-testnet.rpc.kjnodes.com)
* grpc: humans-testnet.grpc.kjnodes.com:12290

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@humans-testnet.rpc.kjnodes.com:12256
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@humans-testnet.rpc.kjnodes.com:12259
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/humans-testnet/addrbook.json > $HOME/.humansd/config/addrbook.json
```

**live-peers** (10)
```bash
peers="a41f29c2d498b232c18f75364e38cee06fac198d@78.46.64.59:26656,de3cd5f6c726935c4c0fdb1e6bd5b705074c637c@144.76.45.59:26656,49f2ffa9786690548a1094b620d869ed72a33f8c@141.95.99.214:14356,b99df5397a6104fac055f21195f1fb25b77f5704@65.109.92.79:17656,2685f8e77fec93c99a55f2adb13835a50124d04e@135.181.18.112:55686,b1639fb460c9f55bb3acc3006df64ac5013f1412@91.194.30.203:26656,b77d993ac7b7e71a788284a7eff017d08711e1bb@51.79.82.138:26656,4762fa22edb91acd78010026f8da5fb71e174acb@142.165.207.19:36656,eb68fd2f20d58a6f8ab68e7a0fea7d5abe311f16@118.193.37.229:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:12256"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.humansd/config/config.toml
```
