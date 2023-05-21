# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/humans.png" alt=""><figcaption></figcaption></figure>

Humans is Blockchain of AIs. It is the first blockchain network  from the Cosmos ecosystem capable of managing, deploying and  executing artificial intelligence on the blockchain.

**Chain ID**: humans_3000-23 | **Latest Version Tag**: v0.2.2 | **Wasm**: OFF

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
peers="6271d80b8fc42da3a2825cc5ef75818dd52423d1@138.201.121.185:26656,a41f29c2d498b232c18f75364e38cee06fac198d@78.46.64.59:26656,417089d6681abacc685c2eff9e029d85231a04a0@141.95.34.193:46656,0ae23e03040dd3e3a6c3a2326c62a206f531d671@162.19.31.150:26656,5e1f23a66fafd1a73871f055a6dd2165c01fe1c2@65.109.25.62:26656,2685f8e77fec93c99a55f2adb13835a50124d04e@135.181.18.112:55686,5ca0389db000da1ce87d992816a4aefa387c3998@143.110.190.223:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:12256,22ccc03acda4e7230f779dc3955a0097a32c358e@69.197.6.24:26656,ceba57f1376d4949cc0419918d110f0085b24b25@135.181.113.225:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.humansd/config/config.toml
```
