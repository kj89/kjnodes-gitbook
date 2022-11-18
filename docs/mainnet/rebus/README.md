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
peers="75c5365e8da9a4caa908a195ffa3fdc1e6432019@65.108.232.248:26756,6ad5dd14c578016cc7bc4d7c6d6f7f773bba39af@65.109.60.57:26656,aa2feb704c0089b1a0f23011a9e7cd2c27a06134@65.21.200.6:29656,b5bf2242c981371224e5e9e89d6c265d554c8989@65.21.202.154:21656,eeca453e3a1cf670c78e2255b8f0bd5a9443c30b@65.108.225.71:26656,9d17d1c5b5d3b8c9e7ffab264b45b5dd979116f3@65.109.24.188:26656,2f6b34ad97c4827dace87436f0299cf89fe0c056@136.243.95.80:46656,a155d381099de93e7efe00f9475786abffd29c3e@167.235.29.125:26637,6d8c83cc702365363b829a14efdd414401da369b@23.88.69.167:27565,f968f06c0f9c08cf7c9ccaf933cc903023ebcc24@194.163.167.122:26656,c0b33353fb70d8d71dcb9c8848b3b4207bd56951@188.165.221.155:30547,c177f05fc7c0379e26eff108048c0bfd96949b2c@141.95.65.73:17256,f83df63886e56713bf3adb5c6836b1a7b07ec024@65.108.235.18:26656,186209f02d238b48dcc7997cca3e6c6855aa91aa@20.112.73.169:26656,7ee74ea68e350fc5214657255cba5e339bb30c2a@138.201.127.91:26674,4a4d2e7070e05ad6c13628d2f191d96172659452@65.109.65.210:40656,e056318da91e77585f496333040e00e12f6941d1@51.83.97.166:26656,5f29f14fe3dd7e1d86caa4d344e67ee81c32255f@65.109.37.228:26656,641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,b1b08fe470551dca6d6631fb1bfabb814f6c1aec@54.37.129.164:54556,f4ad005ee8ec25508c498294e9e83d81b188ea49@185.248.24.16:21656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:21656,0a3eb0b5a76b2b881ae260e4546e3fbbfbbfba4b@65.108.206.56:32656,d6c891779edb84d91aa7dd043dcc819c11bf6895@185.245.183.106:26656,3fc3b7e3073cc0d59fef9390cad15601d7109dd0@65.108.193.11:26656,85fbeb61beb838ecf2059411b62ef04be6275596@138.201.132.55:26656,bb2a7dc81b9bd0e017409a2bbb71b12bb899e743@178.63.22.117:26656,a3d975c913570ad217d9a3de01a8616ad5ce20f8@142.132.128.137:26656,a35d28e111c1dcc1e5f3203627b449adfb4425f2@65.109.29.150:21656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.rebusd/config/config.toml
```
