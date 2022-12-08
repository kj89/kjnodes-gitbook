# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/teritori.png" width="150" alt=""><figcaption></figcaption></figure>

Teritori is a multi-chain hub designed to allow IBC and non IBC communities  to connect, trade services & NFTs, launch new projects & build further existing ones.

**Chain ID**: teritori-1 | **Latest Version Tag**: v1.3.0 | **Wasm**: ON

Website: [https://teritori.com](https://teritori.com)

## Restake

[Restake with kjnodes](https://restake.app/teritori/torivaloper184ln03hkpt75uhrrr26f66kvcqvf4yn4nc2xjm) (every day at 08:00, 20:00)
## Public endpoints

* rpc: [https://teritori.rpc.kjnodes.com](https://teritori.rpc.kjnodes.com)
* api: [https://teritori.api.kjnodes.com](https://teritori.api.kjnodes.com)

## Peering

**state-sync**

```
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@teritori.rpc.kjnodes.com:19656
```

**seed-node**

```
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@teritori.rpc.kjnodes.com:19659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/teritori/addrbook.json > $HOME/.teritorid/config/addrbook.json
```

**live-peers** (26)
```
peers="8e9624292123624e4eddc3f43189f08a0424127e@65.108.131.62:26656,358f13bd95d91517053a58f4d30205842672837f@104.37.187.214:60656,e627e9bbff303c96e859de00e5deaaf5104911cd@51.15.228.89:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:19656,ff8f8c1b4cf70f38e1c370af05a40c1845022ae8@51.79.103.43:26656,0af882985f5fa2db442eda8c9cf1dbcd87865ec5@65.109.94.221:1114,cdda30f407133027bf1322305e62ad968fad5348@96.69.133.222:26656,d956d6180e96c62315a777b1a3ed8f1ebf873e80@38.242.232.202:29656,ab03f6d2d469e0be5b7fd5cb7388c7feffc1deac@15.235.114.194:10656,5a98d637a16b16bf425a4a785c9d11a7d1e5b8a0@65.21.131.215:26736,d3b72cdd4f495dc77ca4bb4b2c76e9ce19f4f4af@144.76.90.130:26656,6ef7a8bc7a3cc0856594f12570e8f2282a099dcf@65.109.93.152:26796,ec4126b26336cd61b335345df4ff2a3fbb79338a@65.109.92.240:20026,7e6fcddab5901d18eeda4b662a499144da397028@54.37.129.164:54256,009e25e99e3f8fde86d283d4b8b0ce2f777cde53@138.201.8.248:53656,6fb98b9e316b2900fce2fd331621460a932f4d7d@65.108.15.183:51656,d43c09d1734e2135102621305aa3d15117b5d1b6@13.209.213.117:26656,bc8734c4c81fc1d0543b311914963be3954255bf@42.116.228.239:26656,40caa979c29a9930ea2b8a6249037924d308ae84@162.55.234.70:54256,3594b73f909a9c4b87cfe6a361ef8b2b51124dd5@65.109.69.59:15956,a8abf12f9b69a7d80999efe0aaafe5fcb28294d4@52.35.72.210:26656,16f90d350de14a596ebdc683ce5e703c14e40bb3@75.119.146.181:19656,29b92a4020171c20fe70e5d60f9c5d07dc9f31f7@194.163.161.146:26656,a191006e50d3af40fd253c23dae715a45fdd7415@95.179.217.1:26656,f490d88332f112ccb43f25edb11f2d6b640f69fc@51.159.130.137:26656,b52a6ec019dfa39bb052dec1406a043027e24fc8@65.144.145.234:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.teritorid/config/config.toml
```
