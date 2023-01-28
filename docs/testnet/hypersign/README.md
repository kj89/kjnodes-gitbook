# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/hypersign.png" width="150" alt=""><figcaption></figcaption></figure>

Hypersign is a decentralized identity layer for the internet, giving  users control of their personal data and identity whilst digital  enabling trust for businesses.

**Chain ID**: jagrat | **Latest Version Tag**: v0.1.5 | **Wasm**: OFF

[Website](https://hypersign.id) | [Discord](https://discord.gg/DmuUjMrHVw) | [Twitter](https://twitter.com/hypersignchain)


## Chain explorer
[https://explorer.kjnodes.com/hypersign-testnet](https://explorer.kjnodes.com/hypersign-testnet)

## Public endpoints

* api: [https://hypersign-testnet.api.kjnodes.com](https://hypersign-testnet.api.kjnodes.com)
* rpc: [https://hypersign-testnet.rpc.kjnodes.com](https://hypersign-testnet.rpc.kjnodes.com)
* grpc: [https://hypersign-testnet.grpc.kjnodes.com](https://hypersign-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@hypersign-testnet.rpc.kjnodes.com:31656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@hypersign-testnet.rpc.kjnodes.com:31659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/hypersign-testnet/addrbook.json > $HOME/.hid-node/config/addrbook.json
```

**live-peers** (10)
```bash
peers="7d85caec437cc8c0a504d6ab3b18fd07c173b2fb@94.130.219.37:26001,5b4482bfe02384184470070c3d3a4465cf0c18d4@144.91.82.61:31656,c1b6d86f46eab9d0aa2e4399cddb9cf05d13621a@65.108.206.118:60556,aa8c0064e866dc57b341a389006df8925a0718fe@5.161.55.130:31656,ec5127072c252f7246fb66f7e7762423a23ff6bd@154.12.228.93:31656,3990d5a402ca8f9e53441b02e22f4558c5c85fc5@65.108.44.149:27756,7b67ef0b793f09bc1bc76d29aa1503aab8a224ad@88.99.161.162:15656,1e3f0aeb6f2a2017b122af2461a75c9695790954@65.108.233.109:10956,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:31656,d7c9b9a3c3a6c5f4ccdfb37a8358755b277271c1@3.110.226.164:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.hid-node/config/config.toml
```
