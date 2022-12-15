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

**live-peers** (18)
```
peers="4cef2b81f82420434c6ce0dc43ca04ad18ef773f@65.108.75.107:15656,e3b906fefa58783395fcf72086c698707908a558@141.95.65.26:27736,1f4e77295379ce0c928502d2b075157a8c8a9e64@51.83.96.150:26642,358f13bd95d91517053a58f4d30205842672837f@104.37.187.214:60656,26d6ee4138c7533c5541722c6e1ecc6d60d47a86@104.193.254.42:26656,1ae3e0eafc14a3626a9cd43de867958526fd851a@176.9.98.24:30589,1e08fefb7e8851490d40e804df76d1ac33cb1f0a@38.146.3.175:15956,2f93424bd346b857bd5164eaac0b2bfd5fd644c0@144.91.127.252:26656,44b2bf9d970aece0531d3d939c5c546a7ac9201a@34.219.76.190:26656,f490d88332f112ccb43f25edb11f2d6b640f69fc@51.159.130.137:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:19656,8e1e342208f400bb10677617d4f08b31a3b48877@138.201.61.159:26656,26175f13ada3d61c93bca342819fd5dc797bced0@65.109.58.226:28656,ebacd77faa91ee858496a79250adff93480ce64b@158.69.188.117:26656,5ab6437f73fe71f392d53566e037aa91087530ac@139.144.67.202:26656,7fb5a1a53f481f037487920ed08b0495158e2041@148.251.53.202:26796,29b92a4020171c20fe70e5d60f9c5d07dc9f31f7@194.163.161.146:26656,46b7ae20e3cc4264076a91c3601f3894a021a80d@65.108.6.45:36656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.teritorid/config/config.toml
```
