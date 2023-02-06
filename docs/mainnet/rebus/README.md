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
peers="05483a7ec0160b17de1ad8e7793c7502e70e5525@146.59.85.223:17256,09e5d302fd49709b5b46d391a297f448a5dc1a37@65.109.82.249:30656,36afb1c827f52d38d7cd328b384d644b531b5997@65.108.238.102:17256,256d9790bf186f5a275790f7fe01e1b8800dcaaf@65.21.88.78:26656,6ac55af662061d3669d7c70961a8fd87ba2f2075@65.108.200.142:26696,30ff8100fefac53ee40ef7631f1a3c66ca2b82cf@135.181.164.90:26656,641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,ff7621be29e39e9fdf07f2501e1a217201ca29ee@213.239.207.175:39656,4e3e545e85000045ef44905ab683a5db6f87cdbe@88.198.32.17:37656,faf349e185255c4aa2786da4f8ac70ea13849db0@169.155.45.128:26656,89757803f40da51678451735445ad40d5b15e059@169.155.44.106:26656,3cc5fb5f6140ac4e57dfc80940c8a06daa299c89@51.77.195.46:26656,3e319c765b7b48d518a2e3218efc317234b81681@142.132.159.188:26656,2b7c9ae046c35b48cb7d3d16416c3f36ab648f66@149.102.136.149:26656,69e27ab9b46350654805df3ea8d9ac2f00af4e4c@38.242.244.85:26656,237bfc05da5f8cabee00f148995333f37186d232@164.68.121.101:26656,b1b08fe470551dca6d6631fb1bfabb814f6c1aec@54.37.129.164:54556,6daeb8cfea285f561e167a0d94718b61e2cf7944@5.189.187.36:21656,d3a8fdbe6776fc71998fa893abcd634461b52b19@65.109.92.241:40106,89ded0a3987d22e46b756fead439e2a4d25f23cb@185.144.99.30:26656,34e3178b6e0f25451fd690c15fc199d5a9bdfb9b@15.204.197.11:26656,241c83e7a6ff769d66be0c4848db44cdcac8b4b0@192.99.62.83:26656,07b84cf4b47a2e5ad251267716fe05bcf30330cd@65.21.170.3:29656,8f023504e27873141164b6fbf1c4b788ff8d533b@159.69.200.24:26656,6dc49b312a98051351f0347568c294fea83a5f9a@51.79.27.21:11656,e056318da91e77585f496333040e00e12f6941d1@51.83.97.166:26656,0fedf7695d9e2721663c1d573d6d81a14c21533e@65.21.90.137:12856,ce38728ac38ebbb4a72d496d42f8e9030af441d7@162.19.137.25:26656,d12f9b52ca0e11cdeca5c46e802249ade4c39c45@185.248.24.40:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
