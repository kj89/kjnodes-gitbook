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
peers="d70c9343af28023a78aceb653e885666c12fec3b@138.201.121.185:26687,b99df5397a6104fac055f21195f1fb25b77f5704@65.109.92.79:17656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:12256,ef4cf8c00b34de7a8c1eba725ac91a93c085781c@38.146.3.210:18456,5e1f23a66fafd1a73871f055a6dd2165c01fe1c2@65.109.25.62:26656,6e2dac7a826fa2c21867dc6620b5945574a89865@65.109.155.238:29656,c467f8c292dbbebc654c8429956d15f09eb38a1d@65.109.13.83:26656,0ae23e03040dd3e3a6c3a2326c62a206f531d671@162.19.31.150:26656,907cb9da5d7d7182a80a6e38aad59bd067059bb3@65.21.200.54:26656,b77d993ac7b7e71a788284a7eff017d08711e1bb@51.79.82.138:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.humansd/config/config.toml
```
