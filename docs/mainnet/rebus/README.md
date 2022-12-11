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
peers="641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,4a4d2e7070e05ad6c13628d2f191d96172659452@65.109.65.210:40656,1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,12e6bea6650a53150c01ca3897e4a0b94d6e9d4e@135.181.141.47:26656,9d17d1c5b5d3b8c9e7ffab264b45b5dd979116f3@65.109.24.188:26656,e056318da91e77585f496333040e00e12f6941d1@51.83.97.166:26656,18ec83c4e3938aec31a3a32154969107739f0b81@135.181.153.228:26656,b570827e4397512e077028ea7121d3e19eb25bab@85.10.200.221:26656,69e27ab9b46350654805df3ea8d9ac2f00af4e4c@38.242.244.85:26656,0fedf7695d9e2721663c1d573d6d81a14c21533e@65.21.90.137:12856,b8137c688096d1abcf56942d335d061f212e6629@62.212.65.138:34656,b1b08fe470551dca6d6631fb1bfabb814f6c1aec@54.37.129.164:54556,89ded0a3987d22e46b756fead439e2a4d25f23cb@185.144.99.30:26656,34e3178b6e0f25451fd690c15fc199d5a9bdfb9b@15.204.197.11:26656,304ff8e051b2fbd038771142b69ac915c14c0819@78.46.78.83:26656,3a378fbfae33a593b913371c876c9d275c0abb12@213.239.215.77:26656,256d9790bf186f5a275790f7fe01e1b8800dcaaf@65.21.88.78:26656,d28516746773bfaeca4efa5537c0bf5990b8828e@65.21.229.33:27656,f467e286567f94c89d39a5bcea0e1d68951299f9@146.59.81.204:34456,d3a8fdbe6776fc71998fa893abcd634461b52b19@65.109.92.241:40106,6d8c83cc702365363b829a14efdd414401da369b@23.88.69.167:27565,c126eed9cfede7802d78f570fec8175835309a73@141.95.127.146:26656,12703ce9efe6c1171c193dae2e2041a2be610852@65.108.44.149:29656,9832950578c4492d934d6e875165757f5a98caff@51.83.96.150:26637,2f6b34ad97c4827dace87436f0299cf89fe0c056@136.243.95.80:46656,f2483e5af4cb1fab55e4f6422627c0365f45b5dd@194.163.188.252:26656,eeca453e3a1cf670c78e2255b8f0bd5a9443c30b@65.108.225.71:26656,ce38728ac38ebbb4a72d496d42f8e9030af441d7@162.19.137.25:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.rebusd/config/config.toml
```
