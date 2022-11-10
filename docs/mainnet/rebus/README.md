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
peers="a35d28e111c1dcc1e5f3203627b449adfb4425f2@65.109.29.150:21656,4a4d2e7070e05ad6c13628d2f191d96172659452@65.109.65.210:40656,d28516746773bfaeca4efa5537c0bf5990b8828e@65.21.229.33:27656,36afb1c827f52d38d7cd328b384d644b531b5997@65.108.238.102:17256,ff7031f45a97600076f72b9318167e3dfcd2a17e@65.21.136.170:52656,12e6bea6650a53150c01ca3897e4a0b94d6e9d4e@135.181.141.47:26656,afdd27b58e851dcbb8c98c0e3191a0d8bfbcd3ae@65.108.41.252:26656,256d9790bf186f5a275790f7fe01e1b8800dcaaf@65.21.88.78:26656,c177f05fc7c0379e26eff108048c0bfd96949b2c@141.95.65.73:17256,3cc5fb5f6140ac4e57dfc80940c8a06daa299c89@51.77.195.46:26656,1749a8f0aa533fc92c1212366c22c0993fbb1545@51.178.47.116:26656,ce38728ac38ebbb4a72d496d42f8e9030af441d7@162.19.137.25:26656,5a13200e67f6cb5385d9d8f8c68a7b5e62f8cd54@188.34.176.96:26656,42d76e6353f9f2206ca062935d0523baa4b7f671@116.202.227.117:21656,a3d975c913570ad217d9a3de01a8616ad5ce20f8@142.132.128.137:26656,77ca73199cf0a73ab52fc216d8ab8f8756275fef@138.201.8.248:52656,cd71aa366822800a2aa7051fae69127f78b3f203@188.165.225.226:26656,d41384a02d523f1ec7310105413e75be2a76b252@85.17.77.84:26658,0fedf7695d9e2721663c1d573d6d81a14c21533e@65.21.90.137:12856,237bfc05da5f8cabee00f148995333f37186d232@164.68.121.101:26656,2f6b34ad97c4827dace87436f0299cf89fe0c056@136.243.95.80:46656,b1dcbb37514fbe215be54079e71aa39dac7fd0ae@64.5.123.203:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:21656,b5bf2242c981371224e5e9e89d6c265d554c8989@65.21.202.154:21656,6ac55af662061d3669d7c70961a8fd87ba2f2075@65.108.200.142:26696,a155d381099de93e7efe00f9475786abffd29c3e@167.235.29.125:26637,bb2a7dc81b9bd0e017409a2bbb71b12bb899e743@178.63.22.117:26656,17779ded6b3dc2f31d6c6f40cc6f07d802753ba7@78.47.153.128:26656,ae67d4c37632435e0d5f27041f50af20d227bdc2@93.170.72.118:21656,5fb9952f3eaeb5be3aab37425831c2a4830a019d@65.21.133.125:29656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.rebusd/config/config.toml
```
