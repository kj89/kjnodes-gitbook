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
peers="fa292bfad37826c9da43894b349b1480dff516b5@65.108.99.254:31656,18ec83c4e3938aec31a3a32154969107739f0b81@135.181.153.228:26656,1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,4a4d2e7070e05ad6c13628d2f191d96172659452@65.109.65.210:40656,12703ce9efe6c1171c193dae2e2041a2be610852@65.108.44.149:29656,9d17d1c5b5d3b8c9e7ffab264b45b5dd979116f3@65.109.24.188:26656,eeca453e3a1cf670c78e2255b8f0bd5a9443c30b@65.108.225.71:26656,d3a8fdbe6776fc71998fa893abcd634461b52b19@65.109.92.241:40106,e056318da91e77585f496333040e00e12f6941d1@51.83.97.166:26656,5f4b34cf261bb4f2c14b8a707ed6cdbbee75d500@154.53.60.246:26656,b570827e4397512e077028ea7121d3e19eb25bab@85.10.200.221:26656,7ee74ea68e350fc5214657255cba5e339bb30c2a@138.201.127.91:26674,34e3178b6e0f25451fd690c15fc199d5a9bdfb9b@15.204.197.11:26656,89ded0a3987d22e46b756fead439e2a4d25f23cb@185.144.99.30:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,6d8c83cc702365363b829a14efdd414401da369b@23.88.69.167:27565,c177f05fc7c0379e26eff108048c0bfd96949b2c@141.95.65.73:17256,77ca73199cf0a73ab52fc216d8ab8f8756275fef@138.201.8.248:52656,12e6bea6650a53150c01ca3897e4a0b94d6e9d4e@135.181.141.47:26656,6ac55af662061d3669d7c70961a8fd87ba2f2075@65.108.200.142:26696,0fedf7695d9e2721663c1d573d6d81a14c21533e@65.21.90.137:12856,ab6a4ae2857ac05fa8f45b03871fa3945193fc61@46.4.81.204:35656,b5bf2242c981371224e5e9e89d6c265d554c8989@65.21.202.154:21656,69e27ab9b46350654805df3ea8d9ac2f00af4e4c@38.242.244.85:26656,235a2754b94c86a85ba645119151ee55d6971554@213.239.216.252:26656,237bfc05da5f8cabee00f148995333f37186d232@164.68.121.101:26656,ce38728ac38ebbb4a72d496d42f8e9030af441d7@162.19.137.25:26656,b8c42fcb311b47cdb8285b5697f661fbba5bf1a5@51.68.157.129:26656,b8ed7daa4e2966f6c160915600d7dadf7e3ef61e@62.171.142.94:26156"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.rebusd/config/config.toml
```
