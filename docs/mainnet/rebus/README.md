# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/rebus.png" width="150" alt=""><figcaption></figcaption></figure>

Rebuschain is a platform that will provide DeFi (Decentralized Finance)  investment opportunities to traditional investors clearly and conveniently

**Chain ID**: reb_1111-1 | **Latest Version Tag**: v0.3.0 | **Wasm**: OFF

[Website](https://www.rebuschain.com) | [Discord](https://discord.gg/rebuschain) | [Twitter](https://twitter.com/RebusChain)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/rebus/rebusvaloper1vndzy8y55ylgpmmsc34uy8rm6kqlml6ffs9lrv)

Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals

## Restake

[Restake with kjnodes](https://restake.app/rebus/rebusvaloper1vndzy8y55ylgpmmsc34uy8rm6kqlml6ffs9lrv) (every 5 minutes)
## Chain explorer
[https://explorer.kjnodes.com/rebus](https://explorer.kjnodes.com/rebus)

## Public endpoints

* api: [https://rebus.api.kjnodes.com](https://rebus.api.kjnodes.com)
* rpc: [https://rebus.rpc.kjnodes.com](https://rebus.rpc.kjnodes.com)
* grpc: rebus.grpc.kjnodes.com:21090

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
peers="12e6bea6650a53150c01ca3897e4a0b94d6e9d4e@135.181.141.47:26656,e772ebf24c2fda82456812050fee31e19c9455fc@65.109.122.105:61456,87102b5dd22c1d17f97197c078f23726ae3c6214@91.157.60.253:26656,ff7621be29e39e9fdf07f2501e1a217201ca29ee@213.239.207.175:39656,faf349e185255c4aa2786da4f8ac70ea13849db0@169.155.45.128:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.16:26656,c126eed9cfede7802d78f570fec8175835309a73@141.95.127.146:26656,e056318da91e77585f496333040e00e12f6941d1@51.83.97.166:26656,17779ded6b3dc2f31d6c6f40cc6f07d802753ba7@78.47.153.128:26656,3e319c765b7b48d518a2e3218efc317234b81681@142.132.159.188:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,69e27ab9b46350654805df3ea8d9ac2f00af4e4c@38.242.244.85:26656,b1dcbb37514fbe215be54079e71aa39dac7fd0ae@64.5.123.203:26656,34e3178b6e0f25451fd690c15fc199d5a9bdfb9b@15.204.197.11:26656,641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,ae67d4c37632435e0d5f27041f50af20d227bdc2@93.170.72.118:21656,5f29f14fe3dd7e1d86caa4d344e67ee81c32255f@65.109.37.228:26656,8f023504e27873141164b6fbf1c4b788ff8d533b@159.69.200.24:26656,d3a8fdbe6776fc71998fa893abcd634461b52b19@65.109.92.241:40106,ab6a4ae2857ac05fa8f45b03871fa3945193fc61@46.4.81.204:35656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
