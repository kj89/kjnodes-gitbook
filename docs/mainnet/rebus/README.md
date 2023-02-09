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
peers="641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,49e084a4c77f168810608e20b530ee9d25ac69b7@209.126.8.176:26656,18ec83c4e3938aec31a3a32154969107739f0b81@135.181.153.228:26656,fa292bfad37826c9da43894b349b1480dff516b5@65.108.99.254:31656,87102b5dd22c1d17f97197c078f23726ae3c6214@91.157.60.253:26656,4e3e545e85000045ef44905ab683a5db6f87cdbe@88.198.32.17:37656,17779ded6b3dc2f31d6c6f40cc6f07d802753ba7@78.47.153.128:26656,7196b111260698b8b6ba8ea64c3af0444fb365c8@195.201.63.87:41656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.16:26656,c126eed9cfede7802d78f570fec8175835309a73@141.95.127.146:26656,2f6b34ad97c4827dace87436f0299cf89fe0c056@136.243.95.80:46656,1749a8f0aa533fc92c1212366c22c0993fbb1545@51.178.47.116:26656,0fedf7695d9e2721663c1d573d6d81a14c21533e@65.21.90.137:12856,8f023504e27873141164b6fbf1c4b788ff8d533b@159.69.200.24:26656,3e319c765b7b48d518a2e3218efc317234b81681@142.132.159.188:26656,ff7621be29e39e9fdf07f2501e1a217201ca29ee@213.239.207.175:39656,ce38728ac38ebbb4a72d496d42f8e9030af441d7@162.19.137.25:26656,cd71aa366822800a2aa7051fae69127f78b3f203@188.165.225.226:26656,b1b08fe470551dca6d6631fb1bfabb814f6c1aec@54.37.129.164:54556,241c83e7a6ff769d66be0c4848db44cdcac8b4b0@192.99.62.83:26656,10eb2d456219ea712c696251ddf231bbec6d987c@65.109.37.58:15656,6ac55af662061d3669d7c70961a8fd87ba2f2075@65.108.200.142:26696,34e3178b6e0f25451fd690c15fc199d5a9bdfb9b@15.204.197.11:26656,ab6a4ae2857ac05fa8f45b03871fa3945193fc61@46.4.81.204:35656,b8137c688096d1abcf56942d335d061f212e6629@62.212.65.138:34656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,89ded0a3987d22e46b756fead439e2a4d25f23cb@185.144.99.30:26656,2b7c9ae046c35b48cb7d3d16416c3f36ab648f66@149.102.136.149:26656,b8c42fcb311b47cdb8285b5697f661fbba5bf1a5@51.68.157.129:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
