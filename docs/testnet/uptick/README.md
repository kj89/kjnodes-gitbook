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

**live-peers** (12)
```
peers="20aaf646f9c766a8b81d838554ba6e593122ed1f@46.4.122.236:36656,0aee682fb3453170737149203e5c23d2e0c46058@142.132.253.112:15656,2763c95b0c9b0b31c312b06d6ae6887968fb9830@194.163.154.224:26656,94b63fddfc78230f51aeb7ac34b9fb86bd042a77@94.23.207.45:30556,d6aad702ecfed6c5e76e2f25dea6b921c3cd7857@154.12.242.252:31656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15656,b9d3fe835ded0b93c39befad43fb3c4964ae740f@91.195.101.100:26656,3666c65e99775b8149396fd5c781dec6a29fb13b@75.119.144.48:31656,7849e4320385434b0828a3e0206a3b69767393f6@65.109.91.227:26656,f06b6a57001440bf3507ba2f09a3010f6d50080b@135.181.133.37:29656,75aa14851ff12bd4825fe5679958dc278086e2b9@95.216.14.72:34656,5368bc0c12a7bfd9d69ba192b06f2be97d28e7ef@185.239.209.56:31656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.uptickd/config/config.toml
```
