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

**live-peers** (10)
```bash
peers="b9767aa2312748caaf67425890768d85186b69b1@5.9.87.205:26646,b1f13e9971cfdcf784fb0efbd1b72417d5410a02@195.201.59.194:26656,42f95015c31c7814b6a0a717fd8c63d15f896e88@94.237.27.19:26656,4a6451353a1040ccb2638de485feda28d40416cd@65.109.84.103:26656,5b92ede5e88c5029d6c7b3b360b9cf59051ce409@65.109.84.33:26656,b99df5397a6104fac055f21195f1fb25b77f5704@65.109.92.79:17656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:12256,d7eb0e65cecbeeaa649b0a2fdf95ca2fb9f0cc3e@206.125.33.0:26656,757df37416499e6936a882a9b43985795503bc22@65.108.195.29:22656,a7eaa41b5565295810b81641e0bf11a9fb2ca54e@159.69.69.183:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.humansd/config/config.toml
```
