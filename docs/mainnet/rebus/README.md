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
peers="ff7031f45a97600076f72b9318167e3dfcd2a17e@65.21.136.170:52656,f546370843f92e2415524a7b18f9cd528e2fd706@65.109.55.186:26656,c124ce0b508e8b9ed1c5b6957f362225659b5343@134.65.192.98:26656,e772ebf24c2fda82456812050fee31e19c9455fc@65.109.122.105:61456,641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,92245ff5c7a4b293d2f0c7f9afca0ddad2e0fb52@65.108.244.178:26656,87102b5dd22c1d17f97197c078f23726ae3c6214@91.157.60.253:26656,8f023504e27873141164b6fbf1c4b788ff8d533b@159.69.200.24:26656,e6f1684ed8ed5c586b188bf7088026da4ffdaff6@134.65.193.78:26656,ae67d4c37632435e0d5f27041f50af20d227bdc2@93.170.72.118:21656,e056318da91e77585f496333040e00e12f6941d1@51.83.97.166:26656,ff7621be29e39e9fdf07f2501e1a217201ca29ee@213.239.207.175:39656,ab6a4ae2857ac05fa8f45b03871fa3945193fc61@46.4.81.204:35656,2f6b34ad97c4827dace87436f0299cf89fe0c056@136.243.95.80:46656,69e27ab9b46350654805df3ea8d9ac2f00af4e4c@38.242.244.85:26656,6ac55af662061d3669d7c70961a8fd87ba2f2075@65.108.200.142:26696,f4ad005ee8ec25508c498294e9e83d81b188ea49@185.248.24.16:21656,89757803f40da51678451735445ad40d5b15e059@169.155.44.106:26656,17779ded6b3dc2f31d6c6f40cc6f07d802753ba7@78.47.153.128:26656,4a4d2e7070e05ad6c13628d2f191d96172659452@65.109.65.210:40656,237bfc05da5f8cabee00f148995333f37186d232@164.68.121.101:26656,d3a8fdbe6776fc71998fa893abcd634461b52b19@65.109.92.241:40106,b8137c688096d1abcf56942d335d061f212e6629@62.212.65.138:34656,49e084a4c77f168810608e20b530ee9d25ac69b7@209.126.8.176:26656,faf349e185255c4aa2786da4f8ac70ea13849db0@169.155.45.128:26656,6dc49b312a98051351f0347568c294fea83a5f9a@51.79.27.21:11656,b1dcbb37514fbe215be54079e71aa39dac7fd0ae@64.5.123.203:26656,cd71aa366822800a2aa7051fae69127f78b3f203@188.165.225.226:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,3a49b0d49e2dcc0fb28d97b77c4e101f20de5842@155.133.22.8:23256"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
