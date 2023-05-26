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
peers="6271d80b8fc42da3a2825cc5ef75818dd52423d1@138.201.121.185:26656,b9767aa2312748caaf67425890768d85186b69b1@5.9.87.205:26646,497886715ac23475f7428bd177b9fa53ff886a8d@78.46.80.79:26656,b1f13e9971cfdcf784fb0efbd1b72417d5410a02@195.201.59.194:26656,0ae23e03040dd3e3a6c3a2326c62a206f531d671@162.19.31.150:26656,564fe1660c058471914d7653bef14e4e214045f9@135.181.142.117:26656,907cb9da5d7d7182a80a6e38aad59bd067059bb3@65.21.200.54:26656,59ad24780f3d8b90da29079a8a386aa1355969ef@144.76.45.59:26656,5b92ede5e88c5029d6c7b3b360b9cf59051ce409@65.109.84.33:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:12256"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.humansd/config/config.toml
```
