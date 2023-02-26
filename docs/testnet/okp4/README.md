# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/okp4.png" width="150" alt=""><figcaption></figcaption></figure>

OKP4 is a revolutionary public blockchain protocol where communities are incentivized to  share data and services confidently. To maximize value from data, it needs to be processed  by complex algorithms and pooled with other datasets, to create valuable knowledge.

**Chain ID**: okp4-nemeton-1 | **Latest Version Tag**: v4.0.0 | **Wasm**: OFF

[Website](https://okp4.network) | [Discord](https://discord.gg/okp4) | [Twitter](https://twitter.com/OKP4_Protocol)




## Chain explorer
[https://explorer.kjnodes.com/okp4-testnet](https://explorer.kjnodes.com/okp4-testnet)

## Public endpoints

* api: [https://okp4-testnet.api.kjnodes.com](https://okp4-testnet.api.kjnodes.com)
* rpc: [https://okp4-testnet.rpc.kjnodes.com](https://okp4-testnet.rpc.kjnodes.com)
* grpc: [https://okp4-testnet.grpc.kjnodes.com](https://okp4-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@okp4-testnet.rpc.kjnodes.com:36656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@okp4-testnet.rpc.kjnodes.com:36659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/okp4-testnet/addrbook.json > $HOME/.okp4d/config/addrbook.json
```

**live-peers** (40)
```bash
peers="1f4fa23210cc1d086a928a3c6de7c24f6c8f17ba@202.61.226.120:16656,052e10ce23cce3249f61853e2ca6a63102b7bddb@5.161.97.198:26656,d132ad0c5b2afd0eab2d87351eeda46dc9d69312@46.228.205.200:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:36656,7dfc61d3ac9f6da7fa9f4893bc0ffa17ef8006e6@185.111.159.139:36656,269d246537499d05698c183497c4263e899036a4@65.108.9.164:35656,ead118d7cbe51cbabf5a77b69db7255512f41023@88.208.34.134:60656,99f6675049e22a0216af0e2447e7a4c5021874cd@142.132.132.200:28656,42fbb917fca6787bc3ab774865f4bb1ef950f114@65.108.226.26:30656,ffbd1adeb58928c3f400fab23c84c3c73badd7fa@65.108.226.44:29656,eef77b5ae1c37f3e5809ff928c329dde906be388@65.108.133.73:21656,8cdeb85dada114c959c36bb59ce258c65ae3a09c@88.198.242.163:36656,b0b56d944cf1cc569a1e77e0923e075bad94d755@141.95.145.41:28656,874373b78d2cd50e716aa464bf407581d9305655@94.250.201.130:27656,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.55.232:26996,8a7605d8ae4338de5b7a0d5c70244ce05e377630@85.10.200.221:26656,c8771124d781b73a9184b8a3237f72837f167edd@5.75.205.215:26656,ae5be91a24a5a454dd7d51b7762666d6ddc795ee@185.144.99.18:26656,d1a0ff9bd7ea1ebd06bc7158f3523f5e557328be@163.172.135.127:26656,d7d3e978951ccf946f0e33805778c1961ad42819@31.7.196.21:26656,74349a1cb9479b291866debe2042de8a2e88b850@65.108.233.109:17656,fff0a8c202befd9459ff93783a0e7756da305fe3@38.242.150.63:16656,643988550263605405a7968c38fd11653bf75cd0@38.242.252.104:26656,473369a53bfa8a0ac4af5a191407b30bc82e83be@74.208.94.42:14656,8527f34bd6e542304809386896997d12d80e5e0e@65.108.237.232:29656,e9255dd3341db6cadf73b4f151c97e0cd14f0efb@65.108.45.200:27464,be9841ace1d71a4c7681918ee39f5e00d8e96a82@213.239.216.252:36656,307fb25cd6998d0d5bd1d947571f6043c6bb4069@65.109.31.114:2280,90481aeb2485505f8844a7347dac9abcf5f7acbe@5.75.190.38:26656,854cc8b83a48ba4394c1940b57d0f42ec013e033@38.242.251.204:26656,034c2fbca12a8ced548d3225bcd21bdf1216a1b3@65.109.49.163:11203,ef7c45199eb3cd79cbf7e906dcfa2c7de11e1499@167.235.15.19:32656,6a66a38bdd5895ec6f1ce18b3430860a30e18e02@142.132.149.118:26656,5c5bf00059349042504c1e7d0449c4ac6ee37fc2@142.132.202.50:11114,fe8bd9375c43a7cc6ef27e62d56af341a62e67c9@95.217.202.49:30656,9f55b6fbf5d246138cc88acfe193ac45aa49c288@31.7.196.148:26656,9d1482bc31fb4578a5c7f7f65c4e0aaf2dfc2336@213.239.215.77:36656,c6abcdff7b29159bf5be14f43c8e877648136468@51.159.2.19:23098,ebc272824924ea1a27ea3183dd0b9ba713494f83@95.214.55.198:26996,ade4d8bc8cbe014af6ebdf3cb7b1e9ad36f412c0@176.9.82.221:17656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.okp4d/config/config.toml
```
