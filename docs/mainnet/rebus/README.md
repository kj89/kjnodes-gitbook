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
peers="256d9790bf186f5a275790f7fe01e1b8800dcaaf@65.21.88.78:26656,75c5365e8da9a4caa908a195ffa3fdc1e6432019@65.108.232.248:26756,4e2a874e538319f204f03751a5e458d0371d5b92@65.108.98.125:60556,346bf012c17fa30ef70ae72f082374838626532a@65.108.106.131:26696,aa2feb704c0089b1a0f23011a9e7cd2c27a06134@65.21.200.6:29656,4a4d2e7070e05ad6c13628d2f191d96172659452@65.109.65.210:40656,ab6a4ae2857ac05fa8f45b03871fa3945193fc61@46.4.81.204:35656,7ee74ea68e350fc5214657255cba5e339bb30c2a@138.201.127.91:26674,5c2018214fcfde67ec390702539f295165f12a3a@86.48.2.20:26656,5f4b34cf261bb4f2c14b8a707ed6cdbbee75d500@154.53.60.246:26656,b8137c688096d1abcf56942d335d061f212e6629@62.212.65.138:34656,34e3178b6e0f25451fd690c15fc199d5a9bdfb9b@15.204.197.11:26656,cd71aa366822800a2aa7051fae69127f78b3f203@188.165.225.226:26656,98206a8f71578850f1d88f08ede96ebc7e7c76a9@176.9.188.21:52656,69e27ab9b46350654805df3ea8d9ac2f00af4e4c@38.242.244.85:26656,bb2a7dc81b9bd0e017409a2bbb71b12bb899e743@178.63.22.117:26656,3e319c765b7b48d518a2e3218efc317234b81681@142.132.159.188:26656,a35d28e111c1dcc1e5f3203627b449adfb4425f2@65.109.29.150:21656,170397e75ca2b0f4e9f3b1bb5d0d23f9b10f01c7@94.23.23.189:30544,30ff8100fefac53ee40ef7631f1a3c66ca2b82cf@135.181.164.90:26656,ad613c7b9c6bb978edd86ae1116cf4c0e0b45c22@92.205.61.172:28656,ce38728ac38ebbb4a72d496d42f8e9030af441d7@162.19.137.25:26656,304ff8e051b2fbd038771142b69ac915c14c0819@78.46.78.83:26656,f6b555005ed8268412906c93a774e85020f6042d@194.163.169.166:26656,f0d73a4976e64643ffc6d3fc335725902b795491@162.248.225.244:26656,c126eed9cfede7802d78f570fec8175835309a73@141.95.127.146:26656,b1b08fe470551dca6d6631fb1bfabb814f6c1aec@54.37.129.164:54556,641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:21656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.rebusd/config/config.toml
```
