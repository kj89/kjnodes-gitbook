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
peers="5f29f14fe3dd7e1d86caa4d344e67ee81c32255f@65.109.37.228:26656,b5bf2242c981371224e5e9e89d6c265d554c8989@65.21.202.154:21656,30ff8100fefac53ee40ef7631f1a3c66ca2b82cf@135.181.164.90:26656,6ac55af662061d3669d7c70961a8fd87ba2f2075@65.108.200.142:26696,eeca453e3a1cf670c78e2255b8f0bd5a9443c30b@65.108.225.71:26656,aa2feb704c0089b1a0f23011a9e7cd2c27a06134@65.21.200.6:29656,3cc5fb5f6140ac4e57dfc80940c8a06daa299c89@51.77.195.46:26656,bb2a7dc81b9bd0e017409a2bbb71b12bb899e743@178.63.22.117:26656,ab6a4ae2857ac05fa8f45b03871fa3945193fc61@46.4.81.204:35656,77ca73199cf0a73ab52fc216d8ab8f8756275fef@138.201.8.248:52656,0fedf7695d9e2721663c1d573d6d81a14c21533e@65.21.90.137:12856,5c2018214fcfde67ec390702539f295165f12a3a@86.48.2.20:26656,f467e286567f94c89d39a5bcea0e1d68951299f9@146.59.81.204:34456,170397e75ca2b0f4e9f3b1bb5d0d23f9b10f01c7@94.23.23.189:30544,3a3e7123b9ae814b8d8517b6635d21b9ae45bf25@195.3.222.148:26656,b1b08fe470551dca6d6631fb1bfabb814f6c1aec@54.37.129.164:54556,2b7c68e1099e0a9dc10de0fc902923294018d048@135.125.5.31:54556,a35d28e111c1dcc1e5f3203627b449adfb4425f2@65.109.29.150:21656,c0b33353fb70d8d71dcb9c8848b3b4207bd56951@188.165.221.155:30547,c126eed9cfede7802d78f570fec8175835309a73@141.95.127.146:26656,1749a8f0aa533fc92c1212366c22c0993fbb1545@51.178.47.116:26656,b570827e4397512e077028ea7121d3e19eb25bab@85.10.200.221:26656,92e47c8be2b13575c61534498520b9dc813b5ea5@185.187.169.194:22656,34e3178b6e0f25451fd690c15fc199d5a9bdfb9b@15.204.197.11:26656,ad116a3f497ebb37ac14226c22a1483237a224ac@65.108.229.102:23656,4e2a874e538319f204f03751a5e458d0371d5b92@65.108.98.125:60556,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:21656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.rebusd/config/config.toml
```
