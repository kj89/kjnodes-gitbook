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
peers="b5bf2242c981371224e5e9e89d6c265d554c8989@65.21.202.154:21656,641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,8535e3e22e5a10e3af6507c34b4bd9859fee4128@65.21.90.137:12856,faf349e185255c4aa2786da4f8ac70ea13849db0@169.155.45.128:26656,89757803f40da51678451735445ad40d5b15e059@169.155.44.106:26656,1749a8f0aa533fc92c1212366c22c0993fbb1545@51.178.47.116:26656,4e3e545e85000045ef44905ab683a5db6f87cdbe@88.198.32.17:37656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,10eb2d456219ea712c696251ddf231bbec6d987c@65.109.37.58:15656,34e3178b6e0f25451fd690c15fc199d5a9bdfb9b@15.204.197.11:26656,ea5e7a6b9a5c18c6455e7a8c583c129c5821a452@51.178.80.111:26656,4a4d2e7070e05ad6c13628d2f191d96172659452@65.109.65.210:40656,3e319c765b7b48d518a2e3218efc317234b81681@142.132.159.188:26656,237bfc05da5f8cabee00f148995333f37186d232@164.68.121.101:26656,89ded0a3987d22e46b756fead439e2a4d25f23cb@185.144.99.30:26656,5f29f14fe3dd7e1d86caa4d344e67ee81c32255f@65.109.37.228:26656,e6f1684ed8ed5c586b188bf7088026da4ffdaff6@134.65.193.78:26656,c126eed9cfede7802d78f570fec8175835309a73@141.95.127.146:26656,bb2a7dc81b9bd0e017409a2bbb71b12bb899e743@178.63.22.117:26656,304ff8e051b2fbd038771142b69ac915c14c0819@78.46.78.83:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
