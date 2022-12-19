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

**live-peers** (27)
```
peers="d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,1749a8f0aa533fc92c1212366c22c0993fbb1545@51.178.47.116:26656,17779ded6b3dc2f31d6c6f40cc6f07d802753ba7@78.47.153.128:26656,98206a8f71578850f1d88f08ede96ebc7e7c76a9@176.9.188.21:52656,5a13200e67f6cb5385d9d8f8c68a7b5e62f8cd54@188.34.176.96:26656,b1b08fe470551dca6d6631fb1bfabb814f6c1aec@54.37.129.164:54556,89ded0a3987d22e46b756fead439e2a4d25f23cb@185.144.99.30:26656,678ded952968137c8ded8aeada337662065f1507@159.203.162.120:26656,5f4b34cf261bb4f2c14b8a707ed6cdbbee75d500@154.53.60.246:26656,8f023504e27873141164b6fbf1c4b788ff8d533b@159.69.200.24:26656,c0b33353fb70d8d71dcb9c8848b3b4207bd56951@94.23.207.45:30547,f4ad005ee8ec25508c498294e9e83d81b188ea49@185.248.24.16:21656,6ad5dd14c578016cc7bc4d7c6d6f7f773bba39af@65.109.60.57:26656,30ff8100fefac53ee40ef7631f1a3c66ca2b82cf@135.181.164.90:26656,f546370843f92e2415524a7b18f9cd528e2fd706@65.109.55.186:26656,ce38728ac38ebbb4a72d496d42f8e9030af441d7@162.19.137.25:26656,170397e75ca2b0f4e9f3b1bb5d0d23f9b10f01c7@94.23.23.189:30544,b1dcbb37514fbe215be54079e71aa39dac7fd0ae@64.5.123.203:26656,b8c42fcb311b47cdb8285b5697f661fbba5bf1a5@51.68.157.129:26656,ad116a3f497ebb37ac14226c22a1483237a224ac@65.108.229.102:23656,f467e286567f94c89d39a5bcea0e1d68951299f9@146.59.81.204:34456,49e084a4c77f168810608e20b530ee9d25ac69b7@209.126.8.176:26656,404ae118865c1485f7859fa2c7cc2e3b8c402a14@51.75.135.34:26656,4a4d2e7070e05ad6c13628d2f191d96172659452@65.109.65.210:40656,346bf012c17fa30ef70ae72f082374838626532a@65.108.106.131:26696"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.rebusd/config/config.toml
```
