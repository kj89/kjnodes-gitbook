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

**live-peers** (9)
```bash
peers="907cb9da5d7d7182a80a6e38aad59bd067059bb3@65.21.200.54:26656,2685f8e77fec93c99a55f2adb13835a50124d04e@135.181.18.112:55686,d70c9343af28023a78aceb653e885666c12fec3b@138.201.121.185:26687,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:12256,6e2dac7a826fa2c21867dc6620b5945574a89865@65.109.155.238:29656,b99df5397a6104fac055f21195f1fb25b77f5704@65.109.92.79:17656,5e1f23a66fafd1a73871f055a6dd2165c01fe1c2@65.109.25.62:26656,35ad999115e2a58540f6cf3bc3b90cc3adc9debc@65.109.116.95:26656,c467f8c292dbbebc654c8429956d15f09eb38a1d@65.109.13.83:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.humansd/config/config.toml
```
