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
peers="6ac55af662061d3669d7c70961a8fd87ba2f2075@65.108.200.142:26696,92245ff5c7a4b293d2f0c7f9afca0ddad2e0fb52@65.108.244.178:26656,12e6bea6650a53150c01ca3897e4a0b94d6e9d4e@135.181.141.47:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.16:26656,d28516746773bfaeca4efa5537c0bf5990b8828e@65.21.229.33:27656,e6f1684ed8ed5c586b188bf7088026da4ffdaff6@134.65.193.78:26656,8f023504e27873141164b6fbf1c4b788ff8d533b@159.69.200.24:26656,89ded0a3987d22e46b756fead439e2a4d25f23cb@185.144.99.30:26656,56bb6c5da47624a89e316ddfdd732ef78d96d79c@142.93.36.204:26656,237bfc05da5f8cabee00f148995333f37186d232@164.68.121.101:26656,afdd27b58e851dcbb8c98c0e3191a0d8bfbcd3ae@65.108.41.252:26656,ab6a4ae2857ac05fa8f45b03871fa3945193fc61@46.4.81.204:35656,641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,f4ad005ee8ec25508c498294e9e83d81b188ea49@185.248.24.16:21656,1749a8f0aa533fc92c1212366c22c0993fbb1545@51.178.47.116:26656,87102b5dd22c1d17f97197c078f23726ae3c6214@91.157.60.253:26656,cd71aa366822800a2aa7051fae69127f78b3f203@188.165.225.226:26656,1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,ff7621be29e39e9fdf07f2501e1a217201ca29ee@213.239.207.175:39656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
