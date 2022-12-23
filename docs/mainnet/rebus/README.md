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

**live-peers** (29)
```
peers="d28516746773bfaeca4efa5537c0bf5990b8828e@65.21.229.33:27656,4a4d2e7070e05ad6c13628d2f191d96172659452@65.109.65.210:40656,dda7abe32cc84a722cf6b1d2ee3b61ebe7ad71df@135.181.212.183:21656,30ff8100fefac53ee40ef7631f1a3c66ca2b82cf@135.181.164.90:26656,1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,07b84cf4b47a2e5ad251267716fe05bcf30330cd@65.21.170.3:29656,ce38728ac38ebbb4a72d496d42f8e9030af441d7@162.19.137.25:26656,3cc5fb5f6140ac4e57dfc80940c8a06daa299c89@51.77.195.46:26656,b8137c688096d1abcf56942d335d061f212e6629@62.212.65.138:34656,8f023504e27873141164b6fbf1c4b788ff8d533b@159.69.200.24:26656,e056318da91e77585f496333040e00e12f6941d1@51.83.97.166:26656,b570827e4397512e077028ea7121d3e19eb25bab@85.10.200.221:26656,1fe32d8f09b8715b1e626da17b3ecfe26623b371@176.9.22.117:27656,77ca73199cf0a73ab52fc216d8ab8f8756275fef@138.201.8.248:52656,5a13200e67f6cb5385d9d8f8c68a7b5e62f8cd54@188.34.176.96:26656,b1b08fe470551dca6d6631fb1bfabb814f6c1aec@54.37.129.164:54556,6daeb8cfea285f561e167a0d94718b61e2cf7944@5.189.187.36:21656,c0b33353fb70d8d71dcb9c8848b3b4207bd56951@94.23.207.45:30547,237bfc05da5f8cabee00f148995333f37186d232@164.68.121.101:26656,12703ce9efe6c1171c193dae2e2041a2be610852@65.108.44.149:29656,2b7c9ae046c35b48cb7d3d16416c3f36ab648f66@149.102.136.149:26656,6ac55af662061d3669d7c70961a8fd87ba2f2075@65.108.200.142:26696,5c2018214fcfde67ec390702539f295165f12a3a@86.48.2.20:26656,ae67d4c37632435e0d5f27041f50af20d227bdc2@93.170.72.118:21656,69e27ab9b46350654805df3ea8d9ac2f00af4e4c@38.242.244.85:26656,6ad5dd14c578016cc7bc4d7c6d6f7f773bba39af@65.109.60.57:26656,1f7c31506f465c5f5536862074e98fc7a6043d4c@65.108.13.212:26656,12e6bea6650a53150c01ca3897e4a0b94d6e9d4e@135.181.141.47:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.rebusd/config/config.toml
```
