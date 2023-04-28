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
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:22656,6271d80b8fc42da3a2825cc5ef75818dd52423d1@138.201.121.185:26656,ca1e46048e4a9b65d60bc9e749aa431401f34ed7@144.76.45.59:26656,62faee4c6224b3562d7123acea58180021c8b47b@162.55.173.57:26656,054c81f412213c90e77b295d6061a4a4b34d8f8f@141.95.99.214:14356,ceba57f1376d4949cc0419918d110f0085b24b25@135.181.113.225:26656,4762fa22edb91acd78010026f8da5fb71e174acb@142.165.207.19:36656,0ab5a0c4fd3d85462da5fa149f3eb6d5702a4f32@118.193.37.229:26656,c94e42eec8bcc7f6db81748a97e5f10d59710e95@135.181.138.160:26656,6f6a90701f3cc459a9007456fa84abf647a68ef5@159.69.69.183:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.humansd/config/config.toml
```
