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
peers="346bf012c17fa30ef70ae72f082374838626532a@65.108.106.131:26696,fa292bfad37826c9da43894b349b1480dff516b5@65.108.99.254:31656,641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,256d9790bf186f5a275790f7fe01e1b8800dcaaf@65.21.88.78:26656,aa2feb704c0089b1a0f23011a9e7cd2c27a06134@65.21.200.6:29656,75c5365e8da9a4caa908a195ffa3fdc1e6432019@65.108.232.248:26756,30ff8100fefac53ee40ef7631f1a3c66ca2b82cf@135.181.164.90:26656,4e2a874e538319f204f03751a5e458d0371d5b92@65.108.98.125:60556,a35d28e111c1dcc1e5f3203627b449adfb4425f2@65.109.29.150:21656,c126eed9cfede7802d78f570fec8175835309a73@141.95.127.146:26656,ab6a4ae2857ac05fa8f45b03871fa3945193fc61@46.4.81.204:35656,85fbeb61beb838ecf2059411b62ef04be6275596@138.201.132.55:26656,b8137c688096d1abcf56942d335d061f212e6629@62.212.65.138:34656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:21656,304ff8e051b2fbd038771142b69ac915c14c0819@78.46.78.83:26656,ad613c7b9c6bb978edd86ae1116cf4c0e0b45c22@92.205.61.172:28656,b1b08fe470551dca6d6631fb1bfabb814f6c1aec@54.37.129.164:54556,e056318da91e77585f496333040e00e12f6941d1@51.83.97.166:26656,34e3178b6e0f25451fd690c15fc199d5a9bdfb9b@15.204.197.11:26656,8f023504e27873141164b6fbf1c4b788ff8d533b@159.69.200.24:26656,5f4b34cf261bb4f2c14b8a707ed6cdbbee75d500@154.53.60.246:26656,186209f02d238b48dcc7997cca3e6c6855aa91aa@20.112.73.169:26656,b570827e4397512e077028ea7121d3e19eb25bab@85.10.200.221:26656,3fc3b7e3073cc0d59fef9390cad15601d7109dd0@65.108.193.11:26656,036c453576f9f4cad684e78d09e0fbf876e9cdee@54.39.243.226:22656,408206e3aab058d1dc09697566e3dadfaa3760ea@135.181.5.47:20106,a3d975c913570ad217d9a3de01a8616ad5ce20f8@142.132.128.137:26656,f467e286567f94c89d39a5bcea0e1d68951299f9@146.59.81.204:34456"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.rebusd/config/config.toml
```
