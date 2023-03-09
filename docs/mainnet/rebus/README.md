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

**live-peers** (19)
```bash
peers="87102b5dd22c1d17f97197c078f23726ae3c6214@91.157.60.253:26656,275d2614d24c8ac015a7712702fcb99cef67ef67@65.108.124.219:29656,afdd27b58e851dcbb8c98c0e3191a0d8bfbcd3ae@65.108.41.252:26656,36afb1c827f52d38d7cd328b384d644b531b5997@65.108.238.102:17256,641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,10eb2d456219ea712c696251ddf231bbec6d987c@65.109.37.58:15656,89757803f40da51678451735445ad40d5b15e059@169.155.44.106:26656,3cc5fb5f6140ac4e57dfc80940c8a06daa299c89@51.77.195.46:26656,b1dcbb37514fbe215be54079e71aa39dac7fd0ae@64.5.123.203:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,7ee74ea68e350fc5214657255cba5e339bb30c2a@138.201.127.91:26674,12e6bea6650a53150c01ca3897e4a0b94d6e9d4e@135.181.141.47:26656,241c83e7a6ff769d66be0c4848db44cdcac8b4b0@192.99.62.83:26656,ebc4d27be0c87f537b44250c2e22ad349dc59fb6@158.69.116.134:26656,34e3178b6e0f25451fd690c15fc199d5a9bdfb9b@15.204.197.11:26656,b570827e4397512e077028ea7121d3e19eb25bab@85.10.200.221:26656,2f6b34ad97c4827dace87436f0299cf89fe0c056@136.243.95.80:46656,05483a7ec0160b17de1ad8e7793c7502e70e5525@146.59.85.223:17256,f546370843f92e2415524a7b18f9cd528e2fd706@65.109.55.186:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
