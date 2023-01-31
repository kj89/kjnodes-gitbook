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
peers="fa292bfad37826c9da43894b349b1480dff516b5@65.108.99.254:31656,30ff8100fefac53ee40ef7631f1a3c66ca2b82cf@135.181.164.90:26656,1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,10eb2d456219ea712c696251ddf231bbec6d987c@65.109.37.58:15656,7ee74ea68e350fc5214657255cba5e339bb30c2a@138.201.127.91:26674,12703ce9efe6c1171c193dae2e2041a2be610852@65.108.44.149:29656,f546370843f92e2415524a7b18f9cd528e2fd706@65.109.55.186:26656,12e6bea6650a53150c01ca3897e4a0b94d6e9d4e@135.181.141.47:26656,e056318da91e77585f496333040e00e12f6941d1@51.83.97.166:26656,e6f1684ed8ed5c586b188bf7088026da4ffdaff6@134.65.193.78:26656,faf349e185255c4aa2786da4f8ac70ea13849db0@169.155.45.128:26656,17779ded6b3dc2f31d6c6f40cc6f07d802753ba7@78.47.153.128:26656,2f6b34ad97c4827dace87436f0299cf89fe0c056@136.243.95.80:46656,1fe32d8f09b8715b1e626da17b3ecfe26623b371@176.9.22.117:27656,237bfc05da5f8cabee00f148995333f37186d232@164.68.121.101:26656,5c2018214fcfde67ec390702539f295165f12a3a@86.48.2.20:26656,b8137c688096d1abcf56942d335d061f212e6629@62.212.65.138:34656,f4ad005ee8ec25508c498294e9e83d81b188ea49@185.248.24.16:21656,05483a7ec0160b17de1ad8e7793c7502e70e5525@146.59.85.223:17256,89ded0a3987d22e46b756fead439e2a4d25f23cb@185.144.99.30:26656,afdd27b58e851dcbb8c98c0e3191a0d8bfbcd3ae@65.108.41.252:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.16:26656,4e3e545e85000045ef44905ab683a5db6f87cdbe@88.198.32.17:37656,5f29f14fe3dd7e1d86caa4d344e67ee81c32255f@65.109.37.228:26656,34e3178b6e0f25451fd690c15fc199d5a9bdfb9b@15.204.197.11:26656,87102b5dd22c1d17f97197c078f23726ae3c6214@91.157.60.253:26656,a7d96dc929824613315dcc1c90fee119f28cc51f@164.152.160.207:26656,cd71aa366822800a2aa7051fae69127f78b3f203@188.165.225.226:26656,275d2614d24c8ac015a7712702fcb99cef67ef67@65.108.124.219:29656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
