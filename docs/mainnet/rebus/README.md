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
peers="fa292bfad37826c9da43894b349b1480dff516b5@65.108.99.254:31656,4e2a874e538319f204f03751a5e458d0371d5b92@65.108.98.125:60556,9d17d1c5b5d3b8c9e7ffab264b45b5dd979116f3@65.109.24.188:26656,aa2feb704c0089b1a0f23011a9e7cd2c27a06134@65.21.200.6:29656,c177f05fc7c0379e26eff108048c0bfd96949b2c@141.95.65.73:17256,404ae118865c1485f7859fa2c7cc2e3b8c402a14@51.75.135.34:26656,6d8c83cc702365363b829a14efdd414401da369b@23.88.69.167:27565,ab6a4ae2857ac05fa8f45b03871fa3945193fc61@46.4.81.204:35656,b570827e4397512e077028ea7121d3e19eb25bab@85.10.200.221:26656,b8137c688096d1abcf56942d335d061f212e6629@62.212.65.138:34656,5c2018214fcfde67ec390702539f295165f12a3a@86.48.2.20:26656,b1b08fe470551dca6d6631fb1bfabb814f6c1aec@54.37.129.164:54556,69e27ab9b46350654805df3ea8d9ac2f00af4e4c@38.242.244.85:26656,3a3e7123b9ae814b8d8517b6635d21b9ae45bf25@195.3.222.148:26656,18ec83c4e3938aec31a3a32154969107739f0b81@135.181.153.228:26656,34e3178b6e0f25451fd690c15fc199d5a9bdfb9b@15.204.197.11:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,b8ed7daa4e2966f6c160915600d7dadf7e3ef61e@62.171.142.94:26156,e056318da91e77585f496333040e00e12f6941d1@51.83.97.166:26656,c0b33353fb70d8d71dcb9c8848b3b4207bd56951@188.165.221.155:30547,b1dcbb37514fbe215be54079e71aa39dac7fd0ae@64.5.123.203:26656,12e6bea6650a53150c01ca3897e4a0b94d6e9d4e@135.181.141.47:26656,6ad5dd14c578016cc7bc4d7c6d6f7f773bba39af@65.109.60.57:26656,641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,a35d28e111c1dcc1e5f3203627b449adfb4425f2@65.109.29.150:21656,346bf012c17fa30ef70ae72f082374838626532a@65.108.106.131:26696,f2483e5af4cb1fab55e4f6422627c0365f45b5dd@194.163.188.252:26656,dda7abe32cc84a722cf6b1d2ee3b61ebe7ad71df@135.181.212.183:21656,3a378fbfae33a593b913371c876c9d275c0abb12@213.239.215.77:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.rebusd/config/config.toml
```
