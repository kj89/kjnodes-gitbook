# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/rebus.png" width="150" alt=""><figcaption></figcaption></figure>

Rebuschain is a platform that will provide DeFi (Decentralized Finance)  investment opportunities to traditional investors clearly and conveniently

**Chain ID**: reb_1111-1 | **Latest Version Tag**: v0.2.0 | **Wasm**: OFF

[Website](https://www.rebuschain.com) | [Discord](https://discord.gg/rebuschain) | [Twitter](https://twitter.com/RebusChain)

## Restake

[Restake with kjnodes](https://restake.app/rebus/rebusvaloper1vndzy8y55ylgpmmsc34uy8rm6kqlml6ffs9lrv) (every day at 08:00, 20:00)
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
peers="f28f30d79025cfadda58edb411bb054b4cf5504f@65.108.226.44:26456,1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,5fb9952f3eaeb5be3aab37425831c2a4830a019d@65.21.133.125:29656,12703ce9efe6c1171c193dae2e2041a2be610852@65.108.44.149:29656,d28516746773bfaeca4efa5537c0bf5990b8828e@65.21.229.33:27656,afdd27b58e851dcbb8c98c0e3191a0d8bfbcd3ae@65.108.41.252:26656,3cc5fb5f6140ac4e57dfc80940c8a06daa299c89@51.77.195.46:26656,ce38728ac38ebbb4a72d496d42f8e9030af441d7@162.19.137.25:26656,c124ce0b508e8b9ed1c5b6957f362225659b5343@134.65.192.98:26656,faf349e185255c4aa2786da4f8ac70ea13849db0@169.155.45.128:26656,c126eed9cfede7802d78f570fec8175835309a73@141.95.127.146:26656,bb2a7dc81b9bd0e017409a2bbb71b12bb899e743@178.63.22.117:26656,05483a7ec0160b17de1ad8e7793c7502e70e5525@146.59.85.223:17256,b8c42fcb311b47cdb8285b5697f661fbba5bf1a5@51.68.157.129:26656,6daeb8cfea285f561e167a0d94718b61e2cf7944@5.189.187.36:21656,36afb1c827f52d38d7cd328b384d644b531b5997@65.108.238.102:17256,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,f546370843f92e2415524a7b18f9cd528e2fd706@65.109.55.186:26656,b5bf2242c981371224e5e9e89d6c265d554c8989@65.21.202.154:21656,a3d975c913570ad217d9a3de01a8616ad5ce20f8@142.132.128.137:26656,5f29f14fe3dd7e1d86caa4d344e67ee81c32255f@65.109.37.228:26656,4a4d2e7070e05ad6c13628d2f191d96172659452@65.109.65.210:40656,89757803f40da51678451735445ad40d5b15e059@169.155.44.106:26656,ff7621be29e39e9fdf07f2501e1a217201ca29ee@213.239.207.175:39656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.16:26656,056d6a61c8a4c5ccb02123d67a013434423f155a@149.102.142.57:26656,30ff8100fefac53ee40ef7631f1a3c66ca2b82cf@135.181.164.90:26656,9832950578c4492d934d6e875165757f5a98caff@51.83.96.150:26637,6ac55af662061d3669d7c70961a8fd87ba2f2075@65.108.200.142:26696,b570827e4397512e077028ea7121d3e19eb25bab@85.10.200.221:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
