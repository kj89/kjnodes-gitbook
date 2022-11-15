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
peers="dda7abe32cc84a722cf6b1d2ee3b61ebe7ad71df@135.181.212.183:21656,408206e3aab058d1dc09697566e3dadfaa3760ea@135.181.5.47:20106,aa2feb704c0089b1a0f23011a9e7cd2c27a06134@65.21.200.6:29656,b5bf2242c981371224e5e9e89d6c265d554c8989@65.21.202.154:21656,30ff8100fefac53ee40ef7631f1a3c66ca2b82cf@135.181.164.90:26656,75c5365e8da9a4caa908a195ffa3fdc1e6432019@65.108.232.248:26756,9d17d1c5b5d3b8c9e7ffab264b45b5dd979116f3@65.109.24.188:26656,a155d381099de93e7efe00f9475786abffd29c3e@167.235.29.125:26637,a3d975c913570ad217d9a3de01a8616ad5ce20f8@142.132.128.137:26656,69e27ab9b46350654805df3ea8d9ac2f00af4e4c@38.242.244.85:26656,304ff8e051b2fbd038771142b69ac915c14c0819@78.46.78.83:26656,bb2a7dc81b9bd0e017409a2bbb71b12bb899e743@178.63.22.117:26656,17779ded6b3dc2f31d6c6f40cc6f07d802753ba7@78.47.153.128:26656,d6c891779edb84d91aa7dd043dcc819c11bf6895@185.245.183.106:26656,b1b08fe470551dca6d6631fb1bfabb814f6c1aec@54.37.129.164:54556,77ca73199cf0a73ab52fc216d8ab8f8756275fef@138.201.8.248:52656,3a3e7123b9ae814b8d8517b6635d21b9ae45bf25@195.3.222.148:26656,e056318da91e77585f496333040e00e12f6941d1@51.83.97.166:26656,6ad5dd14c578016cc7bc4d7c6d6f7f773bba39af@65.109.60.57:26656,3fc3b7e3073cc0d59fef9390cad15601d7109dd0@65.108.193.11:26656,ff7031f45a97600076f72b9318167e3dfcd2a17e@65.21.136.170:52656,7ee74ea68e350fc5214657255cba5e339bb30c2a@138.201.127.91:26674,c177f05fc7c0379e26eff108048c0bfd96949b2c@141.95.65.73:17256,f4ad005ee8ec25508c498294e9e83d81b188ea49@185.248.24.16:21656,3cc5fb5f6140ac4e57dfc80940c8a06daa299c89@51.77.195.46:26656,b8137c688096d1abcf56942d335d061f212e6629@62.212.65.138:34656,ff2657d49f9f50412987a66785e928d7ec9c2f99@88.208.57.200:36656,eeca453e3a1cf670c78e2255b8f0bd5a9443c30b@65.108.225.71:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:21656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.rebusd/config/config.toml
```
