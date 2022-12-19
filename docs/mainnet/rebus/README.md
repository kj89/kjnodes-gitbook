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
peers="dda7abe32cc84a722cf6b1d2ee3b61ebe7ad71df@135.181.212.183:21656,12e6bea6650a53150c01ca3897e4a0b94d6e9d4e@135.181.141.47:26656,f546370843f92e2415524a7b18f9cd528e2fd706@65.109.55.186:26656,1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,34e3178b6e0f25451fd690c15fc199d5a9bdfb9b@15.204.197.11:26656,5f29f14fe3dd7e1d86caa4d344e67ee81c32255f@65.109.37.228:26656,18ec83c4e3938aec31a3a32154969107739f0b81@135.181.153.228:26656,09d22b9fc1b07f3e2f64b685ab6f28130bc2edd2@51.89.7.185:26637,8f023504e27873141164b6fbf1c4b788ff8d533b@159.69.200.24:26656,6d8c83cc702365363b829a14efdd414401da369b@23.88.69.167:27565,9d17d1c5b5d3b8c9e7ffab264b45b5dd979116f3@65.109.24.188:26656,ab6a4ae2857ac05fa8f45b03871fa3945193fc61@46.4.81.204:35656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,b8137c688096d1abcf56942d335d061f212e6629@62.212.65.138:34656,5c2018214fcfde67ec390702539f295165f12a3a@86.48.2.20:26656,056d6a61c8a4c5ccb02123d67a013434423f155a@149.102.142.57:26656,bb2a7dc81b9bd0e017409a2bbb71b12bb899e743@178.63.22.117:26656,b8c42fcb311b47cdb8285b5697f661fbba5bf1a5@51.68.157.129:26656,3a3e7123b9ae814b8d8517b6635d21b9ae45bf25@195.3.222.148:26656,4a4d2e7070e05ad6c13628d2f191d96172659452@65.109.65.210:40656,b570827e4397512e077028ea7121d3e19eb25bab@85.10.200.221:26656,b5bf2242c981371224e5e9e89d6c265d554c8989@65.21.202.154:21656,aa2feb704c0089b1a0f23011a9e7cd2c27a06134@65.21.200.6:29656,c126eed9cfede7802d78f570fec8175835309a73@141.95.127.146:26656,237bfc05da5f8cabee00f148995333f37186d232@164.68.121.101:26656,eeca453e3a1cf670c78e2255b8f0bd5a9443c30b@65.108.225.71:26656,641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,404ae118865c1485f7859fa2c7cc2e3b8c402a14@51.75.135.34:26656,49e084a4c77f168810608e20b530ee9d25ac69b7@209.126.8.176:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.rebusd/config/config.toml
```
