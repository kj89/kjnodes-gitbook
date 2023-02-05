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
peers="18ec83c4e3938aec31a3a32154969107739f0b81@135.181.153.228:26656,2f6b34ad97c4827dace87436f0299cf89fe0c056@136.243.95.80:46656,5f29f14fe3dd7e1d86caa4d344e67ee81c32255f@65.109.37.228:26656,09e5d302fd49709b5b46d391a297f448a5dc1a37@65.109.82.249:30656,1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,10eb2d456219ea712c696251ddf231bbec6d987c@65.109.37.58:15656,07b84cf4b47a2e5ad251267716fe05bcf30330cd@65.21.170.3:29656,87102b5dd22c1d17f97197c078f23726ae3c6214@91.157.60.253:26656,c124ce0b508e8b9ed1c5b6957f362225659b5343@134.65.192.98:26656,4e3e545e85000045ef44905ab683a5db6f87cdbe@88.198.32.17:37656,89757803f40da51678451735445ad40d5b15e059@169.155.44.106:26656,ce38728ac38ebbb4a72d496d42f8e9030af441d7@162.19.137.25:26656,1749a8f0aa533fc92c1212366c22c0993fbb1545@51.178.47.116:26656,0fedf7695d9e2721663c1d573d6d81a14c21533e@65.21.90.137:12856,1fe32d8f09b8715b1e626da17b3ecfe26623b371@176.9.22.117:27656,05483a7ec0160b17de1ad8e7793c7502e70e5525@146.59.85.223:17256,89ded0a3987d22e46b756fead439e2a4d25f23cb@185.144.99.30:26656,b1dcbb37514fbe215be54079e71aa39dac7fd0ae@64.5.123.203:26656,d3a8fdbe6776fc71998fa893abcd634461b52b19@65.109.92.241:40106,69e27ab9b46350654805df3ea8d9ac2f00af4e4c@38.242.244.85:26656,e056318da91e77585f496333040e00e12f6941d1@51.83.97.166:26656,237bfc05da5f8cabee00f148995333f37186d232@164.68.121.101:26656,2b7c9ae046c35b48cb7d3d16416c3f36ab648f66@149.102.136.149:26656,cd71aa366822800a2aa7051fae69127f78b3f203@188.165.225.226:26656,241c83e7a6ff769d66be0c4848db44cdcac8b4b0@192.99.62.83:26656,17779ded6b3dc2f31d6c6f40cc6f07d802753ba7@78.47.153.128:26656,ae67d4c37632435e0d5f27041f50af20d227bdc2@93.170.72.118:21656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.16:26656,6dc49b312a98051351f0347568c294fea83a5f9a@51.79.27.21:11656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
