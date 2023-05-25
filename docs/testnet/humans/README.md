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
peers="b1f13e9971cfdcf784fb0efbd1b72417d5410a02@195.201.59.194:26656,1ac5cfbf03df14b6c41d09d9f284e75cf03f5742@202.61.236.219:26656,e41b5c547ebf5dd2e96d30efbd9d4c5c32e2f3a6@161.97.175.119:26656,442c270ecf448899ff266899b3e8fd819456b52d@185.252.232.85:26656,d792d994b50e546cef27f177f549090e6e41476f@69.197.6.24:26656,5e1f23a66fafd1a73871f055a6dd2165c01fe1c2@65.109.25.62:26656,946b549550e9c564193bf4c963d84b17e5415a50@136.243.136.241:26656,650b54b9fed877f05e8f2fa9b1a046e5a601a7c9@135.181.138.160:26656,4a6451353a1040ccb2638de485feda28d40416cd@65.109.84.103:26656,59ad24780f3d8b90da29079a8a386aa1355969ef@144.76.45.59:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:12256"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.humansd/config/config.toml
```
