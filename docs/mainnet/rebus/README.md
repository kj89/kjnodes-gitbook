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
peers="256d9790bf186f5a275790f7fe01e1b8800dcaaf@65.21.88.78:26656,346bf012c17fa30ef70ae72f082374838626532a@65.108.106.131:26696,641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,75c5365e8da9a4caa908a195ffa3fdc1e6432019@65.108.232.248:26756,aa2feb704c0089b1a0f23011a9e7cd2c27a06134@65.21.200.6:29656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:21656,4a4d2e7070e05ad6c13628d2f191d96172659452@65.109.65.210:40656,17779ded6b3dc2f31d6c6f40cc6f07d802753ba7@78.47.153.128:26656,ab6a4ae2857ac05fa8f45b03871fa3945193fc61@46.4.81.204:35656,cd71aa366822800a2aa7051fae69127f78b3f203@188.165.225.226:26656,34e3178b6e0f25451fd690c15fc199d5a9bdfb9b@15.204.197.11:26656,7196b111260698b8b6ba8ea64c3af0444fb365c8@195.201.63.87:41656,5a13200e67f6cb5385d9d8f8c68a7b5e62f8cd54@188.34.176.96:26656,49e084a4c77f168810608e20b530ee9d25ac69b7@209.126.8.176:26656,186209f02d238b48dcc7997cca3e6c6855aa91aa@20.112.73.169:26656,ea5e7a6b9a5c18c6455e7a8c583c129c5821a452@51.178.80.111:26656,b574e11e103058a121cc03d1c4d9867ba3daed34@135.181.139.113:31656,42d76e6353f9f2206ca062935d0523baa4b7f671@116.202.227.117:21656,237bfc05da5f8cabee00f148995333f37186d232@164.68.121.101:26656,036c453576f9f4cad684e78d09e0fbf876e9cdee@54.39.243.226:22656,c177f05fc7c0379e26eff108048c0bfd96949b2c@141.95.65.73:17256,30ff8100fefac53ee40ef7631f1a3c66ca2b82cf@135.181.164.90:26656,d6c891779edb84d91aa7dd043dcc819c11bf6895@185.245.183.106:26656,69e27ab9b46350654805df3ea8d9ac2f00af4e4c@38.242.244.85:26656,89ded0a3987d22e46b756fead439e2a4d25f23cb@185.144.99.30:26656,7ee74ea68e350fc5214657255cba5e339bb30c2a@138.201.127.91:26674,d12f9b52ca0e11cdeca5c46e802249ade4c39c45@185.248.24.40:26656,3e319c765b7b48d518a2e3218efc317234b81681@142.132.159.188:26656,1e3e466e9e0bfc129d69c0fb71149aea9557bd98@51.89.40.96:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.rebusd/config/config.toml
```
