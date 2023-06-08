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
peers="7bb61943f683af93e6ac1a9cf43e4668f4d3304f@116.202.227.117:12256,f8ae768832a2665c915c3965a5bb8dc1031d5c1e@46.4.23.42:16656,bc098ac0149a0a06701e29e4f7c79cac65c25c7f@162.55.173.57:26656,e6489cf86b51fa37cae968ccbbda1da03b742a5e@128.140.56.206:26656,0ae23e03040dd3e3a6c3a2326c62a206f531d671@162.19.31.150:26656,5b92ede5e88c5029d6c7b3b360b9cf59051ce409@65.109.84.33:26656,d7eb0e65cecbeeaa649b0a2fdf95ca2fb9f0cc3e@206.125.33.0:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:12256,42f95015c31c7814b6a0a717fd8c63d15f896e88@94.237.27.19:26656,945422039658c95372b0b4f45c24ec4a5f849206@38.146.3.209:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.humansd/config/config.toml
```
