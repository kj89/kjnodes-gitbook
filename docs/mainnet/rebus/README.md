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
peers="275d2614d24c8ac015a7712702fcb99cef67ef67@65.108.124.219:29656,12e6bea6650a53150c01ca3897e4a0b94d6e9d4e@135.181.141.47:26656,641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,faf349e185255c4aa2786da4f8ac70ea13849db0@169.155.45.128:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.16:26656,89757803f40da51678451735445ad40d5b15e059@169.155.44.106:26656,e056318da91e77585f496333040e00e12f6941d1@51.83.97.166:26656,8f023504e27873141164b6fbf1c4b788ff8d533b@159.69.200.24:26656,4e3e545e85000045ef44905ab683a5db6f87cdbe@88.198.32.17:37656,3e319c765b7b48d518a2e3218efc317234b81681@142.132.159.188:26656,ff7621be29e39e9fdf07f2501e1a217201ca29ee@213.239.207.175:39656,cd71aa366822800a2aa7051fae69127f78b3f203@188.165.225.226:26656,69e27ab9b46350654805df3ea8d9ac2f00af4e4c@38.242.244.85:26656,f4ad005ee8ec25508c498294e9e83d81b188ea49@185.248.24.16:21656,89ded0a3987d22e46b756fead439e2a4d25f23cb@185.144.99.30:26656,34e3178b6e0f25451fd690c15fc199d5a9bdfb9b@15.204.197.11:26656,ebc4d27be0c87f537b44250c2e22ad349dc59fb6@158.69.116.134:26656,fa292bfad37826c9da43894b349b1480dff516b5@65.108.99.254:31656,241c83e7a6ff769d66be0c4848db44cdcac8b4b0@192.99.62.83:26656,3cc5fb5f6140ac4e57dfc80940c8a06daa299c89@51.77.195.46:26656,40fa2184a7a81e0aae2f9354632e766608afc22a@135.181.207.115:56656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,a7d96dc929824613315dcc1c90fee119f28cc51f@164.152.160.207:26656,237bfc05da5f8cabee00f148995333f37186d232@164.68.121.101:26656,d3a8fdbe6776fc71998fa893abcd634461b52b19@65.109.92.241:40106,0fedf7695d9e2721663c1d573d6d81a14c21533e@65.21.90.137:12856,6ac55af662061d3669d7c70961a8fd87ba2f2075@65.108.200.142:26696,6dc49b312a98051351f0347568c294fea83a5f9a@51.79.27.21:11656,2f6b34ad97c4827dace87436f0299cf89fe0c056@136.243.95.80:46656,1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
