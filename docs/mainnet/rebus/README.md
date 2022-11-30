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

**live-peers** (30)
```
peers="12e6bea6650a53150c01ca3897e4a0b94d6e9d4e@135.181.141.47:26656,9d17d1c5b5d3b8c9e7ffab264b45b5dd979116f3@65.109.24.188:26656,6ad5dd14c578016cc7bc4d7c6d6f7f773bba39af@65.109.60.57:26656,ff7031f45a97600076f72b9318167e3dfcd2a17e@65.21.136.170:52656,4a4d2e7070e05ad6c13628d2f191d96172659452@65.109.65.210:40656,c126eed9cfede7802d78f570fec8175835309a73@141.95.127.146:26656,e056318da91e77585f496333040e00e12f6941d1@51.83.97.166:26656,3cc5fb5f6140ac4e57dfc80940c8a06daa299c89@51.77.195.46:26656,b570827e4397512e077028ea7121d3e19eb25bab@85.10.200.221:26656,69e27ab9b46350654805df3ea8d9ac2f00af4e4c@38.242.244.85:26656,170397e75ca2b0f4e9f3b1bb5d0d23f9b10f01c7@94.23.23.189:30544,ce38728ac38ebbb4a72d496d42f8e9030af441d7@162.19.137.25:26656,eeca453e3a1cf670c78e2255b8f0bd5a9443c30b@65.108.225.71:26656,6d8c83cc702365363b829a14efdd414401da369b@23.88.69.167:27565,77ca73199cf0a73ab52fc216d8ab8f8756275fef@138.201.8.248:52656,f97a11f283cd5f11bf1fe73d8b2012b711d61ce9@38.242.205.80:21656,6daeb8cfea285f561e167a0d94718b61e2cf7944@5.189.187.36:21656,3a3e7123b9ae814b8d8517b6635d21b9ae45bf25@195.3.222.148:26656,d6c891779edb84d91aa7dd043dcc819c11bf6895@185.245.183.106:26656,aa2feb704c0089b1a0f23011a9e7cd2c27a06134@65.21.200.6:29656,75c5365e8da9a4caa908a195ffa3fdc1e6432019@65.108.232.248:26756,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,1f7c31506f465c5f5536862074e98fc7a6043d4c@65.108.13.212:26656,a3d975c913570ad217d9a3de01a8616ad5ce20f8@142.132.128.137:26656,056d6a61c8a4c5ccb02123d67a013434423f155a@149.102.142.57:26656,5c2018214fcfde67ec390702539f295165f12a3a@86.48.2.20:26656,1749a8f0aa533fc92c1212366c22c0993fbb1545@51.178.47.116:26656,f2483e5af4cb1fab55e4f6422627c0365f45b5dd@194.163.188.252:26656,b8137c688096d1abcf56942d335d061f212e6629@62.212.65.138:34656,b1dcbb37514fbe215be54079e71aa39dac7fd0ae@64.5.123.203:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.rebusd/config/config.toml
```
