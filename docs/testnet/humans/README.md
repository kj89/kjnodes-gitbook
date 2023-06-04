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

**live-peers** (11)
```bash
peers="946b549550e9c564193bf4c963d84b17e5415a50@136.243.136.241:26656,0ae23e03040dd3e3a6c3a2326c62a206f531d671@162.19.31.150:26656,fa9eb901a01430d928e71162151992c7afb51d62@178.23.126.70:26656,ceba57f1376d4949cc0419918d110f0085b24b25@135.181.113.225:26656,e6489cf86b51fa37cae968ccbbda1da03b742a5e@128.140.56.206:26656,be5158df5152ec7e6a4eca04c89e40494d19927c@51.79.101.159:26656,a7eaa41b5565295810b81641e0bf11a9fb2ca54e@159.69.69.183:26656,b1f13e9971cfdcf784fb0efbd1b72417d5410a02@195.201.59.194:26656,6e2dac7a826fa2c21867dc6620b5945574a89865@65.109.155.238:29656,42f95015c31c7814b6a0a717fd8c63d15f896e88@94.237.27.19:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:12256"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.humansd/config/config.toml
```
