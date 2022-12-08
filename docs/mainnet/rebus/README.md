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
peers="1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,9d17d1c5b5d3b8c9e7ffab264b45b5dd979116f3@65.109.24.188:26656,256d9790bf186f5a275790f7fe01e1b8800dcaaf@65.21.88.78:26656,a35d28e111c1dcc1e5f3203627b449adfb4425f2@65.109.29.150:21656,fa292bfad37826c9da43894b349b1480dff516b5@65.108.99.254:31656,eeca453e3a1cf670c78e2255b8f0bd5a9443c30b@65.108.225.71:26656,c126eed9cfede7802d78f570fec8175835309a73@141.95.127.146:26656,b570827e4397512e077028ea7121d3e19eb25bab@85.10.200.221:26656,404ae118865c1485f7859fa2c7cc2e3b8c402a14@51.75.135.34:26656,a3d975c913570ad217d9a3de01a8616ad5ce20f8@142.132.128.137:26656,34e3178b6e0f25451fd690c15fc199d5a9bdfb9b@15.204.197.11:26656,2f6b34ad97c4827dace87436f0299cf89fe0c056@136.243.95.80:46656,ab6a4ae2857ac05fa8f45b03871fa3945193fc61@46.4.81.204:35656,6d8c83cc702365363b829a14efdd414401da369b@23.88.69.167:27565,0fedf7695d9e2721663c1d573d6d81a14c21533e@65.21.90.137:12856,40e2c0b68a1dd48466714e3dd0581e4b7d498575@107.155.122.93:26656,3a3e7123b9ae814b8d8517b6635d21b9ae45bf25@195.3.222.148:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,5c2018214fcfde67ec390702539f295165f12a3a@86.48.2.20:26656,75c5365e8da9a4caa908a195ffa3fdc1e6432019@65.108.232.248:26756,f467e286567f94c89d39a5bcea0e1d68951299f9@146.59.81.204:34456,f4ad005ee8ec25508c498294e9e83d81b188ea49@185.248.24.16:21656,4a4d2e7070e05ad6c13628d2f191d96172659452@65.109.65.210:40656,b8ed7daa4e2966f6c160915600d7dadf7e3ef61e@62.171.142.94:26156,c0b33353fb70d8d71dcb9c8848b3b4207bd56951@188.165.221.155:30547,12703ce9efe6c1171c193dae2e2041a2be610852@65.108.44.149:29656,235a2754b94c86a85ba645119151ee55d6971554@213.239.216.252:26656,dda7abe32cc84a722cf6b1d2ee3b61ebe7ad71df@135.181.212.183:21656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.rebusd/config/config.toml
```
