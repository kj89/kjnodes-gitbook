# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/rebus.png" width="150" alt=""><figcaption></figcaption></figure>

Rebuschain is a platform that will provide DeFi (Decentralized Finance)  investment opportunities to traditional investors clearly and conveniently

**Chain ID**: reb_1111-1 | **Latest Version Tag**: v0.3.0 | **Wasm**: OFF

[Website](https://www.rebuschain.com) | [Discord](https://discord.gg/rebuschain) | [Twitter](https://twitter.com/RebusChain)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/rebus/rebusvaloper1vndzy8y55ylgpmmsc34uy8rm6kqlml6ffs9lrv)

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
peers="fa292bfad37826c9da43894b349b1480dff516b5@65.108.99.254:31656,256d9790bf186f5a275790f7fe01e1b8800dcaaf@65.21.88.78:26656,d28516746773bfaeca4efa5537c0bf5990b8828e@65.21.229.33:27656,641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,4a4d2e7070e05ad6c13628d2f191d96172659452@65.109.65.210:40656,d3a8fdbe6776fc71998fa893abcd634461b52b19@65.109.92.241:40106,07b84cf4b47a2e5ad251267716fe05bcf30330cd@65.21.170.3:29656,17779ded6b3dc2f31d6c6f40cc6f07d802753ba7@78.47.153.128:26656,3e319c765b7b48d518a2e3218efc317234b81681@142.132.159.188:26656,faf349e185255c4aa2786da4f8ac70ea13849db0@169.155.45.128:26656,c124ce0b508e8b9ed1c5b6957f362225659b5343@134.65.192.98:26656,89757803f40da51678451735445ad40d5b15e059@169.155.44.106:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.16:26656,8f023504e27873141164b6fbf1c4b788ff8d533b@159.69.200.24:26656,ab6a4ae2857ac05fa8f45b03871fa3945193fc61@46.4.81.204:35656,0fedf7695d9e2721663c1d573d6d81a14c21533e@65.21.90.137:12856,b8137c688096d1abcf56942d335d061f212e6629@62.212.65.138:34656,5c2018214fcfde67ec390702539f295165f12a3a@86.48.2.20:26656,b8c42fcb311b47cdb8285b5697f661fbba5bf1a5@51.68.157.129:26656,89ded0a3987d22e46b756fead439e2a4d25f23cb@185.144.99.30:26656,6ac55af662061d3669d7c70961a8fd87ba2f2075@65.108.200.142:26696,cd71aa366822800a2aa7051fae69127f78b3f203@188.165.225.226:26656,4e3e545e85000045ef44905ab683a5db6f87cdbe@88.198.32.17:37656,b1b08fe470551dca6d6631fb1bfabb814f6c1aec@54.37.129.164:54556,241c83e7a6ff769d66be0c4848db44cdcac8b4b0@192.99.62.83:26656,6dc49b312a98051351f0347568c294fea83a5f9a@51.79.27.21:11656,b5bf2242c981371224e5e9e89d6c265d554c8989@65.21.202.154:21656,b1dcbb37514fbe215be54079e71aa39dac7fd0ae@64.5.123.203:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
