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
peers="7bb61943f683af93e6ac1a9cf43e4668f4d3304f@116.202.227.117:12256,1ac5cfbf03df14b6c41d09d9f284e75cf03f5742@202.61.236.219:26656,ceba57f1376d4949cc0419918d110f0085b24b25@135.181.113.225:26656,e1c43f090cef72f675c37f97ed2117417e251823@65.109.92.240:1166,42f95015c31c7814b6a0a717fd8c63d15f896e88@94.237.27.19:26656,be5158df5152ec7e6a4eca04c89e40494d19927c@51.79.101.159:26656,907cb9da5d7d7182a80a6e38aad59bd067059bb3@65.21.200.54:26656,945422039658c95372b0b4f45c24ec4a5f849206@38.146.3.209:26656,b9767aa2312748caaf67425890768d85186b69b1@5.9.87.205:26646,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:12256"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.humansd/config/config.toml
```
