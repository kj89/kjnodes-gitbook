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
peers="b9767aa2312748caaf67425890768d85186b69b1@5.9.87.205:26646,42f95015c31c7814b6a0a717fd8c63d15f896e88@94.237.27.19:26656,b99df5397a6104fac055f21195f1fb25b77f5704@65.109.92.79:17656,5c76f2a8ecad56dc081be10dc9a3927df18add20@118.193.37.229:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:12256,b1f13e9971cfdcf784fb0efbd1b72417d5410a02@195.201.59.194:26656,ceba57f1376d4949cc0419918d110f0085b24b25@135.181.113.225:26656,fd6bccda6c8c16ed694c1f447966202492a3945c@65.108.72.253:26656,907cb9da5d7d7182a80a6e38aad59bd067059bb3@65.21.200.54:26656,fa9eb901a01430d928e71162151992c7afb51d62@178.23.126.70:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.humansd/config/config.toml
```
