# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/humans.png" alt=""><figcaption></figcaption></figure>

Humans is Blockchain of AIs. It is the first blockchain network  from the Cosmos ecosystem capable of managing, deploying and  executing artificial intelligence on the blockchain.

**Chain ID**: humans_3000-1 | **Latest Version Tag**: v0.1.0 | **Wasm**: OFF

[Website](https://humans.ai) | [Discord](https://discord.gg/humansdotai) | [Twitter](https://twitter.com/humansdotai)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/humans-testnet](https://explorer.kjnodes.com/humans-testnet)

## Public endpoints

* api: [https://humans-testnet.api.kjnodes.com](https://humans-testnet.api.kjnodes.com)
* rpc: [https://humans-testnet.rpc.kjnodes.com](https://humans-testnet.rpc.kjnodes.com)
* grpc: humans-testnet.grpc.kjnodes.com:22090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@humans-testnet.rpc.kjnodes.com:22656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@humans-testnet.rpc.kjnodes.com:22659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/humans-testnet/addrbook.json > $HOME/.humansd/config/addrbook.json
```

**live-peers** (10)
```bash
peers="86768c62c83fcdeb54514b33b33ab44fd9fa5c05@49.13.9.135:26656,ca1e46048e4a9b65d60bc9e749aa431401f34ed7@144.76.45.59:26656,5b92ede5e88c5029d6c7b3b360b9cf59051ce409@65.109.84.33:26656,69a6d587d4bd0d9f37404dbc03029c6220bde175@81.30.157.35:19656,0844b9e6e2cb9c7d7a3eaa037f9e16ac66c9005c@5.161.64.185:26656,8c3c25fa9cd6289d0342cf0e42916f381a1fd671@78.46.64.59:26656,b52e0c6553fb42b5899b93dd584959db2bb23422@95.217.200.36:26656,eef1079a50870610126bd504dbbd89b6a13b160b@65.108.72.253:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:22656,b1639fb460c9f55bb3acc3006df64ac5013f1412@91.194.30.203:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.humansd/config/config.toml
```
