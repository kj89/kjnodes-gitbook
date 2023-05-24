# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/quasar.png" alt=""><figcaption></figcaption></figure>

Quasar (pronounced QWAY-ZAR) is a decentralized  appchain enabling interchain digital asset management.

**Chain ID**: quasar-1 | **Latest Version Tag**: v0.1.0 | **Wasm**: ON

[Website](https://www.quasar.fi) | [Discord](https://discord.gg/quasarfi) | [Twitter](https://twitter.com/QuasarFi)



Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/quasar](https://explorer.kjnodes.com/quasar)

## Public endpoints

* api: [https://quasar.api.kjnodes.com](https://quasar.api.kjnodes.com)
* rpc: [https://quasar.rpc.kjnodes.com](https://quasar.rpc.kjnodes.com)
* grpc: quasar.grpc.kjnodes.com:14890

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@quasar.rpc.kjnodes.com:14856
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@quasar.rpc.kjnodes.com:14859
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/quasar/addrbook.json > $HOME/.quasarnode/config/addrbook.json
```

**live-peers** (11)
```bash
peers="1bf81f0f4e35769d075300bc46e3998d63bf2bb2@135.181.210.186:26656,89757803f40da51678451735445ad40d5b15e059@169.155.169.149:26656,771659b9205187f9094f894c65d29effa79fdd2c@18.156.191.84:26656,1369d544be2680e031b57f30a8d18cbe8b17a8ef@54.38.73.121:26656,ff8bfc8a197e279810ccb21acdd987dfd6d3eb54@81.0.248.60:18256,6cceba286b498d4a1931f85e35ea0fa433373057@169.155.170.222:26656,471518432477e31ea348af246c0b54095d41352c@134.65.195.144:26656,d7ea38275af96271fd66194dad3951ef38b8ba7c@193.70.33.64:18256,664d2f6124721b1633b5a24452f85c1bf00c4bfc@66.85.158.165:26656,367d65ece0aafd9b46e15b9dd58fe319d7d29550@143.198.172.109:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:14856"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quasarnode/config/config.toml
```
