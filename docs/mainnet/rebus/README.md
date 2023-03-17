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
peers="1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,ce38728ac38ebbb4a72d496d42f8e9030af441d7@162.19.137.25:26656,256d9790bf186f5a275790f7fe01e1b8800dcaaf@65.21.88.78:26656,ff7621be29e39e9fdf07f2501e1a217201ca29ee@213.239.207.175:39656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.16:26656,69e27ab9b46350654805df3ea8d9ac2f00af4e4c@38.242.244.85:26656,05483a7ec0160b17de1ad8e7793c7502e70e5525@146.59.85.223:17256,237bfc05da5f8cabee00f148995333f37186d232@164.68.121.101:26656,641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,ebc4d27be0c87f537b44250c2e22ad349dc59fb6@158.69.116.134:26656,8f023504e27873141164b6fbf1c4b788ff8d533b@159.69.200.24:26656,cd71aa366822800a2aa7051fae69127f78b3f203@188.165.225.226:26656,3a378fbfae33a593b913371c876c9d275c0abb12@213.239.215.77:26656,ae67d4c37632435e0d5f27041f50af20d227bdc2@93.170.72.118:21656,10eb2d456219ea712c696251ddf231bbec6d987c@65.109.37.58:15656,eeca453e3a1cf670c78e2255b8f0bd5a9443c30b@65.108.225.71:26656,6daeb8cfea285f561e167a0d94718b61e2cf7944@5.189.187.36:21656,3e319c765b7b48d518a2e3218efc317234b81681@142.132.159.188:26656,b5bf2242c981371224e5e9e89d6c265d554c8989@65.21.202.154:21656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
