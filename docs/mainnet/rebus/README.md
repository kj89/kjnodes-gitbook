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

**live-peers** (29)
```bash
peers="12e6bea6650a53150c01ca3897e4a0b94d6e9d4e@135.181.141.47:26656,10eb2d456219ea712c696251ddf231bbec6d987c@65.109.37.58:15656,afdd27b58e851dcbb8c98c0e3191a0d8bfbcd3ae@65.108.41.252:26656,641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,5f29f14fe3dd7e1d86caa4d344e67ee81c32255f@65.109.37.228:26656,1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,d3a8fdbe6776fc71998fa893abcd634461b52b19@65.109.92.241:40106,4a4d2e7070e05ad6c13628d2f191d96172659452@65.109.65.210:40656,e056318da91e77585f496333040e00e12f6941d1@51.83.97.166:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.16:26656,c126eed9cfede7802d78f570fec8175835309a73@141.95.127.146:26656,8f023504e27873141164b6fbf1c4b788ff8d533b@159.69.200.24:26656,3e319c765b7b48d518a2e3218efc317234b81681@142.132.159.188:26656,237bfc05da5f8cabee00f148995333f37186d232@164.68.121.101:26656,b1b08fe470551dca6d6631fb1bfabb814f6c1aec@54.37.129.164:54556,241c83e7a6ff769d66be0c4848db44cdcac8b4b0@192.99.62.83:26656,ae67d4c37632435e0d5f27041f50af20d227bdc2@93.170.72.118:21656,89ded0a3987d22e46b756fead439e2a4d25f23cb@185.144.99.30:26656,cd71aa366822800a2aa7051fae69127f78b3f203@188.165.225.226:26656,b1dcbb37514fbe215be54079e71aa39dac7fd0ae@64.5.123.203:26656,bb2a7dc81b9bd0e017409a2bbb71b12bb899e743@178.63.22.117:26656,17779ded6b3dc2f31d6c6f40cc6f07d802753ba7@78.47.153.128:26656,ad116a3f497ebb37ac14226c22a1483237a224ac@65.108.229.102:23656,92245ff5c7a4b293d2f0c7f9afca0ddad2e0fb52@65.108.244.178:26656,faf349e185255c4aa2786da4f8ac70ea13849db0@169.155.45.128:26656,275d2614d24c8ac015a7712702fcb99cef67ef67@65.108.124.219:29656,ebc4d27be0c87f537b44250c2e22ad349dc59fb6@158.69.116.134:26656,f4ad005ee8ec25508c498294e9e83d81b188ea49@185.248.24.16:21656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
