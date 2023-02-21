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
peers="641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,10eb2d456219ea712c696251ddf231bbec6d987c@65.109.37.58:15656,1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,d28516746773bfaeca4efa5537c0bf5990b8828e@65.21.229.33:27656,275d2614d24c8ac015a7712702fcb99cef67ef67@65.108.124.219:29656,afdd27b58e851dcbb8c98c0e3191a0d8bfbcd3ae@65.108.41.252:26656,87102b5dd22c1d17f97197c078f23726ae3c6214@91.157.60.253:26656,3e319c765b7b48d518a2e3218efc317234b81681@142.132.159.188:26656,0fedf7695d9e2721663c1d573d6d81a14c21533e@65.21.90.137:12856,3cc5fb5f6140ac4e57dfc80940c8a06daa299c89@51.77.195.46:26656,b570827e4397512e077028ea7121d3e19eb25bab@85.10.200.221:26656,8f023504e27873141164b6fbf1c4b788ff8d533b@159.69.200.24:26656,4e3e545e85000045ef44905ab683a5db6f87cdbe@88.198.32.17:37656,ce38728ac38ebbb4a72d496d42f8e9030af441d7@162.19.137.25:26656,69e27ab9b46350654805df3ea8d9ac2f00af4e4c@38.242.244.85:26656,34e3178b6e0f25451fd690c15fc199d5a9bdfb9b@15.204.197.11:26656,40fa2184a7a81e0aae2f9354632e766608afc22a@135.181.207.115:56656,b1dcbb37514fbe215be54079e71aa39dac7fd0ae@64.5.123.203:26656,346bf012c17fa30ef70ae72f082374838626532a@65.108.106.131:26696,faf349e185255c4aa2786da4f8ac70ea13849db0@169.155.45.128:26656,ff7621be29e39e9fdf07f2501e1a217201ca29ee@213.239.207.175:39656,89757803f40da51678451735445ad40d5b15e059@169.155.44.106:26656,cd71aa366822800a2aa7051fae69127f78b3f203@188.165.225.226:26656,6dc49b312a98051351f0347568c294fea83a5f9a@51.79.27.21:11656,ae67d4c37632435e0d5f27041f50af20d227bdc2@93.170.72.118:21656,f4ad005ee8ec25508c498294e9e83d81b188ea49@185.248.24.16:21656,17779ded6b3dc2f31d6c6f40cc6f07d802753ba7@78.47.153.128:26656,ab6a4ae2857ac05fa8f45b03871fa3945193fc61@46.4.81.204:35656,fa292bfad37826c9da43894b349b1480dff516b5@65.108.99.254:31656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
