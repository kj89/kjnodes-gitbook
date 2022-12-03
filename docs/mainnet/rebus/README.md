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

**live-peers** (28)
```
peers="3e319c765b7b48d518a2e3218efc317234b81681@142.132.159.188:26656,9d17d1c5b5d3b8c9e7ffab264b45b5dd979116f3@65.109.24.188:26656,304ff8e051b2fbd038771142b69ac915c14c0819@78.46.78.83:26656,a35d28e111c1dcc1e5f3203627b449adfb4425f2@65.109.29.150:21656,6ad5dd14c578016cc7bc4d7c6d6f7f773bba39af@65.109.60.57:26656,e056318da91e77585f496333040e00e12f6941d1@51.83.97.166:26656,ea5e7a6b9a5c18c6455e7a8c583c129c5821a452@51.178.80.111:26656,7ee74ea68e350fc5214657255cba5e339bb30c2a@138.201.127.91:26674,6d8c83cc702365363b829a14efdd414401da369b@23.88.69.167:27565,bb2a7dc81b9bd0e017409a2bbb71b12bb899e743@178.63.22.117:26656,ab6a4ae2857ac05fa8f45b03871fa3945193fc61@46.4.81.204:35656,77ca73199cf0a73ab52fc216d8ab8f8756275fef@138.201.8.248:52656,5c2018214fcfde67ec390702539f295165f12a3a@86.48.2.20:26656,1fe32d8f09b8715b1e626da17b3ecfe26623b371@176.9.22.117:27656,3a3e7123b9ae814b8d8517b6635d21b9ae45bf25@195.3.222.148:26656,aa2feb704c0089b1a0f23011a9e7cd2c27a06134@65.21.200.6:29656,1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,2f6b34ad97c4827dace87436f0299cf89fe0c056@136.243.95.80:46656,1749a8f0aa533fc92c1212366c22c0993fbb1545@51.178.47.116:26656,89ded0a3987d22e46b756fead439e2a4d25f23cb@185.144.99.30:26656,056d6a61c8a4c5ccb02123d67a013434423f155a@149.102.142.57:26656,b1b08fe470551dca6d6631fb1bfabb814f6c1aec@54.37.129.164:54556,b8ed7daa4e2966f6c160915600d7dadf7e3ef61e@62.171.142.94:26156,d6c891779edb84d91aa7dd043dcc819c11bf6895@185.245.183.106:26656,69e27ab9b46350654805df3ea8d9ac2f00af4e4c@38.242.244.85:26656,f97a11f283cd5f11bf1fe73d8b2012b711d61ce9@38.242.205.80:21656,75c5365e8da9a4caa908a195ffa3fdc1e6432019@65.108.232.248:26756"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.rebusd/config/config.toml
```
