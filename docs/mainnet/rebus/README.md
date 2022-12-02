# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/rebus.png" width="150" alt=""><figcaption></figcaption></figure>

Rebuschain is a platform that will provide DeFi (Decentralized Finance)  investment opportunities to traditional investors clearly and conveniently

**Chain ID**: reb_1111-1 | **Latest Version Tag**: v0.2.0 | **Wasm**: OFF

Website: [https://www.rebuschain.com](https://www.rebuschain.com)

## Restake

[Restake with kjnodes](https://restake.app/rebus/rebusvaloper1vndzy8y55ylgpmmsc34uy8rm6kqlml6ffs9lrv) (every day at 08:00, 20:00)
## Public endpoints

* rpc: [https://rebus.rpc.kjnodes.com](https://rebus.rpc.kjnodes.com)
* api: [https://rebus.api.kjnodes.com](https://rebus.api.kjnodes.com)

## Peering

**state-sync**

```
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@rebus.rpc.kjnodes.com:21656
```

**seed-node**

```
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@rebus.rpc.kjnodes.com:21659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/rebus/addrbook.json > $HOME/.rebusd/config/addrbook.json
```

**live-peers** (28)
```
peers="75c5365e8da9a4caa908a195ffa3fdc1e6432019@65.108.232.248:26756,9d17d1c5b5d3b8c9e7ffab264b45b5dd979116f3@65.109.24.188:26656,f467e286567f94c89d39a5bcea0e1d68951299f9@146.59.81.204:34456,ea5e7a6b9a5c18c6455e7a8c583c129c5821a452@51.178.80.111:26656,3a378fbfae33a593b913371c876c9d275c0abb12@213.239.215.77:26656,18ec83c4e3938aec31a3a32154969107739f0b81@135.181.153.228:26656,7ee74ea68e350fc5214657255cba5e339bb30c2a@138.201.127.91:26674,5a13200e67f6cb5385d9d8f8c68a7b5e62f8cd54@188.34.176.96:26656,9abd6680cf74fce2ade8edfd8a898dd4a927a425@38.242.242.99:30656,69e27ab9b46350654805df3ea8d9ac2f00af4e4c@38.242.244.85:26656,237bfc05da5f8cabee00f148995333f37186d232@164.68.121.101:26656,056d6a61c8a4c5ccb02123d67a013434423f155a@149.102.142.57:26656,b1dcbb37514fbe215be54079e71aa39dac7fd0ae@64.5.123.203:26656,98206a8f71578850f1d88f08ede96ebc7e7c76a9@176.9.188.21:52656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,f97a11f283cd5f11bf1fe73d8b2012b711d61ce9@38.242.205.80:21656,1749a8f0aa533fc92c1212366c22c0993fbb1545@51.178.47.116:26656,77ca73199cf0a73ab52fc216d8ab8f8756275fef@138.201.8.248:52656,ad613c7b9c6bb978edd86ae1116cf4c0e0b45c22@92.205.61.172:28656,6d8c83cc702365363b829a14efdd414401da369b@23.88.69.167:27565,36afb1c827f52d38d7cd328b384d644b531b5997@65.108.238.102:17256,3a3e7123b9ae814b8d8517b6635d21b9ae45bf25@195.3.222.148:26656,6ad5dd14c578016cc7bc4d7c6d6f7f773bba39af@65.109.60.57:26656,fa292bfad37826c9da43894b349b1480dff516b5@65.108.99.254:31656,34e3178b6e0f25451fd690c15fc199d5a9bdfb9b@15.204.197.11:26656,404ae118865c1485f7859fa2c7cc2e3b8c402a14@51.75.135.34:26656,2f6b34ad97c4827dace87436f0299cf89fe0c056@136.243.95.80:46656,aa2feb704c0089b1a0f23011a9e7cd2c27a06134@65.21.200.6:29656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.rebusd/config/config.toml
```
