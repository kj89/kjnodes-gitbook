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

**live-peers** (20)
```bash
peers="e772ebf24c2fda82456812050fee31e19c9455fc@65.109.122.105:61456,275d2614d24c8ac015a7712702fcb99cef67ef67@65.108.124.219:29656,1749a8f0aa533fc92c1212366c22c0993fbb1545@51.178.47.116:26656,c124ce0b508e8b9ed1c5b6957f362225659b5343@134.65.192.98:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.16:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,8f023504e27873141164b6fbf1c4b788ff8d533b@159.69.200.24:26656,b1dcbb37514fbe215be54079e71aa39dac7fd0ae@64.5.123.203:26656,b8613a7717b0ebaf2100c360cf13c92c4de33100@195.201.63.87:41666,5f29f14fe3dd7e1d86caa4d344e67ee81c32255f@65.109.37.228:26656,34e3178b6e0f25451fd690c15fc199d5a9bdfb9b@15.204.197.11:26656,ae67d4c37632435e0d5f27041f50af20d227bdc2@93.170.72.118:21656,05483a7ec0160b17de1ad8e7793c7502e70e5525@146.59.85.223:17256,b8137c688096d1abcf56942d335d061f212e6629@62.212.65.138:34656,ebc4d27be0c87f537b44250c2e22ad349dc59fb6@158.69.116.134:26656,3e319c765b7b48d518a2e3218efc317234b81681@142.132.159.188:26656,ff7031f45a97600076f72b9318167e3dfcd2a17e@65.21.136.170:52656,89ded0a3987d22e46b756fead439e2a4d25f23cb@185.144.99.30:26656,ff7621be29e39e9fdf07f2501e1a217201ca29ee@213.239.207.175:39656,89757803f40da51678451735445ad40d5b15e059@169.155.44.106:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
