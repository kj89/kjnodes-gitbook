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

**live-peers** (29)
```bash
peers="07b84cf4b47a2e5ad251267716fe05bcf30330cd@65.21.170.3:29656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,b5bf2242c981371224e5e9e89d6c265d554c8989@65.21.202.154:21656,ff7031f45a97600076f72b9318167e3dfcd2a17e@65.21.136.170:52656,641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,e772ebf24c2fda82456812050fee31e19c9455fc@65.109.122.105:61456,89757803f40da51678451735445ad40d5b15e059@169.155.44.106:26656,faf349e185255c4aa2786da4f8ac70ea13849db0@169.155.45.128:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.16:26656,17779ded6b3dc2f31d6c6f40cc6f07d802753ba7@78.47.153.128:26656,2f6b34ad97c4827dace87436f0299cf89fe0c056@136.243.95.80:46656,0fedf7695d9e2721663c1d573d6d81a14c21533e@65.21.90.137:12856,69e27ab9b46350654805df3ea8d9ac2f00af4e4c@38.242.244.85:26656,ce38728ac38ebbb4a72d496d42f8e9030af441d7@162.19.137.25:26656,92245ff5c7a4b293d2f0c7f9afca0ddad2e0fb52@65.108.244.178:26656,b1dcbb37514fbe215be54079e71aa39dac7fd0ae@64.5.123.203:26656,ae67d4c37632435e0d5f27041f50af20d227bdc2@93.170.72.118:21656,e056318da91e77585f496333040e00e12f6941d1@51.83.97.166:26656,8f023504e27873141164b6fbf1c4b788ff8d533b@159.69.200.24:26656,d3a8fdbe6776fc71998fa893abcd634461b52b19@65.109.92.241:40106,4e3e545e85000045ef44905ab683a5db6f87cdbe@88.198.32.17:37656,34e3178b6e0f25451fd690c15fc199d5a9bdfb9b@15.204.197.11:26656,30ff8100fefac53ee40ef7631f1a3c66ca2b82cf@135.181.164.90:26656,c126eed9cfede7802d78f570fec8175835309a73@141.95.127.146:26656,cd71aa366822800a2aa7051fae69127f78b3f203@188.165.225.226:26656,e6f1684ed8ed5c586b188bf7088026da4ffdaff6@134.65.193.78:26656,275d2614d24c8ac015a7712702fcb99cef67ef67@65.108.124.219:29656,678ded952968137c8ded8aeada337662065f1507@159.203.162.120:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
