# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/humans.png" alt=""><figcaption></figcaption></figure>

Humans is Blockchain of AIs. It is the first blockchain network  from the Cosmos ecosystem capable of managing, deploying and  executing artificial intelligence on the blockchain.

**Chain ID**: humans_3000-2 | **Latest Version Tag**: v0.2.1 | **Wasm**: OFF

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
peers="de3cd5f6c726935c4c0fdb1e6bd5b705074c637c@144.76.45.59:26656,b1f13e9971cfdcf784fb0efbd1b72417d5410a02@195.201.59.194:26656,e6489cf86b51fa37cae968ccbbda1da03b742a5e@128.140.56.206:26656,946b549550e9c564193bf4c963d84b17e5415a50@136.243.136.241:26656,f05366147458d2d09ff525f8b4258a7978f72991@162.55.173.57:26656,fa9eb901a01430d928e71162151992c7afb51d62@178.23.126.70:26656,b77d993ac7b7e71a788284a7eff017d08711e1bb@51.79.82.138:26656,eb68fd2f20d58a6f8ab68e7a0fea7d5abe311f16@118.193.37.229:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:12256,2f6cc8b0b255745d71c358351ddde1faa350b0be@95.217.200.36:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.humansd/config/config.toml
```
