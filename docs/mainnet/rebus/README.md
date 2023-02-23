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
peers="346bf012c17fa30ef70ae72f082374838626532a@65.108.106.131:26696,b5bf2242c981371224e5e9e89d6c265d554c8989@65.21.202.154:21656,5f29f14fe3dd7e1d86caa4d344e67ee81c32255f@65.109.37.228:26656,c124ce0b508e8b9ed1c5b6957f362225659b5343@134.65.192.98:26656,1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,30ff8100fefac53ee40ef7631f1a3c66ca2b82cf@135.181.164.90:26656,87102b5dd22c1d17f97197c078f23726ae3c6214@91.157.60.253:26656,17779ded6b3dc2f31d6c6f40cc6f07d802753ba7@78.47.153.128:26656,e6f1684ed8ed5c586b188bf7088026da4ffdaff6@134.65.193.78:26656,89757803f40da51678451735445ad40d5b15e059@169.155.44.106:26656,b8137c688096d1abcf56942d335d061f212e6629@62.212.65.138:34656,1fe32d8f09b8715b1e626da17b3ecfe26623b371@176.9.22.117:27656,0fedf7695d9e2721663c1d573d6d81a14c21533e@65.21.90.137:12856,237bfc05da5f8cabee00f148995333f37186d232@164.68.121.101:26656,34e3178b6e0f25451fd690c15fc199d5a9bdfb9b@15.204.197.11:26656,6ac55af662061d3669d7c70961a8fd87ba2f2075@65.108.200.142:26696,faf349e185255c4aa2786da4f8ac70ea13849db0@169.155.45.128:26656,641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,d28516746773bfaeca4efa5537c0bf5990b8828e@65.21.229.33:27656,69e27ab9b46350654805df3ea8d9ac2f00af4e4c@38.242.244.85:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,b1dcbb37514fbe215be54079e71aa39dac7fd0ae@64.5.123.203:26656,49e084a4c77f168810608e20b530ee9d25ac69b7@209.126.8.176:26656,ae67d4c37632435e0d5f27041f50af20d227bdc2@93.170.72.118:21656,6dc49b312a98051351f0347568c294fea83a5f9a@51.79.27.21:11656,ebc4d27be0c87f537b44250c2e22ad349dc59fb6@158.69.116.134:26656,f546370843f92e2415524a7b18f9cd528e2fd706@65.109.55.186:26656,36afb1c827f52d38d7cd328b384d644b531b5997@65.108.238.102:17256,bb2a7dc81b9bd0e017409a2bbb71b12bb899e743@178.63.22.117:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
