# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/rebus.png" width="150" alt=""><figcaption></figcaption></figure>

Rebuschain is a platform that will provide DeFi (Decentralized Finance)  investment opportunities to traditional investors clearly and conveniently

**Chain ID**: reb_1111-1 | **Latest Version Tag**: v0.2.0 | **Wasm**: OFF

[Website](https://www.rebuschain.com) | [Discord](https://discord.gg/rebuschain) | [Twitter](https://twitter.com/RebusChain)

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

**live-peers** (29)
```bash
peers="a35d28e111c1dcc1e5f3203627b449adfb4425f2@65.109.29.150:21656,1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,5f29f14fe3dd7e1d86caa4d344e67ee81c32255f@65.109.37.228:26656,256d9790bf186f5a275790f7fe01e1b8800dcaaf@65.21.88.78:26656,10eb2d456219ea712c696251ddf231bbec6d987c@65.109.37.58:15656,641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,8f023504e27873141164b6fbf1c4b788ff8d533b@159.69.200.24:26656,17779ded6b3dc2f31d6c6f40cc6f07d802753ba7@78.47.153.128:26656,c124ce0b508e8b9ed1c5b6957f362225659b5343@134.65.192.98:26656,e056318da91e77585f496333040e00e12f6941d1@51.83.97.166:26656,b570827e4397512e077028ea7121d3e19eb25bab@85.10.200.221:26656,a3d975c913570ad217d9a3de01a8616ad5ce20f8@142.132.128.137:26656,ab6a4ae2857ac05fa8f45b03871fa3945193fc61@46.4.81.204:35656,4a4d2e7070e05ad6c13628d2f191d96172659452@65.109.65.210:40656,b8137c688096d1abcf56942d335d061f212e6629@62.212.65.138:34656,05483a7ec0160b17de1ad8e7793c7502e70e5525@146.59.85.223:17256,6daeb8cfea285f561e167a0d94718b61e2cf7944@5.189.187.36:21656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,ff7621be29e39e9fdf07f2501e1a217201ca29ee@213.239.207.175:39656,ff7031f45a97600076f72b9318167e3dfcd2a17e@65.21.136.170:52656,57f475bb44fc6f121790d523ce06fb4e0ad9ab69@141.95.65.73:17256,f546370843f92e2415524a7b18f9cd528e2fd706@65.109.55.186:26656,36afb1c827f52d38d7cd328b384d644b531b5997@65.108.238.102:17256,34e3178b6e0f25451fd690c15fc199d5a9bdfb9b@15.204.197.11:26656,ce38728ac38ebbb4a72d496d42f8e9030af441d7@162.19.137.25:26656,d28516746773bfaeca4efa5537c0bf5990b8828e@65.21.229.33:27656,f4ad005ee8ec25508c498294e9e83d81b188ea49@185.248.24.16:21656,b8c42fcb311b47cdb8285b5697f661fbba5bf1a5@51.68.157.129:26656,d3a8fdbe6776fc71998fa893abcd634461b52b19@65.109.92.241:40106"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
