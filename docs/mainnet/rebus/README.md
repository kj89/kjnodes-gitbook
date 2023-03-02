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

**live-peers** (20)
```bash
peers="275d2614d24c8ac015a7712702fcb99cef67ef67@65.108.124.219:29656,ff7621be29e39e9fdf07f2501e1a217201ca29ee@213.239.207.175:39656,12e6bea6650a53150c01ca3897e4a0b94d6e9d4e@135.181.141.47:26656,1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,07b84cf4b47a2e5ad251267716fe05bcf30330cd@65.21.170.3:29656,faf349e185255c4aa2786da4f8ac70ea13849db0@169.155.45.128:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.16:26656,89757803f40da51678451735445ad40d5b15e059@169.155.44.106:26656,c126eed9cfede7802d78f570fec8175835309a73@141.95.127.146:26656,6ac55af662061d3669d7c70961a8fd87ba2f2075@65.108.200.142:26696,0fedf7695d9e2721663c1d573d6d81a14c21533e@65.21.90.137:12856,69e27ab9b46350654805df3ea8d9ac2f00af4e4c@38.242.244.85:26656,f4ad005ee8ec25508c498294e9e83d81b188ea49@185.248.24.16:21656,ebc4d27be0c87f537b44250c2e22ad349dc59fb6@158.69.116.134:26656,34e3178b6e0f25451fd690c15fc199d5a9bdfb9b@15.204.197.11:26656,49e084a4c77f168810608e20b530ee9d25ac69b7@209.126.8.176:26656,92245ff5c7a4b293d2f0c7f9afca0ddad2e0fb52@65.108.244.178:26656,b5bf2242c981371224e5e9e89d6c265d554c8989@65.21.202.154:21656,10eb2d456219ea712c696251ddf231bbec6d987c@65.109.37.58:15656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
