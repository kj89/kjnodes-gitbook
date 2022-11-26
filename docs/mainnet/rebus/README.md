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
peers="1f7c31506f465c5f5536862074e98fc7a6043d4c@65.108.13.212:26656,9d17d1c5b5d3b8c9e7ffab264b45b5dd979116f3@65.109.24.188:26656,346bf012c17fa30ef70ae72f082374838626532a@65.108.106.131:26696,ff7031f45a97600076f72b9318167e3dfcd2a17e@65.21.136.170:52656,aa2feb704c0089b1a0f23011a9e7cd2c27a06134@65.21.200.6:29656,641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,6ac55af662061d3669d7c70961a8fd87ba2f2075@65.108.200.142:26696,256d9790bf186f5a275790f7fe01e1b8800dcaaf@65.21.88.78:26656,b570827e4397512e077028ea7121d3e19eb25bab@85.10.200.221:26656,3cc5fb5f6140ac4e57dfc80940c8a06daa299c89@51.77.195.46:26656,ab6a4ae2857ac05fa8f45b03871fa3945193fc61@46.4.81.204:35656,69e27ab9b46350654805df3ea8d9ac2f00af4e4c@38.242.244.85:26656,6d8c83cc702365363b829a14efdd414401da369b@23.88.69.167:27565,2f6b34ad97c4827dace87436f0299cf89fe0c056@136.243.95.80:46656,b8613a7717b0ebaf2100c360cf13c92c4de33100@195.201.63.87:41666,b1b08fe470551dca6d6631fb1bfabb814f6c1aec@54.37.129.164:54556,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,d6c891779edb84d91aa7dd043dcc819c11bf6895@185.245.183.106:26656,4e2a874e538319f204f03751a5e458d0371d5b92@65.108.98.125:60556,c177f05fc7c0379e26eff108048c0bfd96949b2c@141.95.65.73:17256,15b1c913dc3d9dab7c912b27bb2a957abbfe8834@142.132.199.27:40106,d241f395a167fd7a9f155641760bffa8af6a50d2@167.235.98.202:27656,40e2c0b68a1dd48466714e3dd0581e4b7d498575@107.155.122.93:26656,12703ce9efe6c1171c193dae2e2041a2be610852@65.108.44.149:29656,09d22b9fc1b07f3e2f64b685ab6f28130bc2edd2@51.89.7.185:26637,5f4b34cf261bb4f2c14b8a707ed6cdbbee75d500@154.53.60.246:26656,3a378fbfae33a593b913371c876c9d275c0abb12@213.239.215.77:26656,b5bf2242c981371224e5e9e89d6c265d554c8989@65.21.202.154:21656,a155d381099de93e7efe00f9475786abffd29c3e@167.235.29.125:26637"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.rebusd/config/config.toml
```
