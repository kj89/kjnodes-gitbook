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
peers="f4ad005ee8ec25508c498294e9e83d81b188ea49@185.248.24.16:21656,6ac55af662061d3669d7c70961a8fd87ba2f2075@65.108.200.142:26696,5f29f14fe3dd7e1d86caa4d344e67ee81c32255f@65.109.37.228:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,170397e75ca2b0f4e9f3b1bb5d0d23f9b10f01c7@94.23.23.189:30544,6ad5dd14c578016cc7bc4d7c6d6f7f773bba39af@65.109.60.57:26656,b570827e4397512e077028ea7121d3e19eb25bab@85.10.200.221:26656,2f6b34ad97c4827dace87436f0299cf89fe0c056@136.243.95.80:46656,5a13200e67f6cb5385d9d8f8c68a7b5e62f8cd54@188.34.176.96:26656,1fe32d8f09b8715b1e626da17b3ecfe26623b371@176.9.22.117:27656,aa2feb704c0089b1a0f23011a9e7cd2c27a06134@65.21.200.6:29656,f467e286567f94c89d39a5bcea0e1d68951299f9@146.59.81.204:34456,6daeb8cfea285f561e167a0d94718b61e2cf7944@5.189.187.36:21656,b8c42fcb311b47cdb8285b5697f661fbba5bf1a5@51.68.157.129:26656,ea5e7a6b9a5c18c6455e7a8c583c129c5821a452@51.178.80.111:26656,49e084a4c77f168810608e20b530ee9d25ac69b7@209.126.8.176:26656,641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,f546370843f92e2415524a7b18f9cd528e2fd706@65.109.55.186:26656,9d17d1c5b5d3b8c9e7ffab264b45b5dd979116f3@65.109.24.188:26656,f2483e5af4cb1fab55e4f6422627c0365f45b5dd@194.163.188.252:26656,3a3e7123b9ae814b8d8517b6635d21b9ae45bf25@195.3.222.148:26656,b1b08fe470551dca6d6631fb1bfabb814f6c1aec@54.37.129.164:54556,6d8c83cc702365363b829a14efdd414401da369b@23.88.69.167:27565,ab6a4ae2857ac05fa8f45b03871fa3945193fc61@46.4.81.204:35656,69e27ab9b46350654805df3ea8d9ac2f00af4e4c@38.242.244.85:26656,b1dcbb37514fbe215be54079e71aa39dac7fd0ae@64.5.123.203:26656,77ca73199cf0a73ab52fc216d8ab8f8756275fef@138.201.8.248:52656,b8613a7717b0ebaf2100c360cf13c92c4de33100@195.201.63.87:41666,ce38728ac38ebbb4a72d496d42f8e9030af441d7@162.19.137.25:26656,b8137c688096d1abcf56942d335d061f212e6629@62.212.65.138:34656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.rebusd/config/config.toml
```
