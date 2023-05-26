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
peers="bc098ac0149a0a06701e29e4f7c79cac65c25c7f@162.55.173.57:26656,497886715ac23475f7428bd177b9fa53ff886a8d@78.46.80.79:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:12256,907cb9da5d7d7182a80a6e38aad59bd067059bb3@65.21.200.54:26656,5e1f23a66fafd1a73871f055a6dd2165c01fe1c2@65.109.25.62:26656,5b92ede5e88c5029d6c7b3b360b9cf59051ce409@65.109.84.33:26656,d792d994b50e546cef27f177f549090e6e41476f@69.197.6.24:26656,e1c43f090cef72f675c37f97ed2117417e251823@65.109.92.240:1166,e41b5c547ebf5dd2e96d30efbd9d4c5c32e2f3a6@161.97.175.119:26656,09e98344c96b5c0de8ba86bd417332b2b04d6b76@65.109.93.58:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.humansd/config/config.toml
```
