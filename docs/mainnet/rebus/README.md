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

**live-peers** (28)
```
peers="b5bf2242c981371224e5e9e89d6c265d554c8989@65.21.202.154:21656,9d17d1c5b5d3b8c9e7ffab264b45b5dd979116f3@65.109.24.188:26656,12e6bea6650a53150c01ca3897e4a0b94d6e9d4e@135.181.141.47:26656,641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,5f29f14fe3dd7e1d86caa4d344e67ee81c32255f@65.109.37.228:26656,1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,c177f05fc7c0379e26eff108048c0bfd96949b2c@141.95.65.73:17256,e056318da91e77585f496333040e00e12f6941d1@51.83.97.166:26656,b570827e4397512e077028ea7121d3e19eb25bab@85.10.200.221:26656,2f6b34ad97c4827dace87436f0299cf89fe0c056@136.243.95.80:46656,304ff8e051b2fbd038771142b69ac915c14c0819@78.46.78.83:26656,ab6a4ae2857ac05fa8f45b03871fa3945193fc61@46.4.81.204:35656,b8c42fcb311b47cdb8285b5697f661fbba5bf1a5@51.68.157.129:26656,34e3178b6e0f25451fd690c15fc199d5a9bdfb9b@15.204.197.11:26656,12703ce9efe6c1171c193dae2e2041a2be610852@65.108.44.149:29656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,170397e75ca2b0f4e9f3b1bb5d0d23f9b10f01c7@94.23.23.189:30544,b1dcbb37514fbe215be54079e71aa39dac7fd0ae@64.5.123.203:26656,69e27ab9b46350654805df3ea8d9ac2f00af4e4c@38.242.244.85:26656,a3d975c913570ad217d9a3de01a8616ad5ce20f8@142.132.128.137:26656,ea5e7a6b9a5c18c6455e7a8c583c129c5821a452@51.178.80.111:26656,18ec83c4e3938aec31a3a32154969107739f0b81@135.181.153.228:26656,ce38728ac38ebbb4a72d496d42f8e9030af441d7@162.19.137.25:26656,ff7031f45a97600076f72b9318167e3dfcd2a17e@65.21.136.170:52656,b8ed7daa4e2966f6c160915600d7dadf7e3ef61e@62.171.142.94:26156,77ca73199cf0a73ab52fc216d8ab8f8756275fef@138.201.8.248:52656,f2483e5af4cb1fab55e4f6422627c0365f45b5dd@194.163.188.252:26656,1749a8f0aa533fc92c1212366c22c0993fbb1545@51.178.47.116:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.rebusd/config/config.toml
```
