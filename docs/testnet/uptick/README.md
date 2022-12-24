# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/uptick.png" width="150" alt=""><figcaption></figcaption></figure>

The Business Grade Multi-Chain NFT Infrastructure for Web 3.0

**Chain ID**: uptick_7000-2 | **Latest Version Tag**: v0.2.4 | **Wasm**: OFF

[Website](https://uptick.network) | [Discord](https://discord.gg/UzeHS7fu5H) | [Twitter](https://twitter.com/uptickproject)


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

**live-peers** (16)
```
peers="883d6557bef1bae68c4fb569078caf0cf4c45bdd@142.132.202.50:26651,f06b6a57001440bf3507ba2f09a3010f6d50080b@135.181.133.37:29656,d8777278648d8fc93800692a8b96a7f104df4f9a@194.163.135.127:26656,2d892493335b4bb1582dabcaa1e832bcba041e79@95.217.4.62:26656,7a4f1c0baa2ff31c02163fb658c4eb8d119193c7@95.214.52.173:26656,821cec653e1bdcd6e0ea7db62ddc65e7dae9fc5b@190.2.136.58:26656,5368bc0c12a7bfd9d69ba192b06f2be97d28e7ef@185.239.209.56:31656,12fe5ed38770b4bb59c59e183ec1161aebda2a4e@185.173.38.18:26656,70c19420bb2d40c5a6c3466c69ead6e0877b9cc7@45.85.250.108:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15656,94b63fddfc78230f51aeb7ac34b9fb86bd042a77@94.23.207.45:30556,2763c95b0c9b0b31c312b06d6ae6887968fb9830@194.163.154.224:26656,b9d3fe835ded0b93c39befad43fb3c4964ae740f@91.195.101.100:26656,b483acbcae7ccd1244f588144245e9d1124c3de5@88.99.56.200:26666,50e92c60d1b8c6681044778d74caaeef51a26ddd@94.130.207.215:15656,eb5a3112a64944e2bd701ff8aa99ab95209c6310@185.198.27.110:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.uptickd/config/config.toml
```
