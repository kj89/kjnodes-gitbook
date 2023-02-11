# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/rebus.png" width="150" alt=""><figcaption></figcaption></figure>

Rebuschain is a platform that will provide DeFi (Decentralized Finance)  investment opportunities to traditional investors clearly and conveniently

**Chain ID**: reb_1111-1 | **Latest Version Tag**: v0.3.0 | **Wasm**: OFF

[Website](https://www.rebuschain.com) | [Discord](https://discord.gg/rebuschain) | [Twitter](https://twitter.com/RebusChain)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/rebus/rebusvaloper1vndzy8y55ylgpmmsc34uy8rm6kqlml6ffs9lrv)

## Restake

[Restake with kjnodes](https://restake.app/rebus/rebusvaloper1vndzy8y55ylgpmmsc34uy8rm6kqlml6ffs9lrv) (every 5 minutes)
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
peers="237bfc05da5f8cabee00f148995333f37186d232@164.68.121.101:26656,641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,275d2614d24c8ac015a7712702fcb99cef67ef67@65.108.124.219:29656,07b84cf4b47a2e5ad251267716fe05bcf30330cd@65.21.170.3:29656,1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,d3a8fdbe6776fc71998fa893abcd634461b52b19@65.109.92.241:40106,fa292bfad37826c9da43894b349b1480dff516b5@65.108.99.254:31656,89757803f40da51678451735445ad40d5b15e059@169.155.44.106:26656,faf349e185255c4aa2786da4f8ac70ea13849db0@169.155.45.128:26656,c126eed9cfede7802d78f570fec8175835309a73@141.95.127.146:26656,b570827e4397512e077028ea7121d3e19eb25bab@85.10.200.221:26656,ab6a4ae2857ac05fa8f45b03871fa3945193fc61@46.4.81.204:35656,3e319c765b7b48d518a2e3218efc317234b81681@142.132.159.188:26656,b8137c688096d1abcf56942d335d061f212e6629@62.212.65.138:34656,05483a7ec0160b17de1ad8e7793c7502e70e5525@146.59.85.223:17256,b1b08fe470551dca6d6631fb1bfabb814f6c1aec@54.37.129.164:54556,f4ad005ee8ec25508c498294e9e83d81b188ea49@185.248.24.16:21656,89ded0a3987d22e46b756fead439e2a4d25f23cb@185.144.99.30:26656,ebc4d27be0c87f537b44250c2e22ad349dc59fb6@158.69.116.134:26656,1749a8f0aa533fc92c1212366c22c0993fbb1545@51.178.47.116:26656,a7d96dc929824613315dcc1c90fee119f28cc51f@164.152.160.207:26656,2b7c9ae046c35b48cb7d3d16416c3f36ab648f66@149.102.136.149:26656,ce38728ac38ebbb4a72d496d42f8e9030af441d7@162.19.137.25:26656,92245ff5c7a4b293d2f0c7f9afca0ddad2e0fb52@65.108.244.178:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.16:26656,6daeb8cfea285f561e167a0d94718b61e2cf7944@5.189.187.36:21656,87102b5dd22c1d17f97197c078f23726ae3c6214@91.157.60.253:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,49e084a4c77f168810608e20b530ee9d25ac69b7@209.126.8.176:26656,256d9790bf186f5a275790f7fe01e1b8800dcaaf@65.21.88.78:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
