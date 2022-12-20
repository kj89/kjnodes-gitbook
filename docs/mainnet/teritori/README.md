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

**live-peers** (20)
```
peers="ec4126b26336cd61b335345df4ff2a3fbb79338a@65.109.92.240:20026,6085c32b26fb1baa4b16b426f5d56f2fff81cfc7@135.181.165.246:26656,6bc9f80a5123d62c23aadb7b5d68b740a794b0c6@65.109.49.111:36656,3178ac8fffd269325500c95679d58d5e8ec61746@198.244.213.94:22956,26d6ee4138c7533c5541722c6e1ecc6d60d47a86@104.193.254.42:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:19656,29b92a4020171c20fe70e5d60f9c5d07dc9f31f7@194.163.161.146:26656,4b04b3d164dc6dd5bb555a7a106a8d314f30516f@65.21.136.170:53656,8ac41af54dfd91c41de71cde222a55670f2f405d@141.95.65.73:15956,0b27217386756577e1eadf00c4169dc8f041e522@51.210.7.219:26656,b336b83d9bab0b8cf96a3833efcbc196fab63fdd@212.95.51.215:36656,3594b73f909a9c4b87cfe6a361ef8b2b51124dd5@65.109.69.59:15956,16f90d350de14a596ebdc683ce5e703c14e40bb3@75.119.146.181:19656,26175f13ada3d61c93bca342819fd5dc797bced0@65.109.58.226:28656,5ab6437f73fe71f392d53566e037aa91087530ac@139.144.67.202:26656,a191006e50d3af40fd253c23dae715a45fdd7415@95.179.217.1:26656,6ef7a8bc7a3cc0856594f12570e8f2282a099dcf@65.109.93.152:26796,a043a97266360ff45781a9fc9392aedc16494c59@65.108.97.58:19656,46b7ae20e3cc4264076a91c3601f3894a021a80d@65.108.6.45:36656,44b2bf9d970aece0531d3d939c5c546a7ac9201a@34.219.76.190:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.teritorid/config/config.toml
```
