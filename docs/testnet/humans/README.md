# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/humans.png" alt=""><figcaption></figcaption></figure>

Humans is Blockchain of AIs. It is the first blockchain network  from the Cosmos ecosystem capable of managing, deploying and  executing artificial intelligence on the blockchain.

**Chain ID**: humans_3000-23 | **Latest Version Tag**: v0.2.1 | **Wasm**: OFF

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
peers="6271d80b8fc42da3a2825cc5ef75818dd52423d1@138.201.121.185:26656,946b549550e9c564193bf4c963d84b17e5415a50@136.243.136.241:26656,b1f13e9971cfdcf784fb0efbd1b72417d5410a02@195.201.59.194:26656,a41f29c2d498b232c18f75364e38cee06fac198d@78.46.64.59:26656,f05366147458d2d09ff525f8b4258a7978f72991@162.55.173.57:26656,459bcaea161d20cddcdead811d282bd495446cbb@135.181.142.117:26656,907cb9da5d7d7182a80a6e38aad59bd067059bb3@65.21.200.54:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:12256,ceba57f1376d4949cc0419918d110f0085b24b25@135.181.113.225:26656,be5158df5152ec7e6a4eca04c89e40494d19927c@51.79.101.159:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.humansd/config/config.toml
```
