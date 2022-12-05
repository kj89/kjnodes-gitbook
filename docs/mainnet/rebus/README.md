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
peers="aa2feb704c0089b1a0f23011a9e7cd2c27a06134@65.21.200.6:29656,641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,e056318da91e77585f496333040e00e12f6941d1@51.83.97.166:26656,afdd27b58e851dcbb8c98c0e3191a0d8bfbcd3ae@65.108.41.252:26656,a3d975c913570ad217d9a3de01a8616ad5ce20f8@142.132.128.137:26656,ea5e7a6b9a5c18c6455e7a8c583c129c5821a452@51.178.80.111:26656,09d22b9fc1b07f3e2f64b685ab6f28130bc2edd2@51.89.7.185:26637,1fe32d8f09b8715b1e626da17b3ecfe26623b371@176.9.22.117:27656,1749a8f0aa533fc92c1212366c22c0993fbb1545@51.178.47.116:26656,ab6a4ae2857ac05fa8f45b03871fa3945193fc61@46.4.81.204:35656,2f6b34ad97c4827dace87436f0299cf89fe0c056@136.243.95.80:46656,235a2754b94c86a85ba645119151ee55d6971554@213.239.216.252:26656,f4ad005ee8ec25508c498294e9e83d81b188ea49@185.248.24.16:21656,92245ff5c7a4b293d2f0c7f9afca0ddad2e0fb52@65.108.244.178:26656,ce38728ac38ebbb4a72d496d42f8e9030af441d7@162.19.137.25:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,75c5365e8da9a4caa908a195ffa3fdc1e6432019@65.108.232.248:26756,b570827e4397512e077028ea7121d3e19eb25bab@85.10.200.221:26656,bb2a7dc81b9bd0e017409a2bbb71b12bb899e743@178.63.22.117:26656,5a13200e67f6cb5385d9d8f8c68a7b5e62f8cd54@188.34.176.96:26656,9d17d1c5b5d3b8c9e7ffab264b45b5dd979116f3@65.109.24.188:26656,34e3178b6e0f25451fd690c15fc199d5a9bdfb9b@15.204.197.11:26656,12703ce9efe6c1171c193dae2e2041a2be610852@65.108.44.149:29656,6d8c83cc702365363b829a14efdd414401da369b@23.88.69.167:27565,b8137c688096d1abcf56942d335d061f212e6629@62.212.65.138:34656,237bfc05da5f8cabee00f148995333f37186d232@164.68.121.101:26656,f2483e5af4cb1fab55e4f6422627c0365f45b5dd@194.163.188.252:26656,b8ed7daa4e2966f6c160915600d7dadf7e3ef61e@62.171.142.94:26156"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.rebusd/config/config.toml
```
