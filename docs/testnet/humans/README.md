# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/humans.png" alt=""><figcaption></figcaption></figure>

Humans is Blockchain of AIs. It is the first blockchain network  from the Cosmos ecosystem capable of managing, deploying and  executing artificial intelligence on the blockchain.

**Chain ID**: humans_3000-23 | **Latest Version Tag**: v0.2.1 | **Wasm**: OFF

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
peers="e6489cf86b51fa37cae968ccbbda1da03b742a5e@128.140.56.206:26656,6271d80b8fc42da3a2825cc5ef75818dd52423d1@138.201.121.185:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:12256,fa9eb901a01430d928e71162151992c7afb51d62@178.23.126.70:26656,733ffab95701aeebbc3021e827a7ef5f5c0dd93c@144.76.97.35:26656,ceba57f1376d4949cc0419918d110f0085b24b25@135.181.113.225:26656,bf99f84b1674f87ffe95972f332cb218d1253b9c@65.108.72.253:26656,a41f29c2d498b232c18f75364e38cee06fac198d@78.46.64.59:26656,6c2581bce457207a8d29895216a06f0f98d39599@38.146.3.209:26656,b1639fb460c9f55bb3acc3006df64ac5013f1412@91.194.30.203:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.humansd/config/config.toml
```
