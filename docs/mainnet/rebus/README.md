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
peers="fa292bfad37826c9da43894b349b1480dff516b5@65.108.99.254:31656,e772ebf24c2fda82456812050fee31e19c9455fc@65.109.122.105:61456,f546370843f92e2415524a7b18f9cd528e2fd706@65.109.55.186:26656,1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,d3a8fdbe6776fc71998fa893abcd634461b52b19@65.109.92.241:40106,5f29f14fe3dd7e1d86caa4d344e67ee81c32255f@65.109.37.228:26656,87102b5dd22c1d17f97197c078f23726ae3c6214@91.157.60.253:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.16:26656,c124ce0b508e8b9ed1c5b6957f362225659b5343@134.65.192.98:26656,ebc4d27be0c87f537b44250c2e22ad349dc59fb6@158.69.116.134:26656,256d9790bf186f5a275790f7fe01e1b8800dcaaf@65.21.88.78:26656,a7d96dc929824613315dcc1c90fee119f28cc51f@164.152.160.207:26656,faf349e185255c4aa2786da4f8ac70ea13849db0@169.155.45.128:26656,89757803f40da51678451735445ad40d5b15e059@169.155.44.106:26656,92245ff5c7a4b293d2f0c7f9afca0ddad2e0fb52@65.108.244.178:26656,b1dcbb37514fbe215be54079e71aa39dac7fd0ae@64.5.123.203:26656,07b84cf4b47a2e5ad251267716fe05bcf30330cd@65.21.170.3:29656,641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,ff7031f45a97600076f72b9318167e3dfcd2a17e@65.21.136.170:52656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
