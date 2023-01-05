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

**live-peers** (31)
```
peers="d28516746773bfaeca4efa5537c0bf5990b8828e@65.21.229.33:27656,36afb1c827f52d38d7cd328b384d644b531b5997@65.108.238.102:17256,9d17d1c5b5d3b8c9e7ffab264b45b5dd979116f3@65.109.24.188:26656,18ec83c4e3938aec31a3a32154969107739f0b81@135.181.153.228:26656,6ac55af662061d3669d7c70961a8fd87ba2f2075@65.108.200.142:26696,641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,d3a8fdbe6776fc71998fa893abcd634461b52b19@65.109.92.241:40106,5f29f14fe3dd7e1d86caa4d344e67ee81c32255f@65.109.37.228:26656,703714c82c94fc1c74b6ee0d1fc3417b932be5f3@134.65.192.98:26656,4e3e545e85000045ef44905ab683a5db6f87cdbe@88.198.32.17:37656,57f475bb44fc6f121790d523ce06fb4e0ad9ab69@141.95.65.73:17256,e056318da91e77585f496333040e00e12f6941d1@51.83.97.166:26656,3cc5fb5f6140ac4e57dfc80940c8a06daa299c89@51.77.195.46:26656,ea5e7a6b9a5c18c6455e7a8c583c129c5821a452@51.178.80.111:26656,a3d975c913570ad217d9a3de01a8616ad5ce20f8@142.132.128.137:26656,0fedf7695d9e2721663c1d573d6d81a14c21533e@65.21.90.137:12856,b570827e4397512e077028ea7121d3e19eb25bab@85.10.200.221:26656,34e3178b6e0f25451fd690c15fc199d5a9bdfb9b@15.204.197.11:26656,b1b08fe470551dca6d6631fb1bfabb814f6c1aec@54.37.129.164:54556,3a378fbfae33a593b913371c876c9d275c0abb12@213.239.215.77:26656,1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,056d6a61c8a4c5ccb02123d67a013434423f155a@149.102.142.57:26656,1e19e8668693863bf573c61f1a83523bf661f9ad@38.242.242.99:26656,4a4d2e7070e05ad6c13628d2f191d96172659452@65.109.65.210:40656,12703ce9efe6c1171c193dae2e2041a2be610852@65.108.44.149:29656,b8613a7717b0ebaf2100c360cf13c92c4de33100@195.201.63.87:41666,6ad5dd14c578016cc7bc4d7c6d6f7f773bba39af@65.109.60.57:26656,10eb2d456219ea712c696251ddf231bbec6d987c@65.109.37.58:15656,f4ad005ee8ec25508c498294e9e83d81b188ea49@185.248.24.16:21656,92245ff5c7a4b293d2f0c7f9afca0ddad2e0fb52@65.108.244.178:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.rebusd/config/config.toml
```
