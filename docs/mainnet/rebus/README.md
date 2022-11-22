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
peers="6ac55af662061d3669d7c70961a8fd87ba2f2075@65.108.200.142:26696,5f29f14fe3dd7e1d86caa4d344e67ee81c32255f@65.109.37.228:26656,9d17d1c5b5d3b8c9e7ffab264b45b5dd979116f3@65.109.24.188:26656,6ad5dd14c578016cc7bc4d7c6d6f7f773bba39af@65.109.60.57:26656,4e2a874e538319f204f03751a5e458d0371d5b92@65.108.98.125:60556,e056318da91e77585f496333040e00e12f6941d1@51.83.97.166:26656,40e2c0b68a1dd48466714e3dd0581e4b7d498575@107.155.122.93:26656,d6c891779edb84d91aa7dd043dcc819c11bf6895@185.245.183.106:26656,a3d975c913570ad217d9a3de01a8616ad5ce20f8@142.132.128.137:26656,ff7031f45a97600076f72b9318167e3dfcd2a17e@65.21.136.170:52656,f2483e5af4cb1fab55e4f6422627c0365f45b5dd@194.163.188.252:26656,98206a8f71578850f1d88f08ede96ebc7e7c76a9@176.9.188.21:52656,ab6a4ae2857ac05fa8f45b03871fa3945193fc61@46.4.81.204:35656,07b84cf4b47a2e5ad251267716fe05bcf30330cd@65.21.170.3:29656,6daeb8cfea285f561e167a0d94718b61e2cf7944@5.189.187.36:21656,f968f06c0f9c08cf7c9ccaf933cc903023ebcc24@194.163.167.122:26656,34e3178b6e0f25451fd690c15fc199d5a9bdfb9b@15.204.197.11:26656,ae67d4c37632435e0d5f27041f50af20d227bdc2@93.170.72.118:21656,346bf012c17fa30ef70ae72f082374838626532a@65.108.106.131:26696,e04e8466071f8f00defce1d45c27ca6118bac358@135.125.4.73:54556,75c5365e8da9a4caa908a195ffa3fdc1e6432019@65.108.232.248:26756,a155d381099de93e7efe00f9475786abffd29c3e@167.235.29.125:26637,e6e888332d1930e24daecbe587500de6360f41cb@65.108.104.253:26656,afdd27b58e851dcbb8c98c0e3191a0d8bfbcd3ae@65.108.41.252:26656,b1b08fe470551dca6d6631fb1bfabb814f6c1aec@54.37.129.164:54556,9abd6680cf74fce2ade8edfd8a898dd4a927a425@38.242.242.99:30656,12e6bea6650a53150c01ca3897e4a0b94d6e9d4e@135.181.141.47:26656,aa2feb704c0089b1a0f23011a9e7cd2c27a06134@65.21.200.6:29656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:21656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.rebusd/config/config.toml
```
