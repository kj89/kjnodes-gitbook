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
peers="59ad24780f3d8b90da29079a8a386aa1355969ef@144.76.45.59:26656,946b549550e9c564193bf4c963d84b17e5415a50@136.243.136.241:26656,f8ae768832a2665c915c3965a5bb8dc1031d5c1e@46.4.23.42:16656,42f95015c31c7814b6a0a717fd8c63d15f896e88@94.237.27.19:26656,417089d6681abacc685c2eff9e029d85231a04a0@141.95.34.193:46656,0ae23e03040dd3e3a6c3a2326c62a206f531d671@162.19.31.150:26656,ceba57f1376d4949cc0419918d110f0085b24b25@135.181.113.225:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:12256,757df37416499e6936a882a9b43985795503bc22@65.108.195.29:22656,907cb9da5d7d7182a80a6e38aad59bd067059bb3@65.21.200.54:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.humansd/config/config.toml
```
