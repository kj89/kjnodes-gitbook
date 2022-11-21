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
peers="36afb1c827f52d38d7cd328b384d644b531b5997@65.108.238.102:17256,9abd6680cf74fce2ade8edfd8a898dd4a927a425@38.242.242.99:30656,d28516746773bfaeca4efa5537c0bf5990b8828e@65.21.229.33:27656,aa2feb704c0089b1a0f23011a9e7cd2c27a06134@65.21.200.6:29656,6ac55af662061d3669d7c70961a8fd87ba2f2075@65.108.200.142:26696,ff7031f45a97600076f72b9318167e3dfcd2a17e@65.21.136.170:52656,f83df63886e56713bf3adb5c6836b1a7b07ec024@65.108.235.18:26656,4a4d2e7070e05ad6c13628d2f191d96172659452@65.109.65.210:40656,e04e8466071f8f00defce1d45c27ca6118bac358@135.125.4.73:54556,17779ded6b3dc2f31d6c6f40cc6f07d802753ba7@78.47.153.128:26656,d6c891779edb84d91aa7dd043dcc819c11bf6895@185.245.183.106:26656,2f6b34ad97c4827dace87436f0299cf89fe0c056@136.243.95.80:46656,ab6a4ae2857ac05fa8f45b03871fa3945193fc61@46.4.81.204:35656,6d8c83cc702365363b829a14efdd414401da369b@23.88.69.167:27565,f4ad005ee8ec25508c498294e9e83d81b188ea49@185.248.24.16:21656,0fedf7695d9e2721663c1d573d6d81a14c21533e@65.21.90.137:12856,f968f06c0f9c08cf7c9ccaf933cc903023ebcc24@194.163.167.122:26656,c0b33353fb70d8d71dcb9c8848b3b4207bd56951@188.165.221.155:30547,f97a11f283cd5f11bf1fe73d8b2012b711d61ce9@38.242.205.80:21656,a155d381099de93e7efe00f9475786abffd29c3e@167.235.29.125:26637,170397e75ca2b0f4e9f3b1bb5d0d23f9b10f01c7@94.23.23.189:30544,c126eed9cfede7802d78f570fec8175835309a73@141.95.127.146:26656,5f4b34cf261bb4f2c14b8a707ed6cdbbee75d500@154.53.60.246:26656,ad613c7b9c6bb978edd86ae1116cf4c0e0b45c22@92.205.61.172:28656,e056318da91e77585f496333040e00e12f6941d1@51.83.97.166:26656,bb2a7dc81b9bd0e017409a2bbb71b12bb899e743@178.63.22.117:26656,f2483e5af4cb1fab55e4f6422627c0365f45b5dd@194.163.188.252:26656,7ee74ea68e350fc5214657255cba5e339bb30c2a@138.201.127.91:26674,1f7c31506f465c5f5536862074e98fc7a6043d4c@65.108.13.212:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:21656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.rebusd/config/config.toml
```
