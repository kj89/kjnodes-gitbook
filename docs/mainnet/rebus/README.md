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
peers="fa292bfad37826c9da43894b349b1480dff516b5@65.108.99.254:31656,1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,a7d96dc929824613315dcc1c90fee119f28cc51f@164.152.160.207:26656,c126eed9cfede7802d78f570fec8175835309a73@141.95.127.146:26656,3cc5fb5f6140ac4e57dfc80940c8a06daa299c89@51.77.195.46:26656,17779ded6b3dc2f31d6c6f40cc6f07d802753ba7@78.47.153.128:26656,49e084a4c77f168810608e20b530ee9d25ac69b7@209.126.8.176:26656,8f023504e27873141164b6fbf1c4b788ff8d533b@159.69.200.24:26656,ebc4d27be0c87f537b44250c2e22ad349dc59fb6@158.69.116.134:26656,92245ff5c7a4b293d2f0c7f9afca0ddad2e0fb52@65.108.244.178:26656,ff7031f45a97600076f72b9318167e3dfcd2a17e@65.21.136.170:52656,4e3e545e85000045ef44905ab683a5db6f87cdbe@88.198.32.17:37656,8535e3e22e5a10e3af6507c34b4bd9859fee4128@65.21.90.137:12856,89757803f40da51678451735445ad40d5b15e059@169.155.44.106:26656,ff7621be29e39e9fdf07f2501e1a217201ca29ee@213.239.207.175:39656,6ac55af662061d3669d7c70961a8fd87ba2f2075@65.108.200.142:26696,b1b08fe470551dca6d6631fb1bfabb814f6c1aec@54.37.129.164:54556,e6f1684ed8ed5c586b188bf7088026da4ffdaff6@134.65.193.78:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,b5bf2242c981371224e5e9e89d6c265d554c8989@65.21.202.154:21656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
