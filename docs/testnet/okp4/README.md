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

**live-peers** (35)
```bash
peers="8cdeb85dada114c959c36bb59ce258c65ae3a09c@88.198.242.163:36656,74349a1cb9479b291866debe2042de8a2e88b850@65.108.233.109:17656,269d246537499d05698c183497c4263e899036a4@65.108.9.164:35656,66a75c374c274733bfa3050277cdb43db3fcee56@147.182.229.52:26656,99f6675049e22a0216af0e2447e7a4c5021874cd@142.132.132.200:28656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:36656,ba469aac96159dbb49844406423180618d267007@65.108.120.21:26113,b0b56d944cf1cc569a1e77e0923e075bad94d755@141.95.145.41:28656,854cc8b83a48ba4394c1940b57d0f42ec013e033@38.242.251.204:26656,cc8bc81fea49a6a412992bb3e2c3f211d9e675c8@88.99.161.162:21656,ebc272824924ea1a27ea3183dd0b9ba713494f83@95.214.55.198:26996,473369a53bfa8a0ac4af5a191407b30bc82e83be@74.208.94.42:14656,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.55.232:26996,d4305fcb7b20dc96481a6ae6ae84f281f3413a4e@65.109.37.58:13656,2c6b5af41689145abb85f95cb49131ae9e193142@217.13.223.167:61356,2bfd405e8f0f176428e2127f98b5ec53164ae1f0@142.132.149.118:26656,09f116943144c71608d98d78c2d89de82855e8a7@65.109.19.173:51656,8a7605d8ae4338de5b7a0d5c70244ce05e377630@85.10.200.221:26656,e1635bec0e5a14dbbf1a41557714632627729ff9@195.201.16.157:36656,034c2fbca12a8ced548d3225bcd21bdf1216a1b3@65.109.49.163:11203,be9841ace1d71a4c7681918ee39f5e00d8e96a82@213.239.216.252:36656,d1a0ff9bd7ea1ebd06bc7158f3523f5e557328be@163.172.131.169:26656,9d1482bc31fb4578a5c7f7f65c4e0aaf2dfc2336@213.239.215.77:36656,307fb25cd6998d0d5bd1d947571f6043c6bb4069@65.109.31.114:2280,95986e08f5baee420d3b72be67826e321663072b@65.109.85.221:6070,a490691c2a423573cb93bc23b13967ed9db0e3ff@146.190.44.218:26656,395848f060440388d4d6d2e8902b9851426c3ec0@51.159.153.211:26656,e20b9048c220d4a8b7e7934fddb3c4fb20c20bdd@81.0.246.196:26656,e676fad27d970abede25b0469676b05ea83e5f04@144.168.47.230:36656,cb6ae22e1e89d029c55f2cb400b0caa19cbe5523@138.197.132.185:26603,f7e481df45bfbe62ea0553f5f6da34eaf4f688c3@194.34.232.225:26656,f17338ec41b1b68b07063984feb407d9038cf78b@65.108.142.47:26616,9755cab2585a2794453a5b396ef13b893393366f@65.108.212.224:46673,5ed1edac2d35c91577b34f6002c85927027058b9@95.217.202.49:30656,2f9e54645aca860f703e3f756fa7c472b829a9a9@195.201.222.82:26009"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.okp4d/config/config.toml
```
