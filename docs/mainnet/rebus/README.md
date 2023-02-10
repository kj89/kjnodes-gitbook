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
peers="275d2614d24c8ac015a7712702fcb99cef67ef67@65.108.124.219:29656,346bf012c17fa30ef70ae72f082374838626532a@65.108.106.131:26696,30ff8100fefac53ee40ef7631f1a3c66ca2b82cf@135.181.164.90:26656,10eb2d456219ea712c696251ddf231bbec6d987c@65.109.37.58:15656,12e6bea6650a53150c01ca3897e4a0b94d6e9d4e@135.181.141.47:26656,18ec83c4e3938aec31a3a32154969107739f0b81@135.181.153.228:26656,afdd27b58e851dcbb8c98c0e3191a0d8bfbcd3ae@65.108.41.252:26656,87102b5dd22c1d17f97197c078f23726ae3c6214@91.157.60.253:26656,bb2a7dc81b9bd0e017409a2bbb71b12bb899e743@178.63.22.117:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.16:26656,4e3e545e85000045ef44905ab683a5db6f87cdbe@88.198.32.17:37656,17779ded6b3dc2f31d6c6f40cc6f07d802753ba7@78.47.153.128:26656,7ee74ea68e350fc5214657255cba5e339bb30c2a@138.201.127.91:26674,3e319c765b7b48d518a2e3218efc317234b81681@142.132.159.188:26656,05483a7ec0160b17de1ad8e7793c7502e70e5525@146.59.85.223:17256,b8c42fcb311b47cdb8285b5697f661fbba5bf1a5@51.68.157.129:26656,241c83e7a6ff769d66be0c4848db44cdcac8b4b0@192.99.62.83:26656,ebc4d27be0c87f537b44250c2e22ad349dc59fb6@158.69.116.134:26656,b1dcbb37514fbe215be54079e71aa39dac7fd0ae@64.5.123.203:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,6daeb8cfea285f561e167a0d94718b61e2cf7944@5.189.187.36:21656,641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,ae67d4c37632435e0d5f27041f50af20d227bdc2@93.170.72.118:21656,07b84cf4b47a2e5ad251267716fe05bcf30330cd@65.21.170.3:29656,49e084a4c77f168810608e20b530ee9d25ac69b7@209.126.8.176:26656,fa292bfad37826c9da43894b349b1480dff516b5@65.108.99.254:31656,0fedf7695d9e2721663c1d573d6d81a14c21533e@65.21.90.137:12856,89757803f40da51678451735445ad40d5b15e059@169.155.44.106:26656,09e5d302fd49709b5b46d391a297f448a5dc1a37@65.109.82.249:30656,1fe32d8f09b8715b1e626da17b3ecfe26623b371@176.9.22.117:27656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
