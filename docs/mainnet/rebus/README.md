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

**live-peers** (19)
```bash
peers="346bf012c17fa30ef70ae72f082374838626532a@65.108.106.131:26696,10eb2d456219ea712c696251ddf231bbec6d987c@65.109.37.58:15656,c126eed9cfede7802d78f570fec8175835309a73@141.95.127.146:26656,e056318da91e77585f496333040e00e12f6941d1@51.83.97.166:26656,1749a8f0aa533fc92c1212366c22c0993fbb1545@51.178.47.116:26656,69e27ab9b46350654805df3ea8d9ac2f00af4e4c@38.242.244.85:26656,49e084a4c77f168810608e20b530ee9d25ac69b7@209.126.8.176:26656,e6f1684ed8ed5c586b188bf7088026da4ffdaff6@134.65.193.78:26656,34e3178b6e0f25451fd690c15fc199d5a9bdfb9b@15.204.197.11:26656,ebc4d27be0c87f537b44250c2e22ad349dc59fb6@158.69.116.134:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,d28516746773bfaeca4efa5537c0bf5990b8828e@65.21.229.33:27656,7ee74ea68e350fc5214657255cba5e339bb30c2a@138.201.127.91:26674,cd71aa366822800a2aa7051fae69127f78b3f203@188.165.225.226:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.16:26656,30ff8100fefac53ee40ef7631f1a3c66ca2b82cf@135.181.164.90:26656,5f29f14fe3dd7e1d86caa4d344e67ee81c32255f@65.109.37.228:26656,87102b5dd22c1d17f97197c078f23726ae3c6214@91.157.60.253:26656,faf349e185255c4aa2786da4f8ac70ea13849db0@169.155.45.128:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
