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

**live-peers** (30)
```bash
peers="87102b5dd22c1d17f97197c078f23726ae3c6214@91.157.60.253:26656,fa292bfad37826c9da43894b349b1480dff516b5@65.108.99.254:31656,641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,f546370843f92e2415524a7b18f9cd528e2fd706@65.109.55.186:26656,b5bf2242c981371224e5e9e89d6c265d554c8989@65.21.202.154:21656,30ff8100fefac53ee40ef7631f1a3c66ca2b82cf@135.181.164.90:26656,faf349e185255c4aa2786da4f8ac70ea13849db0@169.155.45.128:26656,b1b08fe470551dca6d6631fb1bfabb814f6c1aec@54.37.129.164:54556,2f6b34ad97c4827dace87436f0299cf89fe0c056@136.243.95.80:46656,69e27ab9b46350654805df3ea8d9ac2f00af4e4c@38.242.244.85:26656,ce38728ac38ebbb4a72d496d42f8e9030af441d7@162.19.137.25:26656,237bfc05da5f8cabee00f148995333f37186d232@164.68.121.101:26656,b8c42fcb311b47cdb8285b5697f661fbba5bf1a5@51.68.157.129:26656,f4ad005ee8ec25508c498294e9e83d81b188ea49@185.248.24.16:21656,89ded0a3987d22e46b756fead439e2a4d25f23cb@185.144.99.30:26656,34e3178b6e0f25451fd690c15fc199d5a9bdfb9b@15.204.197.11:26656,c126eed9cfede7802d78f570fec8175835309a73@141.95.127.146:26656,49e084a4c77f168810608e20b530ee9d25ac69b7@209.126.8.176:26656,92245ff5c7a4b293d2f0c7f9afca0ddad2e0fb52@65.108.244.178:26656,6ac55af662061d3669d7c70961a8fd87ba2f2075@65.108.200.142:26696,cd71aa366822800a2aa7051fae69127f78b3f203@188.165.225.226:26656,12e6bea6650a53150c01ca3897e4a0b94d6e9d4e@135.181.141.47:26656,89757803f40da51678451735445ad40d5b15e059@169.155.44.106:26656,ea5e7a6b9a5c18c6455e7a8c583c129c5821a452@51.178.80.111:26656,ae67d4c37632435e0d5f27041f50af20d227bdc2@93.170.72.118:21656,8f023504e27873141164b6fbf1c4b788ff8d533b@159.69.200.24:26656,4e3e545e85000045ef44905ab683a5db6f87cdbe@88.198.32.17:37656,275d2614d24c8ac015a7712702fcb99cef67ef67@65.108.124.219:29656,d3a8fdbe6776fc71998fa893abcd634461b52b19@65.109.92.241:40106,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
