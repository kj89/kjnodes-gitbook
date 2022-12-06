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
peers="b8ed7daa4e2966f6c160915600d7dadf7e3ef61e@62.171.142.94:26156,641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,75c5365e8da9a4caa908a195ffa3fdc1e6432019@65.108.232.248:26756,a35d28e111c1dcc1e5f3203627b449adfb4425f2@65.109.29.150:21656,5f29f14fe3dd7e1d86caa4d344e67ee81c32255f@65.109.37.228:26656,c126eed9cfede7802d78f570fec8175835309a73@141.95.127.146:26656,ce38728ac38ebbb4a72d496d42f8e9030af441d7@162.19.137.25:26656,b570827e4397512e077028ea7121d3e19eb25bab@85.10.200.221:26656,3a378fbfae33a593b913371c876c9d275c0abb12@213.239.215.77:26656,a3d975c913570ad217d9a3de01a8616ad5ce20f8@142.132.128.137:26656,ab6a4ae2857ac05fa8f45b03871fa3945193fc61@46.4.81.204:35656,b8137c688096d1abcf56942d335d061f212e6629@62.212.65.138:34656,f4ad005ee8ec25508c498294e9e83d81b188ea49@185.248.24.16:21656,34e3178b6e0f25451fd690c15fc199d5a9bdfb9b@15.204.197.11:26656,3e319c765b7b48d518a2e3218efc317234b81681@142.132.159.188:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,237bfc05da5f8cabee00f148995333f37186d232@164.68.121.101:26656,dda7abe32cc84a722cf6b1d2ee3b61ebe7ad71df@135.181.212.183:21656,eeca453e3a1cf670c78e2255b8f0bd5a9443c30b@65.108.225.71:26656,c177f05fc7c0379e26eff108048c0bfd96949b2c@141.95.65.73:17256,89ded0a3987d22e46b756fead439e2a4d25f23cb@185.144.99.30:26656,404ae118865c1485f7859fa2c7cc2e3b8c402a14@51.75.135.34:26656,18ec83c4e3938aec31a3a32154969107739f0b81@135.181.153.228:26656,c0b33353fb70d8d71dcb9c8848b3b4207bd56951@188.165.221.155:30547,e056318da91e77585f496333040e00e12f6941d1@51.83.97.166:26656,4e2a874e538319f204f03751a5e458d0371d5b92@65.108.98.125:60556,d28516746773bfaeca4efa5537c0bf5990b8828e@65.21.229.33:27656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.rebusd/config/config.toml
```
