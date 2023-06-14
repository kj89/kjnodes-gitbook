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
peers="497886715ac23475f7428bd177b9fa53ff886a8d@78.46.80.79:26656,f8ae768832a2665c915c3965a5bb8dc1031d5c1e@46.4.23.42:16656,fa9eb901a01430d928e71162151992c7afb51d62@178.23.126.70:26656,fd6bccda6c8c16ed694c1f447966202492a3945c@65.108.72.253:26656,b99df5397a6104fac055f21195f1fb25b77f5704@65.109.92.79:17656,5b92ede5e88c5029d6c7b3b360b9cf59051ce409@65.109.84.33:26656,be5158df5152ec7e6a4eca04c89e40494d19927c@51.79.101.159:26656,a7eaa41b5565295810b81641e0bf11a9fb2ca54e@159.69.69.183:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:12256,d7eb0e65cecbeeaa649b0a2fdf95ca2fb9f0cc3e@206.125.33.0:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.humansd/config/config.toml
```
