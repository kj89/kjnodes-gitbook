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
peers="4e2a874e538319f204f03751a5e458d0371d5b92@65.108.98.125:60556,641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,256d9790bf186f5a275790f7fe01e1b8800dcaaf@65.21.88.78:26656,ad116a3f497ebb37ac14226c22a1483237a224ac@65.108.229.102:23656,9d17d1c5b5d3b8c9e7ffab264b45b5dd979116f3@65.109.24.188:26656,c126eed9cfede7802d78f570fec8175835309a73@141.95.127.146:26656,ce38728ac38ebbb4a72d496d42f8e9030af441d7@162.19.137.25:26656,8f023504e27873141164b6fbf1c4b788ff8d533b@159.69.200.24:26656,a3d975c913570ad217d9a3de01a8616ad5ce20f8@142.132.128.137:26656,7ee74ea68e350fc5214657255cba5e339bb30c2a@138.201.127.91:26674,98206a8f71578850f1d88f08ede96ebc7e7c76a9@176.9.188.21:52656,ab6a4ae2857ac05fa8f45b03871fa3945193fc61@46.4.81.204:35656,cd71aa366822800a2aa7051fae69127f78b3f203@188.165.225.226:26656,ad613c7b9c6bb978edd86ae1116cf4c0e0b45c22@92.205.61.172:28656,b1b08fe470551dca6d6631fb1bfabb814f6c1aec@54.37.129.164:54556,4a4d2e7070e05ad6c13628d2f191d96172659452@65.109.65.210:40656,f4ad005ee8ec25508c498294e9e83d81b188ea49@185.248.24.16:21656,34e3178b6e0f25451fd690c15fc199d5a9bdfb9b@15.204.197.11:26656,036c453576f9f4cad684e78d09e0fbf876e9cdee@54.39.243.226:22656,f0d73a4976e64643ffc6d3fc335725902b795491@162.248.225.244:26656,186209f02d238b48dcc7997cca3e6c6855aa91aa@20.112.73.169:26656,408206e3aab058d1dc09697566e3dadfaa3760ea@135.181.5.47:20106,5f29f14fe3dd7e1d86caa4d344e67ee81c32255f@65.109.37.228:26656,89ded0a3987d22e46b756fead439e2a4d25f23cb@185.144.99.30:26656,3fc3b7e3073cc0d59fef9390cad15601d7109dd0@65.108.193.11:26656,1f7c31506f465c5f5536862074e98fc7a6043d4c@65.108.13.212:26656,bb2a7dc81b9bd0e017409a2bbb71b12bb899e743@178.63.22.117:26656,d6c891779edb84d91aa7dd043dcc819c11bf6895@185.245.183.106:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:21656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.rebusd/config/config.toml
```
