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
peers="3fc3b7e3073cc0d59fef9390cad15601d7109dd0@65.108.193.11:26656,aa2feb704c0089b1a0f23011a9e7cd2c27a06134@65.21.200.6:29656,1f7c31506f465c5f5536862074e98fc7a6043d4c@65.108.13.212:26656,ff7031f45a97600076f72b9318167e3dfcd2a17e@65.21.136.170:52656,c177f05fc7c0379e26eff108048c0bfd96949b2c@141.95.65.73:17256,ce38728ac38ebbb4a72d496d42f8e9030af441d7@162.19.137.25:26656,17779ded6b3dc2f31d6c6f40cc6f07d802753ba7@78.47.153.128:26656,a3d975c913570ad217d9a3de01a8616ad5ce20f8@142.132.128.137:26656,bb2a7dc81b9bd0e017409a2bbb71b12bb899e743@178.63.22.117:26656,e056318da91e77585f496333040e00e12f6941d1@51.83.97.166:26656,7ee74ea68e350fc5214657255cba5e339bb30c2a@138.201.127.91:26674,c126eed9cfede7802d78f570fec8175835309a73@141.95.127.146:26656,d6c891779edb84d91aa7dd043dcc819c11bf6895@185.245.183.106:26656,f467e286567f94c89d39a5bcea0e1d68951299f9@146.59.81.204:34456,b1b08fe470551dca6d6631fb1bfabb814f6c1aec@54.37.129.164:54556,3a3e7123b9ae814b8d8517b6635d21b9ae45bf25@195.3.222.148:26656,b5bf2242c981371224e5e9e89d6c265d554c8989@65.21.202.154:21656,6d8c83cc702365363b829a14efdd414401da369b@23.88.69.167:27565,f0d73a4976e64643ffc6d3fc335725902b795491@162.248.225.244:26656,cd71aa366822800a2aa7051fae69127f78b3f203@188.165.225.226:26656,b8c42fcb311b47cdb8285b5697f661fbba5bf1a5@51.68.157.129:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:21656,256d9790bf186f5a275790f7fe01e1b8800dcaaf@65.21.88.78:26656,a155d381099de93e7efe00f9475786abffd29c3e@167.235.29.125:26637,a35d28e111c1dcc1e5f3203627b449adfb4425f2@65.109.29.150:21656,b1dcbb37514fbe215be54079e71aa39dac7fd0ae@64.5.123.203:26656,5f29f14fe3dd7e1d86caa4d344e67ee81c32255f@65.109.37.228:26656,ab6a4ae2857ac05fa8f45b03871fa3945193fc61@46.4.81.204:35656,237bfc05da5f8cabee00f148995333f37186d232@164.68.121.101:26656,92245ff5c7a4b293d2f0c7f9afca0ddad2e0fb52@65.108.244.178:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.rebusd/config/config.toml
```
