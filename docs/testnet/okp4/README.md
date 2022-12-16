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

**live-peers** (19)
```
peers="8028015d1c6828a0b734f3b108f0853b0e19305e@157.90.176.184:26656,d132ad0c5b2afd0eab2d87351eeda46dc9d69312@46.228.205.200:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:36656,74349a1cb9479b291866debe2042de8a2e88b850@65.108.233.109:17656,8af258bbe73f4c66127a7b3e8b1ec23fde2950a6@65.108.192.123:19656,cd2e7d49cc2f911d7df7c7951d72c96727d1db1d@212.8.240.13:36656,e755eb8016c2f6f5303b2f8d503d9126d235e80f@138.201.35.56:26656,23e895e7d650f43e1f53522165607b71685f8cfa@65.108.75.107:26656,2bfd405e8f0f176428e2127f98b5ec53164ae1f0@142.132.149.118:26656,b0b56d944cf1cc569a1e77e0923e075bad94d755@141.95.145.41:28656,1f4fa23210cc1d086a928a3c6de7c24f6c8f17ba@202.61.226.120:16656,8cdeb85dada114c959c36bb59ce258c65ae3a09c@88.198.242.163:36656,d1a0ff9bd7ea1ebd06bc7158f3523f5e557328be@163.172.131.169:26656,8a7605d8ae4338de5b7a0d5c70244ce05e377630@85.10.200.221:26656,307fb25cd6998d0d5bd1d947571f6043c6bb4069@65.109.31.114:2280,9d1482bc31fb4578a5c7f7f65c4e0aaf2dfc2336@213.239.215.77:36656,5ed1edac2d35c91577b34f6002c85927027058b9@95.217.202.49:30656,30092d2717053f1c0813e8354c07c761c9c3ac5c@194.163.161.234:26656,fff0a8c202befd9459ff93783a0e7756da305fe3@38.242.150.63:16656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.okp4d/config/config.toml
```
