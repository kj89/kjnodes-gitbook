# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/rebus.png" width="150" alt=""><figcaption></figcaption></figure>

Rebuschain is a platform that will provide DeFi (Decentralized Finance)  investment opportunities to traditional investors clearly and conveniently

**Chain ID**: reb_1111-1 | **Latest Version Tag**: v0.2.0 | **Wasm**: OFF

Website: [https://www.rebuschain.com](https://www.rebuschain.com)

## Restake

[Restake with kjnodes](https://restake.app/rebus/rebusvaloper1vndzy8y55ylgpmmsc34uy8rm6kqlml6ffs9lrv) (every day at 08:00, 20:00)
## Public endpoints

* rpc: [https://rebus.rpc.kjnodes.com](https://rebus.rpc.kjnodes.com)
* api: [https://rebus.api.kjnodes.com](https://rebus.api.kjnodes.com)

## Peering

**state-sync**

```
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@rebus.rpc.kjnodes.com:21656
```

**seed-node**

```
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@rebus.rpc.kjnodes.com:21659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/rebus/addrbook.json > $HOME/.rebusd/config/addrbook.json
```

**live-peers** (29)
```
peers="c126eed9cfede7802d78f570fec8175835309a73@141.95.127.146:26656,641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,fa292bfad37826c9da43894b349b1480dff516b5@65.108.99.254:31656,1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,9d17d1c5b5d3b8c9e7ffab264b45b5dd979116f3@65.109.24.188:26656,afdd27b58e851dcbb8c98c0e3191a0d8bfbcd3ae@65.108.41.252:26656,17779ded6b3dc2f31d6c6f40cc6f07d802753ba7@78.47.153.128:26656,aa2feb704c0089b1a0f23011a9e7cd2c27a06134@65.21.200.6:29656,b8137c688096d1abcf56942d335d061f212e6629@62.212.65.138:34656,69e27ab9b46350654805df3ea8d9ac2f00af4e4c@38.242.244.85:26656,f4ad005ee8ec25508c498294e9e83d81b188ea49@185.248.24.16:21656,3a3e7123b9ae814b8d8517b6635d21b9ae45bf25@195.3.222.148:26656,6d8c83cc702365363b829a14efdd414401da369b@23.88.69.167:27565,34e3178b6e0f25451fd690c15fc199d5a9bdfb9b@15.204.197.11:26656,5f4b34cf261bb4f2c14b8a707ed6cdbbee75d500@154.53.60.246:26656,3a378fbfae33a593b913371c876c9d275c0abb12@213.239.215.77:26656,2f6b34ad97c4827dace87436f0299cf89fe0c056@136.243.95.80:46656,eeca453e3a1cf670c78e2255b8f0bd5a9443c30b@65.108.225.71:26656,d3a8fdbe6776fc71998fa893abcd634461b52b19@65.109.92.241:40106,c0b33353fb70d8d71dcb9c8848b3b4207bd56951@188.165.221.155:30547,a35d28e111c1dcc1e5f3203627b449adfb4425f2@65.109.29.150:21656,1f7c31506f465c5f5536862074e98fc7a6043d4c@65.108.13.212:26656,0fedf7695d9e2721663c1d573d6d81a14c21533e@65.21.90.137:12856,5f29f14fe3dd7e1d86caa4d344e67ee81c32255f@65.109.37.228:26656,b8ed7daa4e2966f6c160915600d7dadf7e3ef61e@62.171.142.94:26156,ab6a4ae2857ac05fa8f45b03871fa3945193fc61@46.4.81.204:35656,75c5365e8da9a4caa908a195ffa3fdc1e6432019@65.108.232.248:26756,8f023504e27873141164b6fbf1c4b788ff8d533b@159.69.200.24:26656,3e319c765b7b48d518a2e3218efc317234b81681@142.132.159.188:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.rebusd/config/config.toml
```
