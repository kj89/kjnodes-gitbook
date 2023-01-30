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
peers="30ff8100fefac53ee40ef7631f1a3c66ca2b82cf@135.181.164.90:26656,b5bf2242c981371224e5e9e89d6c265d554c8989@65.21.202.154:21656,256d9790bf186f5a275790f7fe01e1b8800dcaaf@65.21.88.78:26656,10eb2d456219ea712c696251ddf231bbec6d987c@65.109.37.58:15656,ff7621be29e39e9fdf07f2501e1a217201ca29ee@213.239.207.175:39656,6d8c83cc702365363b829a14efdd414401da369b@23.88.69.167:27565,92245ff5c7a4b293d2f0c7f9afca0ddad2e0fb52@65.108.244.178:26656,89757803f40da51678451735445ad40d5b15e059@169.155.44.106:26656,b1b08fe470551dca6d6631fb1bfabb814f6c1aec@54.37.129.164:54556,8f023504e27873141164b6fbf1c4b788ff8d533b@159.69.200.24:26656,1fe32d8f09b8715b1e626da17b3ecfe26623b371@176.9.22.117:27656,b8613a7717b0ebaf2100c360cf13c92c4de33100@195.201.63.87:41666,2f6b34ad97c4827dace87436f0299cf89fe0c056@136.243.95.80:46656,e056318da91e77585f496333040e00e12f6941d1@51.83.97.166:26656,34e3178b6e0f25451fd690c15fc199d5a9bdfb9b@15.204.197.11:26656,4a4d2e7070e05ad6c13628d2f191d96172659452@65.109.65.210:40656,ae67d4c37632435e0d5f27041f50af20d227bdc2@93.170.72.118:21656,a3d975c913570ad217d9a3de01a8616ad5ce20f8@142.132.128.137:26656,1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,ce38728ac38ebbb4a72d496d42f8e9030af441d7@162.19.137.25:26656,b8c42fcb311b47cdb8285b5697f661fbba5bf1a5@51.68.157.129:26656,18ec83c4e3938aec31a3a32154969107739f0b81@135.181.153.228:26656,17779ded6b3dc2f31d6c6f40cc6f07d802753ba7@78.47.153.128:26656,bb2a7dc81b9bd0e017409a2bbb71b12bb899e743@178.63.22.117:26656,eeca453e3a1cf670c78e2255b8f0bd5a9443c30b@65.108.225.71:26656,05483a7ec0160b17de1ad8e7793c7502e70e5525@146.59.85.223:17256,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,12703ce9efe6c1171c193dae2e2041a2be610852@65.108.44.149:29656,b570827e4397512e077028ea7121d3e19eb25bab@85.10.200.221:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
