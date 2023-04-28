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
peers="ca1e46048e4a9b65d60bc9e749aa431401f34ed7@144.76.45.59:26656,8c3c25fa9cd6289d0342cf0e42916f381a1fd671@78.46.64.59:26656,62faee4c6224b3562d7123acea58180021c8b47b@162.55.173.57:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:22656,34fd880f1bf2eb7b7481436d0746bbc05a4a5805@144.76.97.35:26656,ceba57f1376d4949cc0419918d110f0085b24b25@135.181.113.225:26656,7acb02817755961e446859eef57c494687e3330f@162.244.35.40:26656,4762fa22edb91acd78010026f8da5fb71e174acb@142.165.207.19:36656,c94e42eec8bcc7f6db81748a97e5f10d59710e95@135.181.138.160:26656,497886715ac23475f7428bd177b9fa53ff886a8d@78.46.80.79:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.humansd/config/config.toml
```
