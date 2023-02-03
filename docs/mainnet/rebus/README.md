# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/rebus.png" width="150" alt=""><figcaption></figcaption></figure>

Rebuschain is a platform that will provide DeFi (Decentralized Finance)  investment opportunities to traditional investors clearly and conveniently

**Chain ID**: reb_1111-1 | **Latest Version Tag**: v0.3.0 | **Wasm**: OFF

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
peers="5fb9952f3eaeb5be3aab37425831c2a4830a019d@65.21.133.125:29656,0fedf7695d9e2721663c1d573d6d81a14c21533e@65.21.90.137:12856,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,7196b111260698b8b6ba8ea64c3af0444fb365c8@195.201.63.87:41656,e6f1684ed8ed5c586b188bf7088026da4ffdaff6@134.65.193.78:26656,fa292bfad37826c9da43894b349b1480dff516b5@65.108.99.254:31656,faf349e185255c4aa2786da4f8ac70ea13849db0@169.155.45.128:26656,a7d96dc929824613315dcc1c90fee119f28cc51f@164.152.160.207:26656,4e3e545e85000045ef44905ab683a5db6f87cdbe@88.198.32.17:37656,f546370843f92e2415524a7b18f9cd528e2fd706@65.109.55.186:26656,49e084a4c77f168810608e20b530ee9d25ac69b7@209.126.8.176:26656,4a4d2e7070e05ad6c13628d2f191d96172659452@65.109.65.210:40656,7ee74ea68e350fc5214657255cba5e339bb30c2a@138.201.127.91:26674,05483a7ec0160b17de1ad8e7793c7502e70e5525@146.59.85.223:17256,d3a8fdbe6776fc71998fa893abcd634461b52b19@65.109.92.241:40106,07b84cf4b47a2e5ad251267716fe05bcf30330cd@65.21.170.3:29656,3e319c765b7b48d518a2e3218efc317234b81681@142.132.159.188:26656,2b7c9ae046c35b48cb7d3d16416c3f36ab648f66@149.102.136.149:26656,b1dcbb37514fbe215be54079e71aa39dac7fd0ae@64.5.123.203:26656,b8c42fcb311b47cdb8285b5697f661fbba5bf1a5@51.68.157.129:26656,18ec83c4e3938aec31a3a32154969107739f0b81@135.181.153.228:26656,ab6a4ae2857ac05fa8f45b03871fa3945193fc61@46.4.81.204:35656,b1b08fe470551dca6d6631fb1bfabb814f6c1aec@54.37.129.164:54556,09d22b9fc1b07f3e2f64b685ab6f28130bc2edd2@51.89.7.185:26637,237bfc05da5f8cabee00f148995333f37186d232@164.68.121.101:26656,d12f9b52ca0e11cdeca5c46e802249ade4c39c45@185.248.24.40:26656,12e6bea6650a53150c01ca3897e4a0b94d6e9d4e@135.181.141.47:26656,30ff8100fefac53ee40ef7631f1a3c66ca2b82cf@135.181.164.90:26656,678ded952968137c8ded8aeada337662065f1507@159.203.162.120:26656,304ff8e051b2fbd038771142b69ac915c14c0819@78.46.78.83:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
