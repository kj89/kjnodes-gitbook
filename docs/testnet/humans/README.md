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
peers="2685f8e77fec93c99a55f2adb13835a50124d04e@135.181.18.112:55686,946b549550e9c564193bf4c963d84b17e5415a50@136.243.136.241:26656,6e2dac7a826fa2c21867dc6620b5945574a89865@65.109.155.238:29656,311973d7b6ed817b79e924a06c2344c9de4319df@65.109.116.95:26656,907cb9da5d7d7182a80a6e38aad59bd067059bb3@65.21.200.54:26656,b99df5397a6104fac055f21195f1fb25b77f5704@65.109.92.79:17656,be5158df5152ec7e6a4eca04c89e40494d19927c@51.79.101.159:26656,945422039658c95372b0b4f45c24ec4a5f849206@38.146.3.209:26656,19230fad7145e6fe80566a72f66b9ca3ec3f04d5@212.47.234.144:26656,b9767aa2312748caaf67425890768d85186b69b1@5.9.87.205:26646"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.humansd/config/config.toml
```
