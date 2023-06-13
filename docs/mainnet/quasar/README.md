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

**live-peers** (10)
```bash
peers="201eb8fc1e84beb4bdce8ae5614c7abb41e32edb@65.109.160.91:18256,d2247f7b919f0781c90ee61958d7044665a22d38@169.155.169.84:26656,a40e1d5f63fad9e14edb9c95458b27f3c1de858c@116.203.236.246:26618,768d3ca8922cb9c4d31f521a86491923ac2a672b@162.55.245.149:2040,bccdc6cb3a0785bf3ee65d98c38bdd62bb843285@141.95.157.139:18256,d7ea38275af96271fd66194dad3951ef38b8ba7c@193.70.33.64:18256,367d65ece0aafd9b46e15b9dd58fe319d7d29550@143.198.172.109:26656,0f7eca0da978e4304bb81fa1b9d9a1c87c57f45d@38.146.3.147:18256,58a4943a150cc77ab77ded222c44b23548ee702a@146.59.81.23:26667,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:14856"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quasarnode/config/config.toml
```
