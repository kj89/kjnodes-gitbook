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
peers="3e319c765b7b48d518a2e3218efc317234b81681@142.132.159.188:26656,eeca453e3a1cf670c78e2255b8f0bd5a9443c30b@65.108.225.71:26656,ff7031f45a97600076f72b9318167e3dfcd2a17e@65.21.136.170:52656,75c5365e8da9a4caa908a195ffa3fdc1e6432019@65.108.232.248:26756,30ff8100fefac53ee40ef7631f1a3c66ca2b82cf@135.181.164.90:26656,aa2feb704c0089b1a0f23011a9e7cd2c27a06134@65.21.200.6:29656,304ff8e051b2fbd038771142b69ac915c14c0819@78.46.78.83:26656,ce38728ac38ebbb4a72d496d42f8e9030af441d7@162.19.137.25:26656,ab6a4ae2857ac05fa8f45b03871fa3945193fc61@46.4.81.204:35656,346bf012c17fa30ef70ae72f082374838626532a@65.108.106.131:26696,a3d975c913570ad217d9a3de01a8616ad5ce20f8@142.132.128.137:26656,f97a11f283cd5f11bf1fe73d8b2012b711d61ce9@38.242.205.80:21656,d6c891779edb84d91aa7dd043dcc819c11bf6895@185.245.183.106:26656,f4ad005ee8ec25508c498294e9e83d81b188ea49@185.248.24.16:21656,ad613c7b9c6bb978edd86ae1116cf4c0e0b45c22@92.205.61.172:28656,237bfc05da5f8cabee00f148995333f37186d232@164.68.121.101:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:21656,c0b33353fb70d8d71dcb9c8848b3b4207bd56951@188.165.221.155:30547,170397e75ca2b0f4e9f3b1bb5d0d23f9b10f01c7@94.23.23.189:30544,f968f06c0f9c08cf7c9ccaf933cc903023ebcc24@194.163.167.122:26656,e04e8466071f8f00defce1d45c27ca6118bac358@135.125.4.73:54556,f467e286567f94c89d39a5bcea0e1d68951299f9@146.59.81.204:34456,256d9790bf186f5a275790f7fe01e1b8800dcaaf@65.21.88.78:26656,5c2018214fcfde67ec390702539f295165f12a3a@86.48.2.20:26656,fa292bfad37826c9da43894b349b1480dff516b5@65.108.99.254:31656,3a3e7123b9ae814b8d8517b6635d21b9ae45bf25@195.3.222.148:26656,b570827e4397512e077028ea7121d3e19eb25bab@85.10.200.221:26656,2f6b34ad97c4827dace87436f0299cf89fe0c056@136.243.95.80:46656,404ae118865c1485f7859fa2c7cc2e3b8c402a14@51.75.135.34:26656,056d6a61c8a4c5ccb02123d67a013434423f155a@149.102.142.57:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.rebusd/config/config.toml
```
