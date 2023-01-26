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
peers="18ec83c4e3938aec31a3a32154969107739f0b81@135.181.153.228:26656,346bf012c17fa30ef70ae72f082374838626532a@65.108.106.131:26696,eeca453e3a1cf670c78e2255b8f0bd5a9443c30b@65.108.225.71:26656,36afb1c827f52d38d7cd328b384d644b531b5997@65.108.238.102:17256,12e6bea6650a53150c01ca3897e4a0b94d6e9d4e@135.181.141.47:26656,6ac55af662061d3669d7c70961a8fd87ba2f2075@65.108.200.142:26696,b1b08fe470551dca6d6631fb1bfabb814f6c1aec@54.37.129.164:54556,4a4d2e7070e05ad6c13628d2f191d96172659452@65.109.65.210:40656,17779ded6b3dc2f31d6c6f40cc6f07d802753ba7@78.47.153.128:26656,2f6b34ad97c4827dace87436f0299cf89fe0c056@136.243.95.80:46656,e6f1684ed8ed5c586b188bf7088026da4ffdaff6@134.65.193.78:26656,1fe32d8f09b8715b1e626da17b3ecfe26623b371@176.9.22.117:27656,bb2a7dc81b9bd0e017409a2bbb71b12bb899e743@178.63.22.117:26656,ff7621be29e39e9fdf07f2501e1a217201ca29ee@213.239.207.175:39656,b8c42fcb311b47cdb8285b5697f661fbba5bf1a5@51.68.157.129:26656,cd71aa366822800a2aa7051fae69127f78b3f203@188.165.225.226:26656,6daeb8cfea285f561e167a0d94718b61e2cf7944@5.189.187.36:21656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,05483a7ec0160b17de1ad8e7793c7502e70e5525@146.59.85.223:17256,f546370843f92e2415524a7b18f9cd528e2fd706@65.109.55.186:26656,30ff8100fefac53ee40ef7631f1a3c66ca2b82cf@135.181.164.90:26656,12703ce9efe6c1171c193dae2e2041a2be610852@65.108.44.149:29656,b5bf2242c981371224e5e9e89d6c265d554c8989@65.21.202.154:21656,afdd27b58e851dcbb8c98c0e3191a0d8bfbcd3ae@65.108.41.252:26656,c124ce0b508e8b9ed1c5b6957f362225659b5343@134.65.192.98:26656,1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,87102b5dd22c1d17f97197c078f23726ae3c6214@91.157.60.253:26656,056d6a61c8a4c5ccb02123d67a013434423f155a@149.102.142.57:26656,4e3e545e85000045ef44905ab683a5db6f87cdbe@88.198.32.17:37656,89757803f40da51678451735445ad40d5b15e059@169.155.44.106:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
