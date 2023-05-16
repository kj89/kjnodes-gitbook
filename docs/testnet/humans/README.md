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
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:12256,733ffab95701aeebbc3021e827a7ef5f5c0dd93c@144.76.97.35:26656,42f95015c31c7814b6a0a717fd8c63d15f896e88@94.237.27.19:26656,ef4cf8c00b34de7a8c1eba725ac91a93c085781c@38.146.3.210:18456,fa9eb901a01430d928e71162151992c7afb51d62@178.23.126.70:26656,35ad999115e2a58540f6cf3bc3b90cc3adc9debc@65.109.116.95:26656,b1639fb460c9f55bb3acc3006df64ac5013f1412@91.194.30.203:26656,5e1f23a66fafd1a73871f055a6dd2165c01fe1c2@65.109.25.62:26656,5ca0389db000da1ce87d992816a4aefa387c3998@143.110.190.223:26656,4762fa22edb91acd78010026f8da5fb71e174acb@142.165.207.19:36656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.humansd/config/config.toml
```
