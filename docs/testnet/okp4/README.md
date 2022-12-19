# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/okp4.png" width="150" alt=""><figcaption></figcaption></figure>

OKP4 is a revolutionary public blockchain protocol where communities are incentivized to  share data and services confidently. To maximize value from data, it needs to be processed  by complex algorithms and pooled with other datasets, to create valuable knowledge.

**Chain ID**: okp4-nemeton-1 | **Latest Version Tag**: v3.0.0 | **Wasm**: OFF

Website: [https://okp4.network](https://okp4.network)


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

**live-peers** (28)
```
peers="e755eb8016c2f6f5303b2f8d503d9126d235e80f@138.201.35.56:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:36656,42b1ed3a559cbc09278d360dfccf64866a780104@65.109.27.156:29656,8af258bbe73f4c66127a7b3e8b1ec23fde2950a6@65.108.192.123:19656,b2c6835ab2300785ca3bdc0e045d8861504a9ff4@185.194.219.96:26656,9d1482bc31fb4578a5c7f7f65c4e0aaf2dfc2336@213.239.215.77:36656,15fdc722cd49ef7676205b6ad3120a84728d948c@65.108.225.158:17656,b0b56d944cf1cc569a1e77e0923e075bad94d755@141.95.145.41:28656,d1a0ff9bd7ea1ebd06bc7158f3523f5e557328be@163.172.131.169:26656,11d2d5cab53f3e10bc8d91c76601d68cce33c82b@144.76.28.163:26656,854cc8b83a48ba4394c1940b57d0f42ec013e033@38.242.251.204:26656,8a7605d8ae4338de5b7a0d5c70244ce05e377630@85.10.200.221:26656,be9841ace1d71a4c7681918ee39f5e00d8e96a82@213.239.216.252:36656,5ed1edac2d35c91577b34f6002c85927027058b9@95.217.202.49:30656,66dba0e3210d9eb33c067ea17fcfdcef33bf53c7@109.123.254.241:26656,74349a1cb9479b291866debe2042de8a2e88b850@65.108.233.109:17656,8cdeb85dada114c959c36bb59ce258c65ae3a09c@88.198.242.163:36656,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.55.232:26996,1f4fa23210cc1d086a928a3c6de7c24f6c8f17ba@202.61.226.120:16656,2bfd405e8f0f176428e2127f98b5ec53164ae1f0@142.132.149.118:26656,307fb25cd6998d0d5bd1d947571f6043c6bb4069@65.109.31.114:2280,30092d2717053f1c0813e8354c07c761c9c3ac5c@194.163.161.234:26656,8028015d1c6828a0b734f3b108f0853b0e19305e@157.90.176.184:26656,d4305fcb7b20dc96481a6ae6ae84f281f3413a4e@65.109.37.58:13656,f7e481df45bfbe62ea0553f5f6da34eaf4f688c3@194.34.232.225:26656,fff0a8c202befd9459ff93783a0e7756da305fe3@38.242.150.63:16656,d132ad0c5b2afd0eab2d87351eeda46dc9d69312@46.228.205.200:26656,cd2e7d49cc2f911d7df7c7951d72c96727d1db1d@212.8.240.13:36656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.okp4d/config/config.toml
```
