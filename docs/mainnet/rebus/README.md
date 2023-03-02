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

**live-peers** (20)
```bash
peers="10eb2d456219ea712c696251ddf231bbec6d987c@65.109.37.58:15656,e772ebf24c2fda82456812050fee31e19c9455fc@65.109.122.105:61456,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.16:26656,89757803f40da51678451735445ad40d5b15e059@169.155.44.106:26656,23529a8c0b1ebbb1459b8bd82d591cfeb396baa1@57.128.82.243:11656,ce38728ac38ebbb4a72d496d42f8e9030af441d7@162.19.137.25:26656,c124ce0b508e8b9ed1c5b6957f362225659b5343@134.65.192.98:26656,8f023504e27873141164b6fbf1c4b788ff8d533b@159.69.200.24:26656,17779ded6b3dc2f31d6c6f40cc6f07d802753ba7@78.47.153.128:26656,b1b08fe470551dca6d6631fb1bfabb814f6c1aec@54.37.129.164:54556,ab6a4ae2857ac05fa8f45b03871fa3945193fc61@46.4.81.204:35656,34e3178b6e0f25451fd690c15fc199d5a9bdfb9b@15.204.197.11:26656,237bfc05da5f8cabee00f148995333f37186d232@164.68.121.101:26656,49e084a4c77f168810608e20b530ee9d25ac69b7@209.126.8.176:26656,ebc4d27be0c87f537b44250c2e22ad349dc59fb6@158.69.116.134:26656,3e319c765b7b48d518a2e3218efc317234b81681@142.132.159.188:26656,89ded0a3987d22e46b756fead439e2a4d25f23cb@185.144.99.30:26656,ae67d4c37632435e0d5f27041f50af20d227bdc2@93.170.72.118:21656,cd71aa366822800a2aa7051fae69127f78b3f203@188.165.225.226:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
