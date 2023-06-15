# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/source.png" alt=""><figcaption></figcaption></figure>

Source is a decentralized, permissionless, and censorship resistant layer 1 proof-of-stake blockchain built in the Cosmos Zone ecosystem.

**Chain ID**: sourcechain-testnet | **Latest Version Tag**: v1.0.0 | **Wasm**: ON

[Website](https://www.sourceprotocol.io) | [Discord](https://discord.io/SourceProtocol) | [Twitter](https://www.twitter.com/sourceprotocol_)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/source-testnet](https://explorer.kjnodes.com/source-testnet)

## Public endpoints

* api: [https://source-testnet.api.kjnodes.com](https://source-testnet.api.kjnodes.com)
* rpc: [https://source-testnet.rpc.kjnodes.com](https://source-testnet.rpc.kjnodes.com)
* grpc: source-testnet.grpc.kjnodes.com:12890

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@source-testnet.rpc.kjnodes.com:12856
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@source-testnet.rpc.kjnodes.com:12859
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/source-testnet/addrbook.json > $HOME/.source/config/addrbook.json
```

**live-peers** (12)
```bash
peers="42bb6ea45070248f5ea1d7c26db7665498a5b8c4@173.249.42.162:28656,805c327443d9a2b425d16a402c23cb9cbfa36388@178.18.243.46:26656,db69700d8b0c277183ab1ec34d79a083c2578d32@65.21.145.209:26656,c27d26527c2f8a097c5a99800809d15338ac3bdb@95.217.207.236:20056,03d324b03078e3bd38c7c7550988362d11106ce4@135.181.198.246:26656,a833e9d068c7f5f32f411662c0430196a88aee91@65.109.65.248:28656,636c7206a1a9a817768766a1f243d27398159028@144.76.97.251:36656,6aba831746663a3f1b4fbeb30f836ef442ec02da@46.17.250.108:46656,46ae715de3bcf284ff997b841e6e82f279e3654f@154.26.153.179:26656,67958f716999fdc47fac777f0605a1911653ae86@65.109.48.181:30656,756368e62cbff16f8d0edcc4d169a090464bed53@38.242.194.233:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:12856"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.source/config/config.toml
```
