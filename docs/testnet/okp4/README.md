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

**live-peers** (41)
```bash
peers="ffbd1adeb58928c3f400fab23c84c3c73badd7fa@65.108.226.44:29656,07023da2f1fd638d40e37d13741e8e3d5525b4f1@65.108.96.104:26656,cf5e82486c4568c29a20719a68210523826ceb00@65.108.229.102:26651,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:36656,99f6675049e22a0216af0e2447e7a4c5021874cd@142.132.132.200:28656,269d246537499d05698c183497c4263e899036a4@65.108.9.164:35656,7dfc61d3ac9f6da7fa9f4893bc0ffa17ef8006e6@185.111.159.139:36656,ba469aac96159dbb49844406423180618d267007@65.108.120.21:26113,8cdeb85dada114c959c36bb59ce258c65ae3a09c@88.198.242.163:36656,b0b56d944cf1cc569a1e77e0923e075bad94d755@141.95.145.41:28656,f17338ec41b1b68b07063984feb407d9038cf78b@65.108.142.47:26616,874373b78d2cd50e716aa464bf407581d9305655@94.250.201.130:27656,42fbb917fca6787bc3ab774865f4bb1ef950f114@65.108.226.26:30656,8577873589dc7ecb9f2e32f79fe51ef7f57e40a3@65.109.161.143:26656,e9255dd3341db6cadf73b4f151c97e0cd14f0efb@65.108.45.200:27464,be9841ace1d71a4c7681918ee39f5e00d8e96a82@213.239.216.252:36656,052e10ce23cce3249f61853e2ca6a63102b7bddb@5.161.97.198:26656,473369a53bfa8a0ac4af5a191407b30bc82e83be@74.208.94.42:14656,307fb25cd6998d0d5bd1d947571f6043c6bb4069@65.109.31.114:2280,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.55.232:26996,9d1482bc31fb4578a5c7f7f65c4e0aaf2dfc2336@213.239.215.77:36656,8a7605d8ae4338de5b7a0d5c70244ce05e377630@85.10.200.221:26656,2bfd405e8f0f176428e2127f98b5ec53164ae1f0@142.132.149.118:26656,d1a0ff9bd7ea1ebd06bc7158f3523f5e557328be@163.172.131.169:26656,82bb185819e5cf2bb6a9896447672efca27f28cb@65.109.15.202:26656,30092d2717053f1c0813e8354c07c761c9c3ac5c@194.163.161.234:26656,74349a1cb9479b291866debe2042de8a2e88b850@65.108.233.109:17656,8527f34bd6e542304809386896997d12d80e5e0e@65.108.237.232:29656,24fbac02738005cfa9d8263d01dc7cc113d6b708@162.248.225.244:26656,eef77b5ae1c37f3e5809ff928c329dde906be388@65.108.133.73:21656,d4305fcb7b20dc96481a6ae6ae84f281f3413a4e@65.109.37.58:13656,a06417f8518fbf6f779e4012dbf72f194a95b48f@65.21.138.124:33656,9a1e456bebf152b65c2087896779e259633ecbef@157.90.34.111:26656,fe8bd9375c43a7cc6ef27e62d56af341a62e67c9@95.217.202.49:30656,034c2fbca12a8ced548d3225bcd21bdf1216a1b3@65.109.49.163:11203,c2545ea3d87dd63d5c6140c1550284d3814b642a@143.198.143.131:26656,ebc272824924ea1a27ea3183dd0b9ba713494f83@95.214.55.198:26996,26114bc5cb42ef90be2aba5b4b6d82bab7a60c31@185.255.131.17:26656,18c5fbcdbac41024a04665b52cf29541d7cd5caf@135.181.138.160:28856,9755cab2585a2794453a5b396ef13b893393366f@65.108.212.224:46673,ade4d8bc8cbe014af6ebdf3cb7b1e9ad36f412c0@176.9.82.221:17656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.okp4d/config/config.toml
```
