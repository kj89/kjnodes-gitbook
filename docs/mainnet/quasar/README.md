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

**live-peers** (30)
```bash
peers="d11f867df7e498de0835e2d1b5bc34334c7337d1@65.109.31.114:2490,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:48656,d2247f7b919f0781c90ee61958d7044665a22d38@169.155.169.84:26656,a286b35c9e9626cc7b780120ebe4afa883c059ce@144.76.40.53:18256,88cc4d314c9804a9478e900b6f18a83ea58a98c6@57.128.20.163:18256,367d65ece0aafd9b46e15b9dd58fe319d7d29550@143.198.172.109:26656,6f9e244b6e225241c02b235f700c2b0788da982d@148.113.159.22:18256,2028d1984d4828fb5662225d12db1a8722b9bfab@135.181.215.62:4740,5a111b281852be31838ecf1202e59981e618355e@89.116.31.95:18256,bccdc6cb3a0785bf3ee65d98c38bdd62bb843285@141.95.157.139:18256,66e0a7d2c2fc75a91627085d0ac5681a35dfd408@37.252.184.234:26656,201eb8fc1e84beb4bdce8ae5614c7abb41e32edb@65.109.160.91:18256,ff8bfc8a197e279810ccb21acdd987dfd6d3eb54@81.0.248.60:18256,298e0e1faf8a5da43514cc2908d2908658e732a0@38.146.3.148:18256,6128f51914659e0ee2c57970d84223404fe5e5ce@65.108.137.36:26656,8688b59432d98b6ded8bed01c3c29d4892ae6e4f@38.146.3.149:18256,1c4d42123dc63fba03bc28d2b5a837879e7de979@162.55.245.149:2040,10e73ac4ab3f9e1edd89e1aa342eb4d4f11120f0@135.181.128.114:18256,6cceba286b498d4a1931f85e35ea0fa433373057@169.155.170.222:26656,97e4468ac589eac505a800411c635b14511a61bb@134.65.195.240:26656,e726816f42831689eab9378d5d577f1d06d25716@176.9.188.21:26656,d7ea38275af96271fd66194dad3951ef38b8ba7c@193.70.33.64:18256,6f95ddfd08c07249c4efafb781eb30ca5739b223@65.109.93.44:18256,dc0a7aa89cc33c93b878ca68b4263af77daafc66@65.21.200.7:1270,e1b058e5cfa2b836ddaa496b10911da62dcf182e@65.21.136.170:58656,f2e7f8af9e5f72bcde83a8bc0ca05aded6d51a5e@103.180.28.199:26656,1bf81f0f4e35769d075300bc46e3998d63bf2bb2@135.181.210.186:26656,bbf8c1562c20726a436f1c1476ad49e560ca179b@51.89.190.33:26656,4a95d1523814b34c2469e62461d67b8ccef2ab02@34.28.193.244:26656,c97640c7c53a32ff301c09b261bbccb35c286dba@65.109.50.30:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quasarnode/config/config.toml
```
