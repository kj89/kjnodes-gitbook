# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/humans.png" alt=""><figcaption></figcaption></figure>

Humans is Blockchain of AIs. It is the first blockchain network  from the Cosmos ecosystem capable of managing, deploying and  executing artificial intelligence on the blockchain.

**Chain ID**: humans_3000-31 | **Latest Version Tag**: v0.2.2 | **Wasm**: OFF

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

**live-peers** (11)
```bash
peers="733ffab95701aeebbc3021e827a7ef5f5c0dd93c@144.76.97.35:26656,f8ae768832a2665c915c3965a5bb8dc1031d5c1e@46.4.23.42:16656,0ae23e03040dd3e3a6c3a2326c62a206f531d671@162.19.31.150:26656,e41b5c547ebf5dd2e96d30efbd9d4c5c32e2f3a6@161.97.175.119:26656,907cb9da5d7d7182a80a6e38aad59bd067059bb3@65.21.200.54:26656,442c270ecf448899ff266899b3e8fd819456b52d@185.252.232.85:26656,bbd9f16f014279e85fd9047cade8a149cee2761d@91.194.30.203:26656,b99df5397a6104fac055f21195f1fb25b77f5704@65.109.92.79:17656,5c76f2a8ecad56dc081be10dc9a3927df18add20@118.193.37.229:26656,36f956fa2fe317a5d3163d0b6c7b104e33aa62e9@103.180.28.79:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:12256"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.humansd/config/config.toml
```
