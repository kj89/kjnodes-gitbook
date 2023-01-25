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

**live-peers** (30)
```bash
peers="f4ad005ee8ec25508c498294e9e83d81b188ea49@185.248.24.16:21656,18ec83c4e3938aec31a3a32154969107739f0b81@135.181.153.228:26656,30ff8100fefac53ee40ef7631f1a3c66ca2b82cf@135.181.164.90:26656,12703ce9efe6c1171c193dae2e2041a2be610852@65.108.44.149:29656,5f29f14fe3dd7e1d86caa4d344e67ee81c32255f@65.109.37.228:26656,1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,eeca453e3a1cf670c78e2255b8f0bd5a9443c30b@65.108.225.71:26656,d28516746773bfaeca4efa5537c0bf5990b8828e@65.21.229.33:27656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.16:26656,641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,c0b33353fb70d8d71dcb9c8848b3b4207bd56951@94.23.207.45:30547,e056318da91e77585f496333040e00e12f6941d1@51.83.97.166:26656,b570827e4397512e077028ea7121d3e19eb25bab@85.10.200.221:26656,4e3e545e85000045ef44905ab683a5db6f87cdbe@88.198.32.17:37656,afdd27b58e851dcbb8c98c0e3191a0d8bfbcd3ae@65.108.41.252:26656,6d8c83cc702365363b829a14efdd414401da369b@23.88.69.167:27565,b8137c688096d1abcf56942d335d061f212e6629@62.212.65.138:34656,6daeb8cfea285f561e167a0d94718b61e2cf7944@5.189.187.36:21656,ae67d4c37632435e0d5f27041f50af20d227bdc2@93.170.72.118:21656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,05483a7ec0160b17de1ad8e7793c7502e70e5525@146.59.85.223:17256,0fedf7695d9e2721663c1d573d6d81a14c21533e@65.21.90.137:12856,a35d28e111c1dcc1e5f3203627b449adfb4425f2@65.109.29.150:21656,89757803f40da51678451735445ad40d5b15e059@169.155.44.106:26656,b1b08fe470551dca6d6631fb1bfabb814f6c1aec@54.37.129.164:54556,2f6b34ad97c4827dace87436f0299cf89fe0c056@136.243.95.80:46656,bb2a7dc81b9bd0e017409a2bbb71b12bb899e743@178.63.22.117:26656,3e319c765b7b48d518a2e3218efc317234b81681@142.132.159.188:26656,b8c42fcb311b47cdb8285b5697f661fbba5bf1a5@51.68.157.129:26656,07b84cf4b47a2e5ad251267716fe05bcf30330cd@65.21.170.3:29656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
