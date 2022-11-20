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
peers="641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,fa292bfad37826c9da43894b349b1480dff516b5@65.108.99.254:31656,6ad5dd14c578016cc7bc4d7c6d6f7f773bba39af@65.109.60.57:26656,75c5365e8da9a4caa908a195ffa3fdc1e6432019@65.108.232.248:26756,6d8c83cc702365363b829a14efdd414401da369b@23.88.69.167:27565,1f7c31506f465c5f5536862074e98fc7a6043d4c@65.108.13.212:26656,eeca453e3a1cf670c78e2255b8f0bd5a9443c30b@65.108.225.71:26656,4e2a874e538319f204f03751a5e458d0371d5b92@65.108.98.125:60556,a35d28e111c1dcc1e5f3203627b449adfb4425f2@65.109.29.150:21656,aa2feb704c0089b1a0f23011a9e7cd2c27a06134@65.21.200.6:29656,b570827e4397512e077028ea7121d3e19eb25bab@85.10.200.221:26656,d6c891779edb84d91aa7dd043dcc819c11bf6895@185.245.183.106:26656,a155d381099de93e7efe00f9475786abffd29c3e@167.235.29.125:26637,5a13200e67f6cb5385d9d8f8c68a7b5e62f8cd54@188.34.176.96:26656,304ff8e051b2fbd038771142b69ac915c14c0819@78.46.78.83:26656,d13731f28e49df608c42e4e7050923fb3a461f3b@34.80.65.34:26656,f968f06c0f9c08cf7c9ccaf933cc903023ebcc24@194.163.167.122:26656,a3d975c913570ad217d9a3de01a8616ad5ce20f8@142.132.128.137:26656,b8137c688096d1abcf56942d335d061f212e6629@62.212.65.138:34656,f467e286567f94c89d39a5bcea0e1d68951299f9@146.59.81.204:34456,b8c42fcb311b47cdb8285b5697f661fbba5bf1a5@51.68.157.129:26656,c126eed9cfede7802d78f570fec8175835309a73@141.95.127.146:26656,34e3178b6e0f25451fd690c15fc199d5a9bdfb9b@15.204.197.11:26656,40e2c0b68a1dd48466714e3dd0581e4b7d498575@107.155.122.93:26656,e04e8466071f8f00defce1d45c27ca6118bac358@135.125.4.73:54556,056d6a61c8a4c5ccb02123d67a013434423f155a@149.102.142.57:26656,ff7031f45a97600076f72b9318167e3dfcd2a17e@65.21.136.170:52656,6ac55af662061d3669d7c70961a8fd87ba2f2075@65.108.200.142:26696,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:21656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.rebusd/config/config.toml
```
