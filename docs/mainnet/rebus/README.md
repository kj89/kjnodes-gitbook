# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/rebus.png" width="150" alt=""><figcaption></figcaption></figure>

Rebuschain is a platform that will provide DeFi (Decentralized Finance)  investment opportunities to traditional investors clearly and conveniently

**Chain ID**: reb_1111-1 | **Latest Version Tag**: v0.3.0 | **Wasm**: OFF

[Website](https://www.rebuschain.com) | [Discord](https://discord.gg/rebuschain) | [Twitter](https://twitter.com/RebusChain)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/rebus/rebusvaloper1vndzy8y55ylgpmmsc34uy8rm6kqlml6ffs9lrv)

## Restake

[Restake with kjnodes](https://restake.app/rebus/rebusvaloper1vndzy8y55ylgpmmsc34uy8rm6kqlml6ffs9lrv) (every day at every 5 minutes)
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
peers="d3a8fdbe6776fc71998fa893abcd634461b52b19@65.109.92.241:40106,09e5d302fd49709b5b46d391a297f448a5dc1a37@65.109.82.249:30656,a35d28e111c1dcc1e5f3203627b449adfb4425f2@65.109.29.150:21656,641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,12e6bea6650a53150c01ca3897e4a0b94d6e9d4e@135.181.141.47:26656,1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,b5bf2242c981371224e5e9e89d6c265d554c8989@65.21.202.154:21656,faf349e185255c4aa2786da4f8ac70ea13849db0@169.155.45.128:26656,8f023504e27873141164b6fbf1c4b788ff8d533b@159.69.200.24:26656,89757803f40da51678451735445ad40d5b15e059@169.155.44.106:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.16:26656,3cc5fb5f6140ac4e57dfc80940c8a06daa299c89@51.77.195.46:26656,4e3e545e85000045ef44905ab683a5db6f87cdbe@88.198.32.17:37656,ff7621be29e39e9fdf07f2501e1a217201ca29ee@213.239.207.175:39656,17779ded6b3dc2f31d6c6f40cc6f07d802753ba7@78.47.153.128:26656,3e319c765b7b48d518a2e3218efc317234b81681@142.132.159.188:26656,ab6a4ae2857ac05fa8f45b03871fa3945193fc61@46.4.81.204:35656,b8c42fcb311b47cdb8285b5697f661fbba5bf1a5@51.68.157.129:26656,05483a7ec0160b17de1ad8e7793c7502e70e5525@146.59.85.223:17256,237bfc05da5f8cabee00f148995333f37186d232@164.68.121.101:26656,b1b08fe470551dca6d6631fb1bfabb814f6c1aec@54.37.129.164:54556,6dc49b312a98051351f0347568c294fea83a5f9a@51.79.27.21:11656,34e3178b6e0f25451fd690c15fc199d5a9bdfb9b@15.204.197.11:26656,07b84cf4b47a2e5ad251267716fe05bcf30330cd@65.21.170.3:29656,6ac55af662061d3669d7c70961a8fd87ba2f2075@65.108.200.142:26696,5c2018214fcfde67ec390702539f295165f12a3a@86.48.2.20:26656,c126eed9cfede7802d78f570fec8175835309a73@141.95.127.146:26656,2b7c9ae046c35b48cb7d3d16416c3f36ab648f66@149.102.136.149:26656,2f6b34ad97c4827dace87436f0299cf89fe0c056@136.243.95.80:46656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
