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
peers="75c5365e8da9a4caa908a195ffa3fdc1e6432019@65.108.232.248:26756,b5bf2242c981371224e5e9e89d6c265d554c8989@65.21.202.154:21656,5f29f14fe3dd7e1d86caa4d344e67ee81c32255f@65.109.37.228:26656,641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,6ad5dd14c578016cc7bc4d7c6d6f7f773bba39af@65.109.60.57:26656,9d17d1c5b5d3b8c9e7ffab264b45b5dd979116f3@65.109.24.188:26656,aa2feb704c0089b1a0f23011a9e7cd2c27a06134@65.21.200.6:29656,fa292bfad37826c9da43894b349b1480dff516b5@65.108.99.254:31656,b570827e4397512e077028ea7121d3e19eb25bab@85.10.200.221:26656,ab6a4ae2857ac05fa8f45b03871fa3945193fc61@46.4.81.204:35656,c126eed9cfede7802d78f570fec8175835309a73@141.95.127.146:26656,a3d975c913570ad217d9a3de01a8616ad5ce20f8@142.132.128.137:26656,7ee74ea68e350fc5214657255cba5e339bb30c2a@138.201.127.91:26674,5a13200e67f6cb5385d9d8f8c68a7b5e62f8cd54@188.34.176.96:26656,d6c891779edb84d91aa7dd043dcc819c11bf6895@185.245.183.106:26656,c0b33353fb70d8d71dcb9c8848b3b4207bd56951@188.165.221.155:30547,f97a11f283cd5f11bf1fe73d8b2012b711d61ce9@38.242.205.80:21656,5c2018214fcfde67ec390702539f295165f12a3a@86.48.2.20:26656,3a3e7123b9ae814b8d8517b6635d21b9ae45bf25@195.3.222.148:26656,d241f395a167fd7a9f155641760bffa8af6a50d2@167.235.98.202:27656,34e3178b6e0f25451fd690c15fc199d5a9bdfb9b@15.204.197.11:26656,f968f06c0f9c08cf7c9ccaf933cc903023ebcc24@194.163.167.122:26656,f0d73a4976e64643ffc6d3fc335725902b795491@162.248.225.244:26656,a35d28e111c1dcc1e5f3203627b449adfb4425f2@65.109.29.150:21656,237bfc05da5f8cabee00f148995333f37186d232@164.68.121.101:26656,f467e286567f94c89d39a5bcea0e1d68951299f9@146.59.81.204:34456,c177f05fc7c0379e26eff108048c0bfd96949b2c@141.95.65.73:17256,e04e8466071f8f00defce1d45c27ca6118bac358@135.125.4.73:54556,e1c9e76dad377c46322ba32b0d5edc261cac6e69@212.8.240.13:21656,d28516746773bfaeca4efa5537c0bf5990b8828e@65.21.229.33:27656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.rebusd/config/config.toml
```
