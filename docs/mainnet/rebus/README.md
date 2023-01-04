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

**live-peers** (28)
```
peers="5f29f14fe3dd7e1d86caa4d344e67ee81c32255f@65.109.37.228:26656,36afb1c827f52d38d7cd328b384d644b531b5997@65.108.238.102:17256,ad116a3f497ebb37ac14226c22a1483237a224ac@65.108.229.102:23656,4a4d2e7070e05ad6c13628d2f191d96172659452@65.109.65.210:40656,30ff8100fefac53ee40ef7631f1a3c66ca2b82cf@135.181.164.90:26656,9d17d1c5b5d3b8c9e7ffab264b45b5dd979116f3@65.109.24.188:26656,1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,5fb9952f3eaeb5be3aab37425831c2a4830a019d@65.21.133.125:29656,12703ce9efe6c1171c193dae2e2041a2be610852@65.108.44.149:29656,ce38728ac38ebbb4a72d496d42f8e9030af441d7@162.19.137.25:26656,a3d975c913570ad217d9a3de01a8616ad5ce20f8@142.132.128.137:26656,b570827e4397512e077028ea7121d3e19eb25bab@85.10.200.221:26656,3cc5fb5f6140ac4e57dfc80940c8a06daa299c89@51.77.195.46:26656,b8137c688096d1abcf56942d335d061f212e6629@62.212.65.138:34656,0fedf7695d9e2721663c1d573d6d81a14c21533e@65.21.90.137:12856,cd71aa366822800a2aa7051fae69127f78b3f203@188.165.225.226:26656,fa292bfad37826c9da43894b349b1480dff516b5@65.108.99.254:31656,b8c42fcb311b47cdb8285b5697f661fbba5bf1a5@51.68.157.129:26656,6daeb8cfea285f561e167a0d94718b61e2cf7944@5.189.187.36:21656,f546370843f92e2415524a7b18f9cd528e2fd706@65.109.55.186:26656,17779ded6b3dc2f31d6c6f40cc6f07d802753ba7@78.47.153.128:26656,6ad5dd14c578016cc7bc4d7c6d6f7f773bba39af@65.109.60.57:26656,6ac55af662061d3669d7c70961a8fd87ba2f2075@65.108.200.142:26696,d28516746773bfaeca4efa5537c0bf5990b8828e@65.21.229.33:27656,2f6b34ad97c4827dace87436f0299cf89fe0c056@136.243.95.80:46656,ae67d4c37632435e0d5f27041f50af20d227bdc2@93.170.72.118:21656,98206a8f71578850f1d88f08ede96ebc7e7c76a9@176.9.188.21:52656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.rebusd/config/config.toml
```
