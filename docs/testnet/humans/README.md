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
peers="b9767aa2312748caaf67425890768d85186b69b1@5.9.87.205:26646,bc098ac0149a0a06701e29e4f7c79cac65c25c7f@162.55.173.57:26656,a7eaa41b5565295810b81641e0bf11a9fb2ca54e@159.69.69.183:26656,f8ae768832a2665c915c3965a5bb8dc1031d5c1e@46.4.23.42:16656,1ac5cfbf03df14b6c41d09d9f284e75cf03f5742@202.61.236.219:26656,42f95015c31c7814b6a0a717fd8c63d15f896e88@94.237.27.19:26656,fa9eb901a01430d928e71162151992c7afb51d62@178.23.126.70:26656,e1c43f090cef72f675c37f97ed2117417e251823@65.109.92.240:1166,3ca8a268313cc18799ec352c50fbaeb2f915399c@95.217.200.36:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:12256"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.humansd/config/config.toml
```
