# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/uptick.png" width="150" alt=""><figcaption></figcaption></figure>

The Business Grade Multi-Chain NFT Infrastructure for Web 3.0

**Chain ID**: uptick_7000-2 | **Latest Version Tag**: v0.2.4 | **Wasm**: OFF

Website: [https://uptick.network](https://uptick.network)


## Public endpoints

* rpc: [https://uptick-testnet.rpc.kjnodes.com](https://uptick-testnet.rpc.kjnodes.com)
* api: [https://uptick-testnet.api.kjnodes.com](https://uptick-testnet.api.kjnodes.com)

## Peering

**state-sync**

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@uptick-testnet.rpc.kjnodes.com:15656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@uptick-testnet.rpc.kjnodes.com:15659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/uptick-testnet/addrbook.json > $HOME/.uptickd/config/addrbook.json
```

**live-peers** (17)
```
peers="962d620d21ce5caba3e765501dd9b309cfac234f@78.31.64.11:26356,d6aad702ecfed6c5e76e2f25dea6b921c3cd7857@154.12.242.252:31656,d8777278648d8fc93800692a8b96a7f104df4f9a@194.163.135.127:26656,75aa14851ff12bd4825fe5679958dc278086e2b9@95.216.14.72:34656,0afb5ce897e69eec34fb32bf87f4a2f93f79e0b3@65.109.65.210:30656,2763c95b0c9b0b31c312b06d6ae6887968fb9830@194.163.154.224:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15656,0fcdc6af694d5b9995340549e5ce444dc96de3e0@195.201.197.4:15656,7a4f1c0baa2ff31c02163fb658c4eb8d119193c7@95.214.52.173:26656,883d6557bef1bae68c4fb569078caf0cf4c45bdd@142.132.202.50:26651,af5262526a0800a29a0a7194e1488a9fa62d0005@195.3.223.208:26656,94b63fddfc78230f51aeb7ac34b9fb86bd042a77@94.23.207.45:30556,eb5a3112a64944e2bd701ff8aa99ab95209c6310@185.198.27.110:26656,2298edffe9306e4d9370233c1d29dab567829095@144.91.78.28:26656,f06b6a57001440bf3507ba2f09a3010f6d50080b@135.181.133.37:29656,5368bc0c12a7bfd9d69ba192b06f2be97d28e7ef@185.239.209.56:31656,70c19420bb2d40c5a6c3466c69ead6e0877b9cc7@45.85.250.108:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.uptickd/config/config.toml
```
