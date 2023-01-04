# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/okp4.png" width="150" alt=""><figcaption></figcaption></figure>

OKP4 is a revolutionary public blockchain protocol where communities are incentivized to  share data and services confidently. To maximize value from data, it needs to be processed  by complex algorithms and pooled with other datasets, to create valuable knowledge.

**Chain ID**: okp4-nemeton-1 | **Latest Version Tag**: v3.0.0 | **Wasm**: OFF

[Website](https://okp4.network) | [Discord](https://discord.gg/okp4) | [Twitter](https://twitter.com/OKP4_Protocol)


## Public endpoints

* rpc: [https://okp4-testnet.rpc.kjnodes.com](https://okp4-testnet.rpc.kjnodes.com)
* api: [https://okp4-testnet.api.kjnodes.com](https://okp4-testnet.api.kjnodes.com)

## Peering

**state-sync**

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@okp4-testnet.rpc.kjnodes.com:36656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@okp4-testnet.rpc.kjnodes.com:36659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/okp4-testnet/addrbook.json > $HOME/.okp4d/config/addrbook.json
```

**live-peers** (27)
```
peers="11d2d5cab53f3e10bc8d91c76601d68cce33c82b@144.76.28.163:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:36656,6bc178290d0773e244cf04598a3919d7a9391bf1@65.109.131.71:36656,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.55.232:26996,cd2e7d49cc2f911d7df7c7951d72c96727d1db1d@212.8.240.13:36656,b2c6835ab2300785ca3bdc0e045d8861504a9ff4@185.194.219.96:26656,8cdeb85dada114c959c36bb59ce258c65ae3a09c@88.198.242.163:36656,b0b56d944cf1cc569a1e77e0923e075bad94d755@141.95.145.41:28656,d132ad0c5b2afd0eab2d87351eeda46dc9d69312@46.228.205.200:26656,854cc8b83a48ba4394c1940b57d0f42ec013e033@38.242.251.204:26656,8a7605d8ae4338de5b7a0d5c70244ce05e377630@85.10.200.221:26656,66a75c374c274733bfa3050277cdb43db3fcee56@147.182.229.52:26656,23e895e7d650f43e1f53522165607b71685f8cfa@65.108.75.107:26656,74349a1cb9479b291866debe2042de8a2e88b850@65.108.233.109:17656,2f6d5a319ebee0201dff4a0e3b7526d0863a4d32@65.109.85.225:6070,2bfd405e8f0f176428e2127f98b5ec53164ae1f0@142.132.149.118:26656,d1a0ff9bd7ea1ebd06bc7158f3523f5e557328be@163.172.131.169:26656,9d1482bc31fb4578a5c7f7f65c4e0aaf2dfc2336@213.239.215.77:36656,307fb25cd6998d0d5bd1d947571f6043c6bb4069@65.109.31.114:2280,e755eb8016c2f6f5303b2f8d503d9126d235e80f@138.201.35.56:26656,f7e481df45bfbe62ea0553f5f6da34eaf4f688c3@194.34.232.225:26656,30092d2717053f1c0813e8354c07c761c9c3ac5c@194.163.161.234:26656,be9841ace1d71a4c7681918ee39f5e00d8e96a82@213.239.216.252:36656,fa04503a35476204861f06b75be4839562205527@65.109.85.226:6070,540e0e9b33b2d87315fdf7089404671581d36e94@95.217.203.43:26656,42b1ed3a559cbc09278d360dfccf64866a780104@65.109.27.156:29656,2f9e54645aca860f703e3f756fa7c472b829a9a9@195.201.222.82:26009"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.okp4d/config/config.toml
```
