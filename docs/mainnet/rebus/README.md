# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/rebus.png" width="150" alt=""><figcaption></figcaption></figure>

Rebuschain is a platform that will provide DeFi (Decentralized Finance)  investment opportunities to traditional investors clearly and conveniently

**Chain ID**: reb_1111-1 | **Latest Version Tag**: v0.2.0 | **Wasm**: OFF

[Website](https://www.rebuschain.com) | [Discord](https://discord.gg/rebuschain) | [Twitter](https://twitter.com/RebusChain)

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
peers="ff7031f45a97600076f72b9318167e3dfcd2a17e@65.21.136.170:52656,d28516746773bfaeca4efa5537c0bf5990b8828e@65.21.229.33:27656,12e6bea6650a53150c01ca3897e4a0b94d6e9d4e@135.181.141.47:26656,12703ce9efe6c1171c193dae2e2041a2be610852@65.108.44.149:29656,6ad5dd14c578016cc7bc4d7c6d6f7f773bba39af@65.109.60.57:26656,b5bf2242c981371224e5e9e89d6c265d554c8989@65.21.202.154:21656,4a4d2e7070e05ad6c13628d2f191d96172659452@65.109.65.210:40656,dda7abe32cc84a722cf6b1d2ee3b61ebe7ad71df@135.181.212.183:21656,056d6a61c8a4c5ccb02123d67a013434423f155a@149.102.142.57:26656,17779ded6b3dc2f31d6c6f40cc6f07d802753ba7@78.47.153.128:26656,8f023504e27873141164b6fbf1c4b788ff8d533b@159.69.200.24:26656,3cc5fb5f6140ac4e57dfc80940c8a06daa299c89@51.77.195.46:26656,e056318da91e77585f496333040e00e12f6941d1@51.83.97.166:26656,a3d975c913570ad217d9a3de01a8616ad5ce20f8@142.132.128.137:26656,6d8c83cc702365363b829a14efdd414401da369b@23.88.69.167:27565,0fedf7695d9e2721663c1d573d6d81a14c21533e@65.21.90.137:12856,b8137c688096d1abcf56942d335d061f212e6629@62.212.65.138:34656,b8c42fcb311b47cdb8285b5697f661fbba5bf1a5@51.68.157.129:26656,a35d28e111c1dcc1e5f3203627b449adfb4425f2@65.109.29.150:21656,6daeb8cfea285f561e167a0d94718b61e2cf7944@5.189.187.36:21656,69e27ab9b46350654805df3ea8d9ac2f00af4e4c@38.242.244.85:26656,eeca453e3a1cf670c78e2255b8f0bd5a9443c30b@65.108.225.71:26656,1749a8f0aa533fc92c1212366c22c0993fbb1545@51.178.47.116:26656,afdd27b58e851dcbb8c98c0e3191a0d8bfbcd3ae@65.108.41.252:26656,170397e75ca2b0f4e9f3b1bb5d0d23f9b10f01c7@94.23.23.189:30544,89757803f40da51678451735445ad40d5b15e059@169.155.44.106:26656,3e319c765b7b48d518a2e3218efc317234b81681@142.132.159.188:26656,237bfc05da5f8cabee00f148995333f37186d232@164.68.121.101:26656,b1b08fe470551dca6d6631fb1bfabb814f6c1aec@54.37.129.164:54556,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.rebusd/config/config.toml
```
