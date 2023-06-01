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
peers="42f95015c31c7814b6a0a717fd8c63d15f896e88@94.237.27.19:26656,5b92ede5e88c5029d6c7b3b360b9cf59051ce409@65.109.84.33:26656,907cb9da5d7d7182a80a6e38aad59bd067059bb3@65.21.200.54:26656,650b54b9fed877f05e8f2fa9b1a046e5a601a7c9@135.181.138.160:26656,ceba57f1376d4949cc0419918d110f0085b24b25@135.181.113.225:26656,fd6bccda6c8c16ed694c1f447966202492a3945c@65.108.72.253:26656,be5158df5152ec7e6a4eca04c89e40494d19927c@51.79.101.159:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:12256,09e98344c96b5c0de8ba86bd417332b2b04d6b76@65.109.93.58:26656,19230fad7145e6fe80566a72f66b9ca3ec3f04d5@212.47.234.144:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.humansd/config/config.toml
```
