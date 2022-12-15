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
peers="12e6bea6650a53150c01ca3897e4a0b94d6e9d4e@135.181.141.47:26656,dda7abe32cc84a722cf6b1d2ee3b61ebe7ad71df@135.181.212.183:21656,9d17d1c5b5d3b8c9e7ffab264b45b5dd979116f3@65.109.24.188:26656,f546370843f92e2415524a7b18f9cd528e2fd706@65.109.55.186:26656,1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,b8613a7717b0ebaf2100c360cf13c92c4de33100@195.201.63.87:41666,a35d28e111c1dcc1e5f3203627b449adfb4425f2@65.109.29.150:21656,c126eed9cfede7802d78f570fec8175835309a73@141.95.127.146:26656,b570827e4397512e077028ea7121d3e19eb25bab@85.10.200.221:26656,2f6b34ad97c4827dace87436f0299cf89fe0c056@136.243.95.80:46656,f4ad005ee8ec25508c498294e9e83d81b188ea49@185.248.24.16:21656,1749a8f0aa533fc92c1212366c22c0993fbb1545@51.178.47.116:26656,34e3178b6e0f25451fd690c15fc199d5a9bdfb9b@15.204.197.11:26656,ab6a4ae2857ac05fa8f45b03871fa3945193fc61@46.4.81.204:35656,ae67d4c37632435e0d5f27041f50af20d227bdc2@93.170.72.118:21656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,cd71aa366822800a2aa7051fae69127f78b3f203@188.165.225.226:26656,b8137c688096d1abcf56942d335d061f212e6629@62.212.65.138:34656,b8c42fcb311b47cdb8285b5697f661fbba5bf1a5@51.68.157.129:26656,5c2018214fcfde67ec390702539f295165f12a3a@86.48.2.20:26656,aa2feb704c0089b1a0f23011a9e7cd2c27a06134@65.21.200.6:29656,9832950578c4492d934d6e875165757f5a98caff@51.83.96.150:26637,fa292bfad37826c9da43894b349b1480dff516b5@65.108.99.254:31656,4a4d2e7070e05ad6c13628d2f191d96172659452@65.109.65.210:40656,3cc5fb5f6140ac4e57dfc80940c8a06daa299c89@51.77.195.46:26656,6d8c83cc702365363b829a14efdd414401da369b@23.88.69.167:27565,3a3e7123b9ae814b8d8517b6635d21b9ae45bf25@195.3.222.148:26656,b8ed7daa4e2966f6c160915600d7dadf7e3ef61e@62.171.142.94:26156,d28516746773bfaeca4efa5537c0bf5990b8828e@65.21.229.33:27656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.rebusd/config/config.toml
```
