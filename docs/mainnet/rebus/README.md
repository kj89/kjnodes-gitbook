# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/rebus.png" width="150" alt=""><figcaption></figcaption></figure>

Rebuschain is a platform that will provide DeFi (Decentralized Finance)  investment opportunities to traditional investors clearly and conveniently

**Chain ID**: reb_1111-1 | **Latest Version Tag**: v0.2.0

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
peers="a35d28e111c1dcc1e5f3203627b449adfb4425f2@65.109.29.150:21656,30ff8100fefac53ee40ef7631f1a3c66ca2b82cf@135.181.164.90:26656,ad116a3f497ebb37ac14226c22a1483237a224ac@65.108.229.102:23656,02dfa87d537a35deced0723029fcadfae71c2c72@185.221.196.52:21656,c177f05fc7c0379e26eff108048c0bfd96949b2c@141.95.65.73:17256,237bfc05da5f8cabee00f148995333f37186d232@164.68.121.101:26656,8f023504e27873141164b6fbf1c4b788ff8d533b@159.69.200.24:26656,2f6b34ad97c4827dace87436f0299cf89fe0c056@136.243.95.80:46656,77ca73199cf0a73ab52fc216d8ab8f8756275fef@138.201.8.248:52656,3e319c765b7b48d518a2e3218efc317234b81681@142.132.159.188:26656,69e27ab9b46350654805df3ea8d9ac2f00af4e4c@38.242.244.85:26656,7ee74ea68e350fc5214657255cba5e339bb30c2a@138.201.127.91:26674,304ff8e051b2fbd038771142b69ac915c14c0819@78.46.78.83:26656,d6c891779edb84d91aa7dd043dcc819c11bf6895@185.245.183.106:26656,5c2018214fcfde67ec390702539f295165f12a3a@86.48.2.20:26656,1749a8f0aa533fc92c1212366c22c0993fbb1545@51.178.47.116:26656,0fedf7695d9e2721663c1d573d6d81a14c21533e@65.21.90.137:12856,3a3e7123b9ae814b8d8517b6635d21b9ae45bf25@195.3.222.148:26656,b1b08fe470551dca6d6631fb1bfabb814f6c1aec@54.37.129.164:54556,f0d73a4976e64643ffc6d3fc335725902b795491@162.248.225.244:26656,5f4b34cf261bb4f2c14b8a707ed6cdbbee75d500@154.53.60.246:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:21656,afdd27b58e851dcbb8c98c0e3191a0d8bfbcd3ae@65.108.41.252:26656,9d17d1c5b5d3b8c9e7ffab264b45b5dd979116f3@65.109.24.188:26656,d41384a02d523f1ec7310105413e75be2a76b252@85.17.77.84:26658,7490cdec1e04d0f415e4f3959e5b8399a22d7ab0@185.182.184.106:26656,0a3eb0b5a76b2b881ae260e4546e3fbbfbbfba4b@65.108.206.56:32656,36afb1c827f52d38d7cd328b384d644b531b5997@65.108.238.102:17256,07b84cf4b47a2e5ad251267716fe05bcf30330cd@65.21.170.3:29656,1e3e466e9e0bfc129d69c0fb71149aea9557bd98@51.89.40.96:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.rebusd/config/config.toml
```
