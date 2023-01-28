# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/okp4.png" width="150" alt=""><figcaption></figcaption></figure>

OKP4 is a revolutionary public blockchain protocol where communities are incentivized to  share data and services confidently. To maximize value from data, it needs to be processed  by complex algorithms and pooled with other datasets, to create valuable knowledge.

**Chain ID**: okp4-nemeton-1 | **Latest Version Tag**: v3.0.0 | **Wasm**: OFF

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

**live-peers** (37)
```bash
peers="95986e08f5baee420d3b72be67826e321663072b@65.109.85.221:6070,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:36656,99f6675049e22a0216af0e2447e7a4c5021874cd@142.132.132.200:28656,269d246537499d05698c183497c4263e899036a4@65.108.9.164:35656,ebc272824924ea1a27ea3183dd0b9ba713494f83@95.214.55.198:26996,034c2fbca12a8ced548d3225bcd21bdf1216a1b3@65.109.49.163:11203,fe8bd9375c43a7cc6ef27e62d56af341a62e67c9@95.217.202.49:30656,7dfc61d3ac9f6da7fa9f4893bc0ffa17ef8006e6@185.111.159.139:36656,8cdeb85dada114c959c36bb59ce258c65ae3a09c@88.198.242.163:36656,b0b56d944cf1cc569a1e77e0923e075bad94d755@141.95.145.41:28656,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.55.232:26996,d1a0ff9bd7ea1ebd06bc7158f3523f5e557328be@163.172.131.169:26656,be9841ace1d71a4c7681918ee39f5e00d8e96a82@213.239.216.252:36656,cc8bc81fea49a6a412992bb3e2c3f211d9e675c8@88.99.161.162:21656,09f116943144c71608d98d78c2d89de82855e8a7@65.109.19.173:51656,2bfd405e8f0f176428e2127f98b5ec53164ae1f0@142.132.149.118:26656,99a7a548357ca9b5d5e11e235f0fd7cbce9a38a4@178.128.85.30:36656,ba469aac96159dbb49844406423180618d267007@65.108.120.21:26113,3bcc5bf2652c8288af50dfe1677350ff1aa598f3@65.108.77.250:26656,473369a53bfa8a0ac4af5a191407b30bc82e83be@74.208.94.42:14656,d4305fcb7b20dc96481a6ae6ae84f281f3413a4e@65.109.37.58:13656,74349a1cb9479b291866debe2042de8a2e88b850@65.108.233.109:17656,9d1482bc31fb4578a5c7f7f65c4e0aaf2dfc2336@213.239.215.77:36656,052e10ce23cce3249f61853e2ca6a63102b7bddb@5.161.97.198:26656,f7fb0f3248e4aed14e89bc4967d48c66b72e6f62@135.181.147.169:26656,8a7605d8ae4338de5b7a0d5c70244ce05e377630@85.10.200.221:26656,eff365c8e0e2f99026e3dd91704d3764eb38e0a1@65.108.13.212:26756,30092d2717053f1c0813e8354c07c761c9c3ac5c@194.163.161.234:26656,307fb25cd6998d0d5bd1d947571f6043c6bb4069@65.109.31.114:2280,a490691c2a423573cb93bc23b13967ed9db0e3ff@146.190.44.218:26656,540e0e9b33b2d87315fdf7089404671581d36e94@95.217.203.43:26656,26114bc5cb42ef90be2aba5b4b6d82bab7a60c31@185.255.131.17:26656,fa04503a35476204861f06b75be4839562205527@65.109.85.226:6070,854cc8b83a48ba4394c1940b57d0f42ec013e033@38.242.251.204:26656,9a1e456bebf152b65c2087896779e259633ecbef@157.90.34.111:26656,2f6d5a319ebee0201dff4a0e3b7526d0863a4d32@65.109.85.225:6070,23e895e7d650f43e1f53522165607b71685f8cfa@65.108.75.107:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.okp4d/config/config.toml
```
