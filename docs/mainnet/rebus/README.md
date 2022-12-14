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
peers="9d17d1c5b5d3b8c9e7ffab264b45b5dd979116f3@65.109.24.188:26656,d28516746773bfaeca4efa5537c0bf5990b8828e@65.21.229.33:27656,4e2a874e538319f204f03751a5e458d0371d5b92@65.108.98.125:60556,235a2754b94c86a85ba645119151ee55d6971554@213.239.216.252:26656,ce38728ac38ebbb4a72d496d42f8e9030af441d7@162.19.137.25:26656,b570827e4397512e077028ea7121d3e19eb25bab@85.10.200.221:26656,17779ded6b3dc2f31d6c6f40cc6f07d802753ba7@78.47.153.128:26656,8f023504e27873141164b6fbf1c4b788ff8d533b@159.69.200.24:26656,ab6a4ae2857ac05fa8f45b03871fa3945193fc61@46.4.81.204:35656,0fedf7695d9e2721663c1d573d6d81a14c21533e@65.21.90.137:12856,34e3178b6e0f25451fd690c15fc199d5a9bdfb9b@15.204.197.11:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,fa292bfad37826c9da43894b349b1480dff516b5@65.108.99.254:31656,3e319c765b7b48d518a2e3218efc317234b81681@142.132.159.188:26656,256d9790bf186f5a275790f7fe01e1b8800dcaaf@65.21.88.78:26656,36afb1c827f52d38d7cd328b384d644b531b5997@65.108.238.102:17256,6d8c83cc702365363b829a14efdd414401da369b@23.88.69.167:27565,c126eed9cfede7802d78f570fec8175835309a73@141.95.127.146:26656,75c5365e8da9a4caa908a195ffa3fdc1e6432019@65.108.232.248:26756,18ec83c4e3938aec31a3a32154969107739f0b81@135.181.153.228:26656,b1b08fe470551dca6d6631fb1bfabb814f6c1aec@54.37.129.164:54556,b8137c688096d1abcf56942d335d061f212e6629@62.212.65.138:34656,1f7c31506f465c5f5536862074e98fc7a6043d4c@65.108.13.212:26656,641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,aa2feb704c0089b1a0f23011a9e7cd2c27a06134@65.21.200.6:29656,12703ce9efe6c1171c193dae2e2041a2be610852@65.108.44.149:29656,4a4d2e7070e05ad6c13628d2f191d96172659452@65.109.65.210:40656,304ff8e051b2fbd038771142b69ac915c14c0819@78.46.78.83:26656,b5bf2242c981371224e5e9e89d6c265d554c8989@65.21.202.154:21656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.rebusd/config/config.toml
```
