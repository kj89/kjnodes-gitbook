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
peers="3e319c765b7b48d518a2e3218efc317234b81681@142.132.159.188:26656,f4ad005ee8ec25508c498294e9e83d81b188ea49@185.248.24.16:21656,12e6bea6650a53150c01ca3897e4a0b94d6e9d4e@135.181.141.47:26656,07b84cf4b47a2e5ad251267716fe05bcf30330cd@65.21.170.3:29656,10eb2d456219ea712c696251ddf231bbec6d987c@65.109.37.58:15656,36afb1c827f52d38d7cd328b384d644b531b5997@65.108.238.102:17256,30ff8100fefac53ee40ef7631f1a3c66ca2b82cf@135.181.164.90:26656,faf349e185255c4aa2786da4f8ac70ea13849db0@169.155.45.128:26656,ae67d4c37632435e0d5f27041f50af20d227bdc2@93.170.72.118:21656,c124ce0b508e8b9ed1c5b6957f362225659b5343@134.65.192.98:26656,237bfc05da5f8cabee00f148995333f37186d232@164.68.121.101:26656,b1dcbb37514fbe215be54079e71aa39dac7fd0ae@64.5.123.203:26656,cd71aa366822800a2aa7051fae69127f78b3f203@188.165.225.226:26656,346bf012c17fa30ef70ae72f082374838626532a@65.108.106.131:26696,6ac55af662061d3669d7c70961a8fd87ba2f2075@65.108.200.142:26696,92245ff5c7a4b293d2f0c7f9afca0ddad2e0fb52@65.108.244.178:26656,69e27ab9b46350654805df3ea8d9ac2f00af4e4c@38.242.244.85:26656,8f023504e27873141164b6fbf1c4b788ff8d533b@159.69.200.24:26656,275d2614d24c8ac015a7712702fcb99cef67ef67@65.108.124.219:29656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
