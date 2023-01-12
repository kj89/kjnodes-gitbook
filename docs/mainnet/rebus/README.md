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

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@rebus.rpc.kjnodes.com:21656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@rebus.rpc.kjnodes.com:21659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/rebus/addrbook.json > $HOME/.rebusd/config/addrbook.json
```

**live-peers** (29)
```bash
peers="5f29f14fe3dd7e1d86caa4d344e67ee81c32255f@65.109.37.228:26656,5fb9952f3eaeb5be3aab37425831c2a4830a019d@65.21.133.125:29656,1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,a35d28e111c1dcc1e5f3203627b449adfb4425f2@65.109.29.150:21656,12e6bea6650a53150c01ca3897e4a0b94d6e9d4e@135.181.141.47:26656,ad116a3f497ebb37ac14226c22a1483237a224ac@65.108.229.102:23656,9d17d1c5b5d3b8c9e7ffab264b45b5dd979116f3@65.109.24.188:26656,4a4d2e7070e05ad6c13628d2f191d96172659452@65.109.65.210:40656,89757803f40da51678451735445ad40d5b15e059@169.155.44.106:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.16:26656,ff7031f45a97600076f72b9318167e3dfcd2a17e@65.21.136.170:52656,b8137c688096d1abcf56942d335d061f212e6629@62.212.65.138:34656,69e27ab9b46350654805df3ea8d9ac2f00af4e4c@38.242.244.85:26656,c0b33353fb70d8d71dcb9c8848b3b4207bd56951@94.23.207.45:30547,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,256d9790bf186f5a275790f7fe01e1b8800dcaaf@65.21.88.78:26656,12703ce9efe6c1171c193dae2e2041a2be610852@65.108.44.149:29656,170397e75ca2b0f4e9f3b1bb5d0d23f9b10f01c7@94.23.23.189:30544,d12f9b52ca0e11cdeca5c46e802249ade4c39c45@185.248.24.40:26656,d28516746773bfaeca4efa5537c0bf5990b8828e@65.21.229.33:27656,056d6a61c8a4c5ccb02123d67a013434423f155a@149.102.142.57:26656,1e19e8668693863bf573c61f1a83523bf661f9ad@38.242.242.99:26656,eeca453e3a1cf670c78e2255b8f0bd5a9443c30b@65.108.225.71:26656,17779ded6b3dc2f31d6c6f40cc6f07d802753ba7@78.47.153.128:26656,7ee74ea68e350fc5214657255cba5e339bb30c2a@138.201.127.91:26674,237bfc05da5f8cabee00f148995333f37186d232@164.68.121.101:26656,18ec83c4e3938aec31a3a32154969107739f0b81@135.181.153.228:26656,10eb2d456219ea712c696251ddf231bbec6d987c@65.109.37.58:15656,6d8c83cc702365363b829a14efdd414401da369b@23.88.69.167:27565"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
