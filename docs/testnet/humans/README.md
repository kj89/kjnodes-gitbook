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
peers="497886715ac23475f7428bd177b9fa53ff886a8d@78.46.80.79:26656,0ae23e03040dd3e3a6c3a2326c62a206f531d671@162.19.31.150:26656,ceba57f1376d4949cc0419918d110f0085b24b25@135.181.113.225:26656,907cb9da5d7d7182a80a6e38aad59bd067059bb3@65.21.200.54:26656,2685f8e77fec93c99a55f2adb13835a50124d04e@135.181.18.112:55686,5ca0389db000da1ce87d992816a4aefa387c3998@143.110.190.223:26656,757df37416499e6936a882a9b43985795503bc22@65.108.195.29:22656,3563bf0924f203b6b7c5e31c21c1de4a8f2e0949@178.23.126.92:26656,a7eaa41b5565295810b81641e0bf11a9fb2ca54e@159.69.69.183:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:12256"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.humansd/config/config.toml
```
