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
peers="d3a8fdbe6776fc71998fa893abcd634461b52b19@65.109.92.241:40106,1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,ff7031f45a97600076f72b9318167e3dfcd2a17e@65.21.136.170:52656,30ff8100fefac53ee40ef7631f1a3c66ca2b82cf@135.181.164.90:26656,12703ce9efe6c1171c193dae2e2041a2be610852@65.108.44.149:29656,57f475bb44fc6f121790d523ce06fb4e0ad9ab69@141.95.65.73:17256,c126eed9cfede7802d78f570fec8175835309a73@141.95.127.146:26656,703714c82c94fc1c74b6ee0d1fc3417b932be5f3@134.65.192.98:26656,e056318da91e77585f496333040e00e12f6941d1@51.83.97.166:26656,ff7621be29e39e9fdf07f2501e1a217201ca29ee@213.239.207.175:39656,3e319c765b7b48d518a2e3218efc317234b81681@142.132.159.188:26656,a3d975c913570ad217d9a3de01a8616ad5ce20f8@142.132.128.137:26656,17779ded6b3dc2f31d6c6f40cc6f07d802753ba7@78.47.153.128:26656,cd71aa366822800a2aa7051fae69127f78b3f203@188.165.225.226:26656,98206a8f71578850f1d88f08ede96ebc7e7c76a9@176.9.188.21:52656,b8c42fcb311b47cdb8285b5697f661fbba5bf1a5@51.68.157.129:26656,ae67d4c37632435e0d5f27041f50af20d227bdc2@93.170.72.118:21656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,b5bf2242c981371224e5e9e89d6c265d554c8989@65.21.202.154:21656,6daeb8cfea285f561e167a0d94718b61e2cf7944@5.189.187.36:21656,ce38728ac38ebbb4a72d496d42f8e9030af441d7@162.19.137.25:26656,d28516746773bfaeca4efa5537c0bf5990b8828e@65.21.229.33:27656,ab6a4ae2857ac05fa8f45b03871fa3945193fc61@46.4.81.204:35656,69e27ab9b46350654805df3ea8d9ac2f00af4e4c@38.242.244.85:26656,5fb9952f3eaeb5be3aab37425831c2a4830a019d@65.21.133.125:29656,92245ff5c7a4b293d2f0c7f9afca0ddad2e0fb52@65.108.244.178:26656,0fedf7695d9e2721663c1d573d6d81a14c21533e@65.21.90.137:12856,b570827e4397512e077028ea7121d3e19eb25bab@85.10.200.221:26656,6ac55af662061d3669d7c70961a8fd87ba2f2075@65.108.200.142:26696"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
