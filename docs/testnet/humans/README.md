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
peers="b1f13e9971cfdcf784fb0efbd1b72417d5410a02@195.201.59.194:26656,6271d80b8fc42da3a2825cc5ef75818dd52423d1@138.201.121.185:26656,e41b5c547ebf5dd2e96d30efbd9d4c5c32e2f3a6@161.97.175.119:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:12256,df5cb643d8aeade8ef288a3dd90e4fd8220954ba@162.55.243.211:36656,497886715ac23475f7428bd177b9fa53ff886a8d@78.46.80.79:26656,fa9eb901a01430d928e71162151992c7afb51d62@178.23.126.70:26656,be5158df5152ec7e6a4eca04c89e40494d19927c@51.79.101.159:26656,1ac5cfbf03df14b6c41d09d9f284e75cf03f5742@202.61.236.219:26656,0ae23e03040dd3e3a6c3a2326c62a206f531d671@162.19.31.150:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.humansd/config/config.toml
```
