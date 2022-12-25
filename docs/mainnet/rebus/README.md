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
peers="f546370843f92e2415524a7b18f9cd528e2fd706@65.109.55.186:26656,a35d28e111c1dcc1e5f3203627b449adfb4425f2@65.109.29.150:21656,b574e11e103058a121cc03d1c4d9867ba3daed34@135.181.139.113:31656,1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,dda7abe32cc84a722cf6b1d2ee3b61ebe7ad71df@135.181.212.183:21656,6ad5dd14c578016cc7bc4d7c6d6f7f773bba39af@65.109.60.57:26656,4a4d2e7070e05ad6c13628d2f191d96172659452@65.109.65.210:40656,5f29f14fe3dd7e1d86caa4d344e67ee81c32255f@65.109.37.228:26656,4e2a874e538319f204f03751a5e458d0371d5b92@65.108.98.125:60556,d3a8fdbe6776fc71998fa893abcd634461b52b19@65.109.92.241:40106,30ff8100fefac53ee40ef7631f1a3c66ca2b82cf@135.181.164.90:26656,404ae118865c1485f7859fa2c7cc2e3b8c402a14@51.75.135.34:26656,a7d96dc929824613315dcc1c90fee119f28cc51f@164.152.160.207:26656,89757803f40da51678451735445ad40d5b15e059@169.155.44.106:26656,3cc5fb5f6140ac4e57dfc80940c8a06daa299c89@51.77.195.46:26656,2f6b34ad97c4827dace87436f0299cf89fe0c056@136.243.95.80:46656,b1b08fe470551dca6d6631fb1bfabb814f6c1aec@54.37.129.164:54556,6daeb8cfea285f561e167a0d94718b61e2cf7944@5.189.187.36:21656,17779ded6b3dc2f31d6c6f40cc6f07d802753ba7@78.47.153.128:26656,ae67d4c37632435e0d5f27041f50af20d227bdc2@93.170.72.118:21656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,6ac55af662061d3669d7c70961a8fd87ba2f2075@65.108.200.142:26696,f2483e5af4cb1fab55e4f6422627c0365f45b5dd@194.163.188.252:26656,3a3e7123b9ae814b8d8517b6635d21b9ae45bf25@195.3.222.148:26656,b8137c688096d1abcf56942d335d061f212e6629@62.212.65.138:34656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.16:26656,e056318da91e77585f496333040e00e12f6941d1@51.83.97.166:26656,5a13200e67f6cb5385d9d8f8c68a7b5e62f8cd54@188.34.176.96:26656,1e19e8668693863bf573c61f1a83523bf661f9ad@38.242.242.99:26656,1f7c31506f465c5f5536862074e98fc7a6043d4c@65.108.13.212:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.rebusd/config/config.toml
```
