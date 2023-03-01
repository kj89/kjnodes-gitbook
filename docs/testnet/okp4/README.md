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

**live-peers** (36)
```bash
peers="e755eb8016c2f6f5303b2f8d503d9126d235e80f@138.201.35.56:26656,8cdeb85dada114c959c36bb59ce258c65ae3a09c@88.198.242.163:36656,d7d3e978951ccf946f0e33805778c1961ad42819@31.7.196.21:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:36656,ead118d7cbe51cbabf5a77b69db7255512f41023@88.208.34.134:60656,7dfc61d3ac9f6da7fa9f4893bc0ffa17ef8006e6@185.111.159.139:36656,d132ad0c5b2afd0eab2d87351eeda46dc9d69312@46.228.205.200:26656,99f6675049e22a0216af0e2447e7a4c5021874cd@142.132.132.200:28656,42fbb917fca6787bc3ab774865f4bb1ef950f114@65.108.226.26:30656,854cc8b83a48ba4394c1940b57d0f42ec013e033@38.242.251.204:26656,b0b56d944cf1cc569a1e77e0923e075bad94d755@141.95.145.41:28656,fff0a8c202befd9459ff93783a0e7756da305fe3@38.242.150.63:16656,fe8bd9375c43a7cc6ef27e62d56af341a62e67c9@95.217.202.49:30656,74349a1cb9479b291866debe2042de8a2e88b850@65.108.233.109:17656,874373b78d2cd50e716aa464bf407581d9305655@94.250.201.130:27656,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.55.232:26996,d1a0ff9bd7ea1ebd06bc7158f3523f5e557328be@163.172.135.127:26656,473369a53bfa8a0ac4af5a191407b30bc82e83be@74.208.94.42:14656,be9841ace1d71a4c7681918ee39f5e00d8e96a82@213.239.216.252:36656,d4305fcb7b20dc96481a6ae6ae84f281f3413a4e@65.109.37.58:13656,5c5bf00059349042504c1e7d0449c4ac6ee37fc2@142.132.202.50:11114,6a66a38bdd5895ec6f1ce18b3430860a30e18e02@142.132.149.118:26656,a06417f8518fbf6f779e4012dbf72f194a95b48f@65.21.138.124:33656,307fb25cd6998d0d5bd1d947571f6043c6bb4069@65.109.31.114:2280,eef77b5ae1c37f3e5809ff928c329dde906be388@65.108.133.73:21656,5a460ead06c5fc1d6d70a1f858d874bf53463a4a@149.102.143.145:31656,2c6b5af41689145abb85f95cb49131ae9e193142@217.13.223.167:61356,9d1482bc31fb4578a5c7f7f65c4e0aaf2dfc2336@213.239.215.77:36656,8a7605d8ae4338de5b7a0d5c70244ce05e377630@85.10.200.221:26656,1655cdc8fdfe1dc2209d47ff68c02a417ef9ed52@135.181.222.179:31656,ebc272824924ea1a27ea3183dd0b9ba713494f83@95.214.55.198:26996,e9255dd3341db6cadf73b4f151c97e0cd14f0efb@65.108.45.200:27464,2f6d5a319ebee0201dff4a0e3b7526d0863a4d32@65.109.85.225:6070,c6abcdff7b29159bf5be14f43c8e877648136468@51.159.2.19:23098,9755cab2585a2794453a5b396ef13b893393366f@65.108.212.224:46673,ade4d8bc8cbe014af6ebdf3cb7b1e9ad36f412c0@176.9.82.221:17656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.okp4d/config/config.toml
```
