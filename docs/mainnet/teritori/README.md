# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/teritori.png" width="150" alt=""><figcaption></figcaption></figure>

Teritori is a multi-chain hub designed to allow IBC and non IBC communities  to connect, trade services & NFTs, launch new projects & build further existing ones.

**Chain ID**: teritori-1 | **Latest Version Tag**: v1.3.0 | **Wasm**: ON

[Website](https://teritori.com) | [Discord](https://discord.gg/teritori) | [Twitter](https://twitter.com/TeritoriNetwork)

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

**live-peers** (23)
```
peers="ec4126b26336cd61b335345df4ff2a3fbb79338a@65.109.92.240:20026,88a407d4749e1ccbb630f98ca44f304744d97864@38.242.141.168:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:19656,bbc594f0a8424368b869fef47a18d6e35965db2e@176.9.188.21:53656,5ab6437f73fe71f392d53566e037aa91087530ac@139.144.67.202:26656,6ef7a8bc7a3cc0856594f12570e8f2282a099dcf@65.109.93.152:26796,b336b83d9bab0b8cf96a3833efcbc196fab63fdd@212.95.51.215:36656,c669be4c7c0e44a3da941f4b97a8ee4ef39f7d6e@51.159.106.145:26656,7fb5a1a53f481f037487920ed08b0495158e2041@148.251.53.202:26796,0b27217386756577e1eadf00c4169dc8f041e522@51.210.7.219:26656,c124ce0b508e8b9ed1c5b6957f362225659b5343@169.155.168.57:26656,d956d6180e96c62315a777b1a3ed8f1ebf873e80@38.242.232.202:29656,97e4468ac589eac505a800411c635b14511a61bb@134.65.192.221:26656,471518432477e31ea348af246c0b54095d41352c@134.65.192.81:26656,370bf5f5b9ce655403d05753c355798288c1f120@89.245.24.83:23356,2b4f46e601fb4ede2a0c98976337e3afdaa50dac@65.108.238.102:15956,3594b73f909a9c4b87cfe6a361ef8b2b51124dd5@65.109.69.59:15956,6cceba286b498d4a1931f85e35ea0fa433373057@169.155.44.201:26656,29b92a4020171c20fe70e5d60f9c5d07dc9f31f7@194.163.161.146:26656,26175f13ada3d61c93bca342819fd5dc797bced0@65.109.58.226:28656,46b7ae20e3cc4264076a91c3601f3894a021a80d@65.108.6.45:36656,94b63fddfc78230f51aeb7ac34b9fb86bd042a77@176.9.98.24:30552,20e1000e88125698264454a884812746c2eb4807@65.108.227.217:15956"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.teritorid/config/config.toml
```
