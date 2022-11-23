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
peers="256d9790bf186f5a275790f7fe01e1b8800dcaaf@65.21.88.78:26656,eeca453e3a1cf670c78e2255b8f0bd5a9443c30b@65.108.225.71:26656,c126eed9cfede7802d78f570fec8175835309a73@141.95.127.146:26656,b570827e4397512e077028ea7121d3e19eb25bab@85.10.200.221:26656,6d8c83cc702365363b829a14efdd414401da369b@23.88.69.167:27565,2f6b34ad97c4827dace87436f0299cf89fe0c056@136.243.95.80:46656,d6c891779edb84d91aa7dd043dcc819c11bf6895@185.245.183.106:26656,5c2018214fcfde67ec390702539f295165f12a3a@86.48.2.20:26656,f4ad005ee8ec25508c498294e9e83d81b188ea49@185.248.24.16:21656,34e3178b6e0f25451fd690c15fc199d5a9bdfb9b@15.204.197.11:26656,f968f06c0f9c08cf7c9ccaf933cc903023ebcc24@194.163.167.122:26656,ce38728ac38ebbb4a72d496d42f8e9030af441d7@162.19.137.25:26656,f2483e5af4cb1fab55e4f6422627c0365f45b5dd@194.163.188.252:26656,f0d73a4976e64643ffc6d3fc335725902b795491@162.248.225.244:26656,a155d381099de93e7efe00f9475786abffd29c3e@167.235.29.125:26637,c0b33353fb70d8d71dcb9c8848b3b4207bd56951@188.165.221.155:30547,a35d28e111c1dcc1e5f3203627b449adfb4425f2@65.109.29.150:21656,3a3e7123b9ae814b8d8517b6635d21b9ae45bf25@195.3.222.148:26656,fa292bfad37826c9da43894b349b1480dff516b5@65.108.99.254:31656,e04e8466071f8f00defce1d45c27ca6118bac358@135.125.4.73:54556,9abd6680cf74fce2ade8edfd8a898dd4a927a425@38.242.242.99:30656,dda7abe32cc84a722cf6b1d2ee3b61ebe7ad71df@135.181.212.183:21656,186209f02d238b48dcc7997cca3e6c6855aa91aa@20.112.73.169:26656,9d17d1c5b5d3b8c9e7ffab264b45b5dd979116f3@65.109.24.188:26656,f97a11f283cd5f11bf1fe73d8b2012b711d61ce9@38.242.205.80:21656,e056318da91e77585f496333040e00e12f6941d1@51.83.97.166:26656,a3d975c913570ad217d9a3de01a8616ad5ce20f8@142.132.128.137:26656,1f7c31506f465c5f5536862074e98fc7a6043d4c@65.108.13.212:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:21656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.rebusd/config/config.toml
```
