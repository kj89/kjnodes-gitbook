# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/okp4.png" width="150" alt=""><figcaption></figcaption></figure>

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

**live-peers** (41)
```bash
peers="23e895e7d650f43e1f53522165607b71685f8cfa@65.108.75.107:26656,61a8b9fdd5c21ebe6c02359cb192a4eda13d44cb@135.181.139.153:26656,8527f34bd6e542304809386896997d12d80e5e0e@65.108.237.232:29656,d1c1b729eff9afe7dfd371f190df6282c82ccfad@65.109.89.5:31656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:36656,ead118d7cbe51cbabf5a77b69db7255512f41023@88.208.34.134:60656,99f6675049e22a0216af0e2447e7a4c5021874cd@142.132.132.200:28656,874373b78d2cd50e716aa464bf407581d9305655@94.250.201.130:27656,d132ad0c5b2afd0eab2d87351eeda46dc9d69312@46.228.205.200:26656,ba469aac96159dbb49844406423180618d267007@65.108.120.21:26113,7dfc61d3ac9f6da7fa9f4893bc0ffa17ef8006e6@185.111.159.139:36656,854cc8b83a48ba4394c1940b57d0f42ec013e033@38.242.251.204:26656,b0b56d944cf1cc569a1e77e0923e075bad94d755@141.95.145.41:28656,d1a0ff9bd7ea1ebd06bc7158f3523f5e557328be@163.172.135.127:26656,42fbb917fca6787bc3ab774865f4bb1ef950f114@65.108.226.26:30656,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.55.232:26996,052e10ce23cce3249f61853e2ca6a63102b7bddb@5.161.97.198:26656,473369a53bfa8a0ac4af5a191407b30bc82e83be@74.208.94.42:14656,be9841ace1d71a4c7681918ee39f5e00d8e96a82@213.239.216.252:36656,8cdeb85dada114c959c36bb59ce258c65ae3a09c@88.198.242.163:36656,c6abcdff7b29159bf5be14f43c8e877648136468@51.159.2.19:23098,540e0e9b33b2d87315fdf7089404671581d36e94@95.217.203.43:26656,d4305fcb7b20dc96481a6ae6ae84f281f3413a4e@65.109.37.58:13656,6a66a38bdd5895ec6f1ce18b3430860a30e18e02@142.132.149.118:26656,643988550263605405a7968c38fd11653bf75cd0@38.242.252.104:26656,8a7605d8ae4338de5b7a0d5c70244ce05e377630@85.10.200.221:26656,9928d19b7663a6fa639eb7c1ee239e671edcbdb2@5.9.147.22:26616,eef77b5ae1c37f3e5809ff928c329dde906be388@65.108.133.73:21656,74349a1cb9479b291866debe2042de8a2e88b850@65.108.233.109:17656,7ba5d3721d98efd479b2a3f3b4df6ebd5fd2f119@109.123.243.135:26656,307fb25cd6998d0d5bd1d947571f6043c6bb4069@65.109.31.114:2280,c3db3a07493e8f04d93a9228998ae799fa89877f@5.78.48.118:26656,c2545ea3d87dd63d5c6140c1550284d3814b642a@143.198.143.131:26656,9392c27a9a561c31e7a920dc6f577d663c473ef8@154.12.225.88:26656,9d1482bc31fb4578a5c7f7f65c4e0aaf2dfc2336@213.239.215.77:36656,fe8bd9375c43a7cc6ef27e62d56af341a62e67c9@95.217.202.49:30656,30092d2717053f1c0813e8354c07c761c9c3ac5c@194.163.161.234:26656,78d923333e39e747c6a7fbfcc822ec6279990556@91.211.251.232:28656,1e48c09a0f78070e90ed49b2e3d59f8fdc188e74@162.55.234.70:55156,9755cab2585a2794453a5b396ef13b893393366f@65.108.212.224:46673,ade4d8bc8cbe014af6ebdf3cb7b1e9ad36f412c0@176.9.82.221:17656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.okp4d/config/config.toml
```
