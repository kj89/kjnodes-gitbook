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
peers="f2483e5af4cb1fab55e4f6422627c0365f45b5dd@194.163.188.252:26656,1749a8f0aa533fc92c1212366c22c0993fbb1545@51.178.47.116:26656,f546370843f92e2415524a7b18f9cd528e2fd706@65.109.55.186:26656,256d9790bf186f5a275790f7fe01e1b8800dcaaf@65.21.88.78:26656,fa292bfad37826c9da43894b349b1480dff516b5@65.108.99.254:31656,d28516746773bfaeca4efa5537c0bf5990b8828e@65.21.229.33:27656,ab6a4ae2857ac05fa8f45b03871fa3945193fc61@46.4.81.204:35656,2f6b34ad97c4827dace87436f0299cf89fe0c056@136.243.95.80:46656,bb2a7dc81b9bd0e017409a2bbb71b12bb899e743@178.63.22.117:26656,e056318da91e77585f496333040e00e12f6941d1@51.83.97.166:26656,15b1c913dc3d9dab7c912b27bb2a957abbfe8834@142.132.199.27:40106,6d8c83cc702365363b829a14efdd414401da369b@23.88.69.167:27565,d6c891779edb84d91aa7dd043dcc819c11bf6895@185.245.183.106:26656,304ff8e051b2fbd038771142b69ac915c14c0819@78.46.78.83:26656,f97a11f283cd5f11bf1fe73d8b2012b711d61ce9@38.242.205.80:21656,5f4b34cf261bb4f2c14b8a707ed6cdbbee75d500@154.53.60.246:26656,3a3e7123b9ae814b8d8517b6635d21b9ae45bf25@195.3.222.148:26656,ae67d4c37632435e0d5f27041f50af20d227bdc2@93.170.72.118:21656,f467e286567f94c89d39a5bcea0e1d68951299f9@146.59.81.204:34456,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,7ee74ea68e350fc5214657255cba5e339bb30c2a@138.201.127.91:26674,c0b33353fb70d8d71dcb9c8848b3b4207bd56951@188.165.221.155:30547,12e6bea6650a53150c01ca3897e4a0b94d6e9d4e@135.181.141.47:26656,9832950578c4492d934d6e875165757f5a98caff@51.83.96.150:26637,b8ed7daa4e2966f6c160915600d7dadf7e3ef61e@62.171.142.94:26156,4a4d2e7070e05ad6c13628d2f191d96172659452@65.109.65.210:40656,cd71aa366822800a2aa7051fae69127f78b3f203@188.165.225.226:26656,b8613a7717b0ebaf2100c360cf13c92c4de33100@195.201.63.87:41666,aa2feb704c0089b1a0f23011a9e7cd2c27a06134@65.21.200.6:29656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.rebusd/config/config.toml
```
