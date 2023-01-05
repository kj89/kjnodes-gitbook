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
peers="5f29f14fe3dd7e1d86caa4d344e67ee81c32255f@65.109.37.228:26656,12703ce9efe6c1171c193dae2e2041a2be610852@65.108.44.149:29656,d28516746773bfaeca4efa5537c0bf5990b8828e@65.21.229.33:27656,641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,6ac55af662061d3669d7c70961a8fd87ba2f2075@65.108.200.142:26696,10eb2d456219ea712c696251ddf231bbec6d987c@65.109.37.58:15656,eeca453e3a1cf670c78e2255b8f0bd5a9443c30b@65.108.225.71:26656,ea5e7a6b9a5c18c6455e7a8c583c129c5821a452@51.178.80.111:26656,1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,404ae118865c1485f7859fa2c7cc2e3b8c402a14@51.75.135.34:26656,89757803f40da51678451735445ad40d5b15e059@169.155.44.106:26656,b570827e4397512e077028ea7121d3e19eb25bab@85.10.200.221:26656,e056318da91e77585f496333040e00e12f6941d1@51.83.97.166:26656,2f6b34ad97c4827dace87436f0299cf89fe0c056@136.243.95.80:46656,bb2a7dc81b9bd0e017409a2bbb71b12bb899e743@178.63.22.117:26656,237bfc05da5f8cabee00f148995333f37186d232@164.68.121.101:26656,b8c42fcb311b47cdb8285b5697f661fbba5bf1a5@51.68.157.129:26656,ae67d4c37632435e0d5f27041f50af20d227bdc2@93.170.72.118:21656,34e3178b6e0f25451fd690c15fc199d5a9bdfb9b@15.204.197.11:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.16:26656,d3a8fdbe6776fc71998fa893abcd634461b52b19@65.109.92.241:40106,a3d975c913570ad217d9a3de01a8616ad5ce20f8@142.132.128.137:26656,98206a8f71578850f1d88f08ede96ebc7e7c76a9@176.9.188.21:52656,4a4d2e7070e05ad6c13628d2f191d96172659452@65.109.65.210:40656,ad116a3f497ebb37ac14226c22a1483237a224ac@65.108.229.102:23656,6ad5dd14c578016cc7bc4d7c6d6f7f773bba39af@65.109.60.57:26656,1e19e8668693863bf573c61f1a83523bf661f9ad@38.242.242.99:26656,3e319c765b7b48d518a2e3218efc317234b81681@142.132.159.188:26656,b5bf2242c981371224e5e9e89d6c265d554c8989@65.21.202.154:21656,a35d28e111c1dcc1e5f3203627b449adfb4425f2@65.109.29.150:21656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.rebusd/config/config.toml
```
