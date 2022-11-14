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

**live-peers** (30)
```
peers="256d9790bf186f5a275790f7fe01e1b8800dcaaf@65.21.88.78:26656,f83df63886e56713bf3adb5c6836b1a7b07ec024@65.108.235.18:26656,ad116a3f497ebb37ac14226c22a1483237a224ac@65.108.229.102:23656,5f29f14fe3dd7e1d86caa4d344e67ee81c32255f@65.109.37.228:26656,aa2feb704c0089b1a0f23011a9e7cd2c27a06134@65.21.200.6:29656,30ff8100fefac53ee40ef7631f1a3c66ca2b82cf@135.181.164.90:26656,3e319c765b7b48d518a2e3218efc317234b81681@142.132.159.188:26656,75c5365e8da9a4caa908a195ffa3fdc1e6432019@65.108.232.248:26756,c126eed9cfede7802d78f570fec8175835309a73@141.95.127.146:26656,b8137c688096d1abcf56942d335d061f212e6629@62.212.65.138:34656,304ff8e051b2fbd038771142b69ac915c14c0819@78.46.78.83:26656,a3d975c913570ad217d9a3de01a8616ad5ce20f8@142.132.128.137:26656,7ee74ea68e350fc5214657255cba5e339bb30c2a@138.201.127.91:26674,8f023504e27873141164b6fbf1c4b788ff8d533b@159.69.200.24:26656,69e27ab9b46350654805df3ea8d9ac2f00af4e4c@38.242.244.85:26656,d6c891779edb84d91aa7dd043dcc819c11bf6895@185.245.183.106:26656,036c453576f9f4cad684e78d09e0fbf876e9cdee@54.39.243.226:22656,f0d73a4976e64643ffc6d3fc335725902b795491@162.248.225.244:26656,5f4b34cf261bb4f2c14b8a707ed6cdbbee75d500@154.53.60.246:26656,cd71aa366822800a2aa7051fae69127f78b3f203@188.165.225.226:26656,a35d28e111c1dcc1e5f3203627b449adfb4425f2@65.109.29.150:21656,dda7abe32cc84a722cf6b1d2ee3b61ebe7ad71df@135.181.212.183:21656,237bfc05da5f8cabee00f148995333f37186d232@164.68.121.101:26656,6daeb8cfea285f561e167a0d94718b61e2cf7944@5.189.187.36:21656,a155d381099de93e7efe00f9475786abffd29c3e@167.235.29.125:26637,12e6bea6650a53150c01ca3897e4a0b94d6e9d4e@135.181.141.47:26656,42d76e6353f9f2206ca062935d0523baa4b7f671@116.202.227.117:21656,3fc3b7e3073cc0d59fef9390cad15601d7109dd0@65.108.193.11:26656,f4ad005ee8ec25508c498294e9e83d81b188ea49@185.248.24.16:21656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:21656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.rebusd/config/config.toml
```
