# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/rebus.png" width="150" alt=""><figcaption></figcaption></figure>

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

**live-peers** (19)
```bash
peers="d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,e772ebf24c2fda82456812050fee31e19c9455fc@65.109.122.105:61456,275d2614d24c8ac015a7712702fcb99cef67ef67@65.108.124.219:29656,6ac55af662061d3669d7c70961a8fd87ba2f2075@65.108.200.142:26696,e6f1684ed8ed5c586b188bf7088026da4ffdaff6@134.65.193.78:26656,ab6a4ae2857ac05fa8f45b03871fa3945193fc61@46.4.81.204:35656,a3d975c913570ad217d9a3de01a8616ad5ce20f8@142.132.128.137:26656,241c83e7a6ff769d66be0c4848db44cdcac8b4b0@192.99.62.83:26656,cd71aa366822800a2aa7051fae69127f78b3f203@188.165.225.226:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.16:26656,3e319c765b7b48d518a2e3218efc317234b81681@142.132.159.188:26656,17779ded6b3dc2f31d6c6f40cc6f07d802753ba7@78.47.153.128:26656,b1dcbb37514fbe215be54079e71aa39dac7fd0ae@64.5.123.203:26656,ae67d4c37632435e0d5f27041f50af20d227bdc2@93.170.72.118:21656,c126eed9cfede7802d78f570fec8175835309a73@141.95.127.146:26656,89757803f40da51678451735445ad40d5b15e059@169.155.44.106:26656,641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,8f023504e27873141164b6fbf1c4b788ff8d533b@159.69.200.24:26656,2f6b34ad97c4827dace87436f0299cf89fe0c056@136.243.95.80:46656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
