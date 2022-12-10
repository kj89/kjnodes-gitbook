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

**live-peers** (29)
```
peers="237bfc05da5f8cabee00f148995333f37186d232@164.68.121.101:26656,641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,12703ce9efe6c1171c193dae2e2041a2be610852@65.108.44.149:29656,12e6bea6650a53150c01ca3897e4a0b94d6e9d4e@135.181.141.47:26656,18ec83c4e3938aec31a3a32154969107739f0b81@135.181.153.228:26656,e056318da91e77585f496333040e00e12f6941d1@51.83.97.166:26656,aa2feb704c0089b1a0f23011a9e7cd2c27a06134@65.21.200.6:29656,3e319c765b7b48d518a2e3218efc317234b81681@142.132.159.188:26656,bb2a7dc81b9bd0e017409a2bbb71b12bb899e743@178.63.22.117:26656,ab6a4ae2857ac05fa8f45b03871fa3945193fc61@46.4.81.204:35656,cd71aa366822800a2aa7051fae69127f78b3f203@188.165.225.226:26656,056d6a61c8a4c5ccb02123d67a013434423f155a@149.102.142.57:26656,69e27ab9b46350654805df3ea8d9ac2f00af4e4c@38.242.244.85:26656,b570827e4397512e077028ea7121d3e19eb25bab@85.10.200.221:26656,6d8c83cc702365363b829a14efdd414401da369b@23.88.69.167:27565,186209f02d238b48dcc7997cca3e6c6855aa91aa@20.112.73.169:26656,75c5365e8da9a4caa908a195ffa3fdc1e6432019@65.108.232.248:26756,dda7abe32cc84a722cf6b1d2ee3b61ebe7ad71df@135.181.212.183:21656,3a3e7123b9ae814b8d8517b6635d21b9ae45bf25@195.3.222.148:26656,4e2a874e538319f204f03751a5e458d0371d5b92@65.108.98.125:60556,c126eed9cfede7802d78f570fec8175835309a73@141.95.127.146:26656,2f6b34ad97c4827dace87436f0299cf89fe0c056@136.243.95.80:46656,d28516746773bfaeca4efa5537c0bf5990b8828e@65.21.229.33:27656,346bf012c17fa30ef70ae72f082374838626532a@65.108.106.131:26696,34e3178b6e0f25451fd690c15fc199d5a9bdfb9b@15.204.197.11:26656,ea5e7a6b9a5c18c6455e7a8c583c129c5821a452@51.178.80.111:26656,5a13200e67f6cb5385d9d8f8c68a7b5e62f8cd54@188.34.176.96:26656,256d9790bf186f5a275790f7fe01e1b8800dcaaf@65.21.88.78:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.rebusd/config/config.toml
```
