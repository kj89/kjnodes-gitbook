# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/rebus.png" width="150" alt=""><figcaption></figcaption></figure>

Rebuschain is a platform that will provide DeFi (Decentralized Finance)  investment opportunities to traditional investors clearly and conveniently

**Chain ID**: reb_1111-1 | **Latest Version Tag**: v0.2.0 | **Wasm**: OFF

[Website](https://www.rebuschain.com) | [Discord](https://discord.gg/rebuschain) | [Twitter](https://twitter.com/RebusChain)

## Restake

[Restake with kjnodes](https://restake.app/rebus/rebusvaloper1vndzy8y55ylgpmmsc34uy8rm6kqlml6ffs9lrv) (every day at 08:00, 20:00)
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
peers="d28516746773bfaeca4efa5537c0bf5990b8828e@65.21.229.33:27656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,5f29f14fe3dd7e1d86caa4d344e67ee81c32255f@65.109.37.228:26656,4a4d2e7070e05ad6c13628d2f191d96172659452@65.109.65.210:40656,57f475bb44fc6f121790d523ce06fb4e0ad9ab69@141.95.65.73:17256,b570827e4397512e077028ea7121d3e19eb25bab@85.10.200.221:26656,b8613a7717b0ebaf2100c360cf13c92c4de33100@195.201.63.87:41666,6d8c83cc702365363b829a14efdd414401da369b@23.88.69.167:27565,89757803f40da51678451735445ad40d5b15e059@169.155.44.106:26656,3e319c765b7b48d518a2e3218efc317234b81681@142.132.159.188:26656,bb2a7dc81b9bd0e017409a2bbb71b12bb899e743@178.63.22.117:26656,a3d975c913570ad217d9a3de01a8616ad5ce20f8@142.132.128.137:26656,34e3178b6e0f25451fd690c15fc199d5a9bdfb9b@15.204.197.11:26656,6daeb8cfea285f561e167a0d94718b61e2cf7944@5.189.187.36:21656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.16:26656,ff7031f45a97600076f72b9318167e3dfcd2a17e@65.21.136.170:52656,c126eed9cfede7802d78f570fec8175835309a73@141.95.127.146:26656,0fedf7695d9e2721663c1d573d6d81a14c21533e@65.21.90.137:12856,2f6b34ad97c4827dace87436f0299cf89fe0c056@136.243.95.80:46656,faf349e185255c4aa2786da4f8ac70ea13849db0@169.155.45.128:26656,ce38728ac38ebbb4a72d496d42f8e9030af441d7@162.19.137.25:26656,a35d28e111c1dcc1e5f3203627b449adfb4425f2@65.109.29.150:21656,056d6a61c8a4c5ccb02123d67a013434423f155a@149.102.142.57:26656,6ac55af662061d3669d7c70961a8fd87ba2f2075@65.108.200.142:26696,d3a8fdbe6776fc71998fa893abcd634461b52b19@65.109.92.241:40106,92245ff5c7a4b293d2f0c7f9afca0ddad2e0fb52@65.108.244.178:26656,69e27ab9b46350654805df3ea8d9ac2f00af4e4c@38.242.244.85:26656,b8c42fcb311b47cdb8285b5697f661fbba5bf1a5@51.68.157.129:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
