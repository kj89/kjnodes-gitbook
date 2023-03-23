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
peers="d3a8fdbe6776fc71998fa893abcd634461b52b19@65.109.92.241:40106,92245ff5c7a4b293d2f0c7f9afca0ddad2e0fb52@65.108.244.178:26656,e772ebf24c2fda82456812050fee31e19c9455fc@65.109.122.105:61456,e6f1684ed8ed5c586b188bf7088026da4ffdaff6@134.65.193.78:26656,a7d96dc929824613315dcc1c90fee119f28cc51f@164.152.160.207:26656,3cc5fb5f6140ac4e57dfc80940c8a06daa299c89@51.77.195.46:26656,05483a7ec0160b17de1ad8e7793c7502e70e5525@146.59.85.223:17256,a3d975c913570ad217d9a3de01a8616ad5ce20f8@142.132.128.137:26656,237bfc05da5f8cabee00f148995333f37186d232@164.68.121.101:26656,30ff8100fefac53ee40ef7631f1a3c66ca2b82cf@135.181.164.90:26656,ce38728ac38ebbb4a72d496d42f8e9030af441d7@162.19.137.25:26656,6daeb8cfea285f561e167a0d94718b61e2cf7944@5.189.187.36:21656,89ded0a3987d22e46b756fead439e2a4d25f23cb@185.144.99.30:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.16:26656,34e3178b6e0f25451fd690c15fc199d5a9bdfb9b@15.204.197.11:26656,ae67d4c37632435e0d5f27041f50af20d227bdc2@93.170.72.118:21656,6ac55af662061d3669d7c70961a8fd87ba2f2075@65.108.200.142:26696,5f29f14fe3dd7e1d86caa4d344e67ee81c32255f@65.109.37.228:26656,12e6bea6650a53150c01ca3897e4a0b94d6e9d4e@135.181.141.47:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
