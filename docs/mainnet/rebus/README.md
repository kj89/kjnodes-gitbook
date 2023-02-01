# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/rebus.png" width="150" alt=""><figcaption></figcaption></figure>

Rebuschain is a platform that will provide DeFi (Decentralized Finance)  investment opportunities to traditional investors clearly and conveniently

**Chain ID**: reb_1111-1 | **Latest Version Tag**: v0.2.0 | **Wasm**: OFF

[Website](https://www.rebuschain.com) | [Discord](https://discord.gg/rebuschain) | [Twitter](https://twitter.com/RebusChain)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/rebus/rebusvaloper1vndzy8y55ylgpmmsc34uy8rm6kqlml6ffs9lrv)

## Restake

[Restake with kjnodes](https://restake.app/rebus/rebusvaloper1vndzy8y55ylgpmmsc34uy8rm6kqlml6ffs9lrv) (every day at 08:00, 20:00)
## Chain explorer
[https://explorer.kjnodes.com/rebus](https://explorer.kjnodes.com/rebus)

## Public endpoints

* api: [https://rebus.api.kjnodes.com](https://rebus.api.kjnodes.com)
* rpc: [https://rebus.rpc.kjnodes.com](https://rebus.rpc.kjnodes.com)
* grpc: [https://rebus.grpc.kjnodes.com](https://rebus.grpc.kjnodes.com)

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

**live-peers** (30)
```bash
peers="256d9790bf186f5a275790f7fe01e1b8800dcaaf@65.21.88.78:26656,275d2614d24c8ac015a7712702fcb99cef67ef67@65.108.124.219:29656,12703ce9efe6c1171c193dae2e2041a2be610852@65.108.44.149:29656,30ff8100fefac53ee40ef7631f1a3c66ca2b82cf@135.181.164.90:26656,ff7031f45a97600076f72b9318167e3dfcd2a17e@65.21.136.170:52656,07b84cf4b47a2e5ad251267716fe05bcf30330cd@65.21.170.3:29656,87102b5dd22c1d17f97197c078f23726ae3c6214@91.157.60.253:26656,92245ff5c7a4b293d2f0c7f9afca0ddad2e0fb52@65.108.244.178:26656,e6f1684ed8ed5c586b188bf7088026da4ffdaff6@134.65.193.78:26656,faf349e185255c4aa2786da4f8ac70ea13849db0@169.155.45.128:26656,afdd27b58e851dcbb8c98c0e3191a0d8bfbcd3ae@65.108.41.252:26656,c124ce0b508e8b9ed1c5b6957f362225659b5343@134.65.192.98:26656,ce38728ac38ebbb4a72d496d42f8e9030af441d7@162.19.137.25:26656,ff7621be29e39e9fdf07f2501e1a217201ca29ee@213.239.207.175:39656,8f023504e27873141164b6fbf1c4b788ff8d533b@159.69.200.24:26656,69e27ab9b46350654805df3ea8d9ac2f00af4e4c@38.242.244.85:26656,0fedf7695d9e2721663c1d573d6d81a14c21533e@65.21.90.137:12856,237bfc05da5f8cabee00f148995333f37186d232@164.68.121.101:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,17779ded6b3dc2f31d6c6f40cc6f07d802753ba7@78.47.153.128:26656,49e084a4c77f168810608e20b530ee9d25ac69b7@209.126.8.176:26656,6ac55af662061d3669d7c70961a8fd87ba2f2075@65.108.200.142:26696,4a4d2e7070e05ad6c13628d2f191d96172659452@65.109.65.210:40656,6d8c83cc702365363b829a14efdd414401da369b@23.88.69.167:27565,18ec83c4e3938aec31a3a32154969107739f0b81@135.181.153.228:26656,d28516746773bfaeca4efa5537c0bf5990b8828e@65.21.229.33:27656,ae67d4c37632435e0d5f27041f50af20d227bdc2@93.170.72.118:21656,ab6a4ae2857ac05fa8f45b03871fa3945193fc61@46.4.81.204:35656,1749a8f0aa533fc92c1212366c22c0993fbb1545@51.178.47.116:26656,5c2018214fcfde67ec390702539f295165f12a3a@86.48.2.20:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
