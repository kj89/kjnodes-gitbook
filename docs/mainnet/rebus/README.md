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
peers="346bf012c17fa30ef70ae72f082374838626532a@65.108.106.131:26696,1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,d3a8fdbe6776fc71998fa893abcd634461b52b19@65.109.92.241:40106,641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,fa292bfad37826c9da43894b349b1480dff516b5@65.108.99.254:31656,e6f1684ed8ed5c586b188bf7088026da4ffdaff6@134.65.193.78:26656,c124ce0b508e8b9ed1c5b6957f362225659b5343@134.65.192.98:26656,89757803f40da51678451735445ad40d5b15e059@169.155.44.106:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.16:26656,c126eed9cfede7802d78f570fec8175835309a73@141.95.127.146:26656,ff7621be29e39e9fdf07f2501e1a217201ca29ee@213.239.207.175:39656,5f29f14fe3dd7e1d86caa4d344e67ee81c32255f@65.109.37.228:26656,ab6a4ae2857ac05fa8f45b03871fa3945193fc61@46.4.81.204:35656,69e27ab9b46350654805df3ea8d9ac2f00af4e4c@38.242.244.85:26656,237bfc05da5f8cabee00f148995333f37186d232@164.68.121.101:26656,05483a7ec0160b17de1ad8e7793c7502e70e5525@146.59.85.223:17256,89ded0a3987d22e46b756fead439e2a4d25f23cb@185.144.99.30:26656,ebc4d27be0c87f537b44250c2e22ad349dc59fb6@158.69.116.134:26656,275d2614d24c8ac015a7712702fcb99cef67ef67@65.108.124.219:29656,92245ff5c7a4b293d2f0c7f9afca0ddad2e0fb52@65.108.244.178:26656,cd71aa366822800a2aa7051fae69127f78b3f203@188.165.225.226:26656,afdd27b58e851dcbb8c98c0e3191a0d8bfbcd3ae@65.108.41.252:26656,34e3178b6e0f25451fd690c15fc199d5a9bdfb9b@15.204.197.11:26656,241c83e7a6ff769d66be0c4848db44cdcac8b4b0@192.99.62.83:26656,4a4d2e7070e05ad6c13628d2f191d96172659452@65.109.65.210:40656,12e6bea6650a53150c01ca3897e4a0b94d6e9d4e@135.181.141.47:26656,6dc49b312a98051351f0347568c294fea83a5f9a@51.79.27.21:11656,f546370843f92e2415524a7b18f9cd528e2fd706@65.109.55.186:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,d12f9b52ca0e11cdeca5c46e802249ade4c39c45@185.248.24.40:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
