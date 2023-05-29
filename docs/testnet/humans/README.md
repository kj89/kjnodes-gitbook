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
peers="b9767aa2312748caaf67425890768d85186b69b1@5.9.87.205:26646,59ad24780f3d8b90da29079a8a386aa1355969ef@144.76.45.59:26656,497886715ac23475f7428bd177b9fa53ff886a8d@78.46.80.79:26656,946b549550e9c564193bf4c963d84b17e5415a50@136.243.136.241:26656,0ae23e03040dd3e3a6c3a2326c62a206f531d671@162.19.31.150:26656,650b54b9fed877f05e8f2fa9b1a046e5a601a7c9@135.181.138.160:26656,757df37416499e6936a882a9b43985795503bc22@65.108.195.29:22656,bbd9f16f014279e85fd9047cade8a149cee2761d@91.194.30.203:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:12256,d7eb0e65cecbeeaa649b0a2fdf95ca2fb9f0cc3e@206.125.33.0:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.humansd/config/config.toml
```
