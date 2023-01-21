# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/okp4.png" width="150" alt=""><figcaption></figcaption></figure>

OKP4 is a revolutionary public blockchain protocol where communities are incentivized to  share data and services confidently. To maximize value from data, it needs to be processed  by complex algorithms and pooled with other datasets, to create valuable knowledge.

**Chain ID**: okp4-nemeton-1 | **Latest Version Tag**: v3.0.0 | **Wasm**: OFF

[Website](https://okp4.network) | [Discord](https://discord.gg/okp4) | [Twitter](https://twitter.com/OKP4_Protocol)


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

**live-peers** (33)
```bash
peers="cc8bc81fea49a6a412992bb3e2c3f211d9e675c8@88.99.161.162:21656,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.55.232:26996,ebc272824924ea1a27ea3183dd0b9ba713494f83@95.214.55.198:26996,269d246537499d05698c183497c4263e899036a4@65.108.9.164:35656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:36656,99f6675049e22a0216af0e2447e7a4c5021874cd@142.132.132.200:28656,ba469aac96159dbb49844406423180618d267007@65.108.120.21:26113,8cdeb85dada114c959c36bb59ce258c65ae3a09c@88.198.242.163:36656,b0b56d944cf1cc569a1e77e0923e075bad94d755@141.95.145.41:28656,0a961bdf4e0c23a2984d67f8d7bf7cfa85daa4e5@135.181.158.205:26656,854cc8b83a48ba4394c1940b57d0f42ec013e033@38.242.251.204:26656,84eaaf4a1149f1925afe7027eef64f2560ada09b@75.119.159.226:36656,be9841ace1d71a4c7681918ee39f5e00d8e96a82@213.239.216.252:36656,034c2fbca12a8ced548d3225bcd21bdf1216a1b3@65.109.49.163:11203,d1a0ff9bd7ea1ebd06bc7158f3523f5e557328be@163.172.131.169:26656,2bfd405e8f0f176428e2127f98b5ec53164ae1f0@142.132.149.118:26656,8a7605d8ae4338de5b7a0d5c70244ce05e377630@85.10.200.221:26656,f17338ec41b1b68b07063984feb407d9038cf78b@65.108.142.47:26616,473369a53bfa8a0ac4af5a191407b30bc82e83be@74.208.94.42:14656,2c6b5af41689145abb85f95cb49131ae9e193142@217.13.223.167:61356,f7e481df45bfbe62ea0553f5f6da34eaf4f688c3@194.34.232.225:26656,fa04503a35476204861f06b75be4839562205527@65.109.85.226:6070,74349a1cb9479b291866debe2042de8a2e88b850@65.108.233.109:17656,66a75c374c274733bfa3050277cdb43db3fcee56@147.182.229.52:26656,307fb25cd6998d0d5bd1d947571f6043c6bb4069@65.109.31.114:2280,d132ad0c5b2afd0eab2d87351eeda46dc9d69312@46.228.205.200:26656,9d1482bc31fb4578a5c7f7f65c4e0aaf2dfc2336@213.239.215.77:36656,a490691c2a423573cb93bc23b13967ed9db0e3ff@146.190.44.218:26656,c7c9c41bb9fc578c5698a427691eae259a7c81b8@51.159.153.211:36656,d4305fcb7b20dc96481a6ae6ae84f281f3413a4e@65.109.37.58:13656,11d2d5cab53f3e10bc8d91c76601d68cce33c82b@144.76.28.163:26656,5ed1edac2d35c91577b34f6002c85927027058b9@95.217.202.49:30656,9755cab2585a2794453a5b396ef13b893393366f@65.108.212.224:46673"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.okp4d/config/config.toml
```
