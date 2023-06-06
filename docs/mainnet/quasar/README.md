# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/quasar.png" alt=""><figcaption></figcaption></figure>

Quasar (pronounced QWAY-ZAR) is a decentralized  appchain enabling interchain digital asset management.

**Chain ID**: quasar-1 | **Latest Version Tag**: v0.1.1 | **Wasm**: ON

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
peers="a7d96dc929824613315dcc1c90fee119f28cc51f@134.65.193.189:26656,1993e3bee8826be9fd617720eebe83f826a8ebcf@51.89.7.235:26647,88cc4d314c9804a9478e900b6f18a83ea58a98c6@57.128.20.163:18256,5a111b281852be31838ecf1202e59981e618355e@89.116.31.95:18256,bccdc6cb3a0785bf3ee65d98c38bdd62bb843285@141.95.157.139:18256,d7ea38275af96271fd66194dad3951ef38b8ba7c@193.70.33.64:18256,6f9e244b6e225241c02b235f700c2b0788da982d@148.113.159.22:18256,0f7eca0da978e4304bb81fa1b9d9a1c87c57f45d@38.146.3.147:18256,6f95ddfd08c07249c4efafb781eb30ca5739b223@65.109.93.44:18256,a286b35c9e9626cc7b780120ebe4afa883c059ce@144.76.40.53:18256,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:14856"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quasarnode/config/config.toml
```
