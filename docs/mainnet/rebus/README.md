# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/rebus.png" width="150" alt=""><figcaption></figcaption></figure>

Rebuschain is a platform that will provide DeFi (Decentralized Finance)  investment opportunities to traditional investors clearly and conveniently

**Chain ID**: reb_1111-1 | **Latest Version Tag**: v0.2.0 | **Wasm**: OFF

[Website](https://www.rebuschain.com) | [Discord](https://discord.gg/rebuschain) | [Twitter](https://twitter.com/RebusChain)

## Restake

[Restake with kjnodes](https://restake.app/rebus/rebusvaloper1vndzy8y55ylgpmmsc34uy8rm6kqlml6ffs9lrv) (every day at 08:00, 20:00)
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

**live-peers** (28)
```bash
peers="256d9790bf186f5a275790f7fe01e1b8800dcaaf@65.21.88.78:26656,30ff8100fefac53ee40ef7631f1a3c66ca2b82cf@135.181.164.90:26656,346bf012c17fa30ef70ae72f082374838626532a@65.108.106.131:26696,a35d28e111c1dcc1e5f3203627b449adfb4425f2@65.109.29.150:21656,12703ce9efe6c1171c193dae2e2041a2be610852@65.108.44.149:29656,d3a8fdbe6776fc71998fa893abcd634461b52b19@65.109.92.241:40106,275d2614d24c8ac015a7712702fcb99cef67ef67@65.108.124.219:29656,4e3e545e85000045ef44905ab683a5db6f87cdbe@88.198.32.17:37656,f546370843f92e2415524a7b18f9cd528e2fd706@65.109.55.186:26656,57f475bb44fc6f121790d523ce06fb4e0ad9ab69@141.95.65.73:17256,3cc5fb5f6140ac4e57dfc80940c8a06daa299c89@51.77.195.46:26656,bb2a7dc81b9bd0e017409a2bbb71b12bb899e743@178.63.22.117:26656,c0b33353fb70d8d71dcb9c8848b3b4207bd56951@94.23.207.45:30547,f4ad005ee8ec25508c498294e9e83d81b188ea49@185.248.24.16:21656,170397e75ca2b0f4e9f3b1bb5d0d23f9b10f01c7@94.23.23.189:30544,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,9832950578c4492d934d6e875165757f5a98caff@51.83.96.150:26637,17779ded6b3dc2f31d6c6f40cc6f07d802753ba7@78.47.153.128:26656,98206a8f71578850f1d88f08ede96ebc7e7c76a9@176.9.188.21:52656,0fedf7695d9e2721663c1d573d6d81a14c21533e@65.21.90.137:12856,b8c42fcb311b47cdb8285b5697f661fbba5bf1a5@51.68.157.129:26656,5f29f14fe3dd7e1d86caa4d344e67ee81c32255f@65.109.37.228:26656,e056318da91e77585f496333040e00e12f6941d1@51.83.97.166:26656,b8613a7717b0ebaf2100c360cf13c92c4de33100@195.201.63.87:41666,2b7c9ae046c35b48cb7d3d16416c3f36ab648f66@149.102.136.149:26656,641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,eeca453e3a1cf670c78e2255b8f0bd5a9443c30b@65.108.225.71:26656,b8137c688096d1abcf56942d335d061f212e6629@62.212.65.138:34656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
