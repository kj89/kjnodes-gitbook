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
peers="275d2614d24c8ac015a7712702fcb99cef67ef67@65.108.124.219:29656,92245ff5c7a4b293d2f0c7f9afca0ddad2e0fb52@65.108.244.178:26656,6ac55af662061d3669d7c70961a8fd87ba2f2075@65.108.200.142:26696,256d9790bf186f5a275790f7fe01e1b8800dcaaf@65.21.88.78:26656,346bf012c17fa30ef70ae72f082374838626532a@65.108.106.131:26696,d3a8fdbe6776fc71998fa893abcd634461b52b19@65.109.92.241:40106,b570827e4397512e077028ea7121d3e19eb25bab@85.10.200.221:26656,ff7621be29e39e9fdf07f2501e1a217201ca29ee@213.239.207.175:39656,ab6a4ae2857ac05fa8f45b03871fa3945193fc61@46.4.81.204:35656,e6f1684ed8ed5c586b188bf7088026da4ffdaff6@134.65.193.78:26656,c126eed9cfede7802d78f570fec8175835309a73@141.95.127.146:26656,bb2a7dc81b9bd0e017409a2bbb71b12bb899e743@178.63.22.117:26656,c124ce0b508e8b9ed1c5b6957f362225659b5343@134.65.192.98:26656,0fedf7695d9e2721663c1d573d6d81a14c21533e@65.21.90.137:12856,b8137c688096d1abcf56942d335d061f212e6629@62.212.65.138:34656,17779ded6b3dc2f31d6c6f40cc6f07d802753ba7@78.47.153.128:26656,ce38728ac38ebbb4a72d496d42f8e9030af441d7@162.19.137.25:26656,b1b08fe470551dca6d6631fb1bfabb814f6c1aec@54.37.129.164:54556,241c83e7a6ff769d66be0c4848db44cdcac8b4b0@192.99.62.83:26656,1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,a3d975c913570ad217d9a3de01a8616ad5ce20f8@142.132.128.137:26656,b1dcbb37514fbe215be54079e71aa39dac7fd0ae@64.5.123.203:26656,ae67d4c37632435e0d5f27041f50af20d227bdc2@93.170.72.118:21656,641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,6dc49b312a98051351f0347568c294fea83a5f9a@51.79.27.21:11656,ebc4d27be0c87f537b44250c2e22ad349dc59fb6@158.69.116.134:26656,cd71aa366822800a2aa7051fae69127f78b3f203@188.165.225.226:26656,7ee74ea68e350fc5214657255cba5e339bb30c2a@138.201.127.91:26674,3cc5fb5f6140ac4e57dfc80940c8a06daa299c89@51.77.195.46:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
