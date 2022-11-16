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
peers="5f29f14fe3dd7e1d86caa4d344e67ee81c32255f@65.109.37.228:26656,75c5365e8da9a4caa908a195ffa3fdc1e6432019@65.108.232.248:26756,ad116a3f497ebb37ac14226c22a1483237a224ac@65.108.229.102:23656,408206e3aab058d1dc09697566e3dadfaa3760ea@135.181.5.47:20106,1f7c31506f465c5f5536862074e98fc7a6043d4c@65.108.13.212:26656,b5bf2242c981371224e5e9e89d6c265d554c8989@65.21.202.154:21656,3a3e7123b9ae814b8d8517b6635d21b9ae45bf25@195.3.222.148:26656,c126eed9cfede7802d78f570fec8175835309a73@141.95.127.146:26656,b570827e4397512e077028ea7121d3e19eb25bab@85.10.200.221:26656,7ee74ea68e350fc5214657255cba5e339bb30c2a@138.201.127.91:26674,ab6a4ae2857ac05fa8f45b03871fa3945193fc61@46.4.81.204:35656,e6e888332d1930e24daecbe587500de6360f41cb@65.108.104.253:26656,5c2018214fcfde67ec390702539f295165f12a3a@86.48.2.20:26656,69e27ab9b46350654805df3ea8d9ac2f00af4e4c@38.242.244.85:26656,d6c891779edb84d91aa7dd043dcc819c11bf6895@185.245.183.106:26656,0fedf7695d9e2721663c1d573d6d81a14c21533e@65.21.90.137:12856,b1b08fe470551dca6d6631fb1bfabb814f6c1aec@54.37.129.164:54556,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:21656,34e3178b6e0f25451fd690c15fc199d5a9bdfb9b@15.204.197.11:26656,f0d73a4976e64643ffc6d3fc335725902b795491@162.248.225.244:26656,186209f02d238b48dcc7997cca3e6c6855aa91aa@20.112.73.169:26656,641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,a3d975c913570ad217d9a3de01a8616ad5ce20f8@142.132.128.137:26656,f97a11f283cd5f11bf1fe73d8b2012b711d61ce9@38.242.205.80:21656,eeca453e3a1cf670c78e2255b8f0bd5a9443c30b@65.108.225.71:26656,5f4b34cf261bb4f2c14b8a707ed6cdbbee75d500@154.53.60.246:26656,6ac55af662061d3669d7c70961a8fd87ba2f2075@65.108.200.142:26696,6d8c83cc702365363b829a14efdd414401da369b@23.88.69.167:27565"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.rebusd/config/config.toml
```
