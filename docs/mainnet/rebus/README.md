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
peers="e772ebf24c2fda82456812050fee31e19c9455fc@65.109.122.105:61456,641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,36afb1c827f52d38d7cd328b384d644b531b5997@65.108.238.102:17256,1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,6ac55af662061d3669d7c70961a8fd87ba2f2075@65.108.200.142:26696,ff7621be29e39e9fdf07f2501e1a217201ca29ee@213.239.207.175:39656,89757803f40da51678451735445ad40d5b15e059@169.155.44.106:26656,17779ded6b3dc2f31d6c6f40cc6f07d802753ba7@78.47.153.128:26656,2f6b34ad97c4827dace87436f0299cf89fe0c056@136.243.95.80:46656,f4ad005ee8ec25508c498294e9e83d81b188ea49@185.248.24.16:21656,ea5e7a6b9a5c18c6455e7a8c583c129c5821a452@51.178.80.111:26656,c124ce0b508e8b9ed1c5b6957f362225659b5343@134.65.192.98:26656,12e6bea6650a53150c01ca3897e4a0b94d6e9d4e@135.181.141.47:26656,cd71aa366822800a2aa7051fae69127f78b3f203@188.165.225.226:26656,275d2614d24c8ac015a7712702fcb99cef67ef67@65.108.124.219:29656,10eb2d456219ea712c696251ddf231bbec6d987c@65.109.37.58:15656,92245ff5c7a4b293d2f0c7f9afca0ddad2e0fb52@65.108.244.178:26656,237bfc05da5f8cabee00f148995333f37186d232@164.68.121.101:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
