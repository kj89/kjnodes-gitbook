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
peers="1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,ff7031f45a97600076f72b9318167e3dfcd2a17e@65.21.136.170:52656,87102b5dd22c1d17f97197c078f23726ae3c6214@91.157.60.253:26656,c126eed9cfede7802d78f570fec8175835309a73@141.95.127.146:26656,ff7621be29e39e9fdf07f2501e1a217201ca29ee@213.239.207.175:39656,faf349e185255c4aa2786da4f8ac70ea13849db0@169.155.45.128:26656,8f023504e27873141164b6fbf1c4b788ff8d533b@159.69.200.24:26656,3e319c765b7b48d518a2e3218efc317234b81681@142.132.159.188:26656,69e27ab9b46350654805df3ea8d9ac2f00af4e4c@38.242.244.85:26656,ae67d4c37632435e0d5f27041f50af20d227bdc2@93.170.72.118:21656,6daeb8cfea285f561e167a0d94718b61e2cf7944@5.189.187.36:21656,ebc4d27be0c87f537b44250c2e22ad349dc59fb6@158.69.116.134:26656,b1dcbb37514fbe215be54079e71aa39dac7fd0ae@64.5.123.203:26656,17779ded6b3dc2f31d6c6f40cc6f07d802753ba7@78.47.153.128:26656,d28516746773bfaeca4efa5537c0bf5990b8828e@65.21.229.33:27656,05483a7ec0160b17de1ad8e7793c7502e70e5525@146.59.85.223:17256,ce38728ac38ebbb4a72d496d42f8e9030af441d7@162.19.137.25:26656,cd71aa366822800a2aa7051fae69127f78b3f203@188.165.225.226:26656,34e3178b6e0f25451fd690c15fc199d5a9bdfb9b@15.204.197.11:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
