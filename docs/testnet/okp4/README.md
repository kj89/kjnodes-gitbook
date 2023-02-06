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

**live-peers** (39)
```bash
peers="cf5e82486c4568c29a20719a68210523826ceb00@65.108.229.102:26651,1655cdc8fdfe1dc2209d47ff68c02a417ef9ed52@135.181.222.179:31656,540e0e9b33b2d87315fdf7089404671581d36e94@95.217.203.43:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:36656,99f6675049e22a0216af0e2447e7a4c5021874cd@142.132.132.200:28656,269d246537499d05698c183497c4263e899036a4@65.108.9.164:35656,ba469aac96159dbb49844406423180618d267007@65.108.120.21:26113,2bfd405e8f0f176428e2127f98b5ec53164ae1f0@142.132.149.118:26656,7dfc61d3ac9f6da7fa9f4893bc0ffa17ef8006e6@185.111.159.139:36656,2c6b5af41689145abb85f95cb49131ae9e193142@217.13.223.167:61356,8cdeb85dada114c959c36bb59ce258c65ae3a09c@88.198.242.163:36656,b0b56d944cf1cc569a1e77e0923e075bad94d755@141.95.145.41:28656,8577873589dc7ecb9f2e32f79fe51ef7f57e40a3@65.109.161.143:26656,f17338ec41b1b68b07063984feb407d9038cf78b@65.108.142.47:26616,d4305fcb7b20dc96481a6ae6ae84f281f3413a4e@65.109.37.58:13656,473369a53bfa8a0ac4af5a191407b30bc82e83be@74.208.94.42:14656,8af258bbe73f4c66127a7b3e8b1ec23fde2950a6@65.108.192.123:19656,9d1482bc31fb4578a5c7f7f65c4e0aaf2dfc2336@213.239.215.77:36656,eef77b5ae1c37f3e5809ff928c329dde906be388@65.108.133.73:21656,ffbd1adeb58928c3f400fab23c84c3c73badd7fa@65.108.226.44:29656,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.55.232:26996,26114bc5cb42ef90be2aba5b4b6d82bab7a60c31@185.255.131.17:26656,9a1e456bebf152b65c2087896779e259633ecbef@157.90.34.111:26656,a06417f8518fbf6f779e4012dbf72f194a95b48f@65.21.138.124:33656,42fbb917fca6787bc3ab774865f4bb1ef950f114@65.108.226.26:30656,be9841ace1d71a4c7681918ee39f5e00d8e96a82@213.239.216.252:36656,874373b78d2cd50e716aa464bf407581d9305655@94.250.201.130:27656,854cc8b83a48ba4394c1940b57d0f42ec013e033@38.242.251.204:26656,a490691c2a423573cb93bc23b13967ed9db0e3ff@146.190.44.218:26656,307fb25cd6998d0d5bd1d947571f6043c6bb4069@65.109.31.114:2280,b5e97c26a21f7ac60b4c54bb7bae84fe454135e0@194.233.68.136:26656,30092d2717053f1c0813e8354c07c761c9c3ac5c@194.163.161.234:26656,fe8bd9375c43a7cc6ef27e62d56af341a62e67c9@95.217.202.49:30656,d1a0ff9bd7ea1ebd06bc7158f3523f5e557328be@163.172.131.169:26656,052e10ce23cce3249f61853e2ca6a63102b7bddb@5.161.97.198:26656,74349a1cb9479b291866debe2042de8a2e88b850@65.108.233.109:17656,ebc272824924ea1a27ea3183dd0b9ba713494f83@95.214.55.198:26996,8a7605d8ae4338de5b7a0d5c70244ce05e377630@85.10.200.221:26656,9755cab2585a2794453a5b396ef13b893393366f@65.108.212.224:46673"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.okp4d/config/config.toml
```
