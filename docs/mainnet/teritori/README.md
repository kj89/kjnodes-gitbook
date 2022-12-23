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

**live-peers** (30)
```
peers="b336b83d9bab0b8cf96a3833efcbc196fab63fdd@212.95.51.215:36656,009e25e99e3f8fde86d283d4b8b0ce2f777cde53@138.201.8.248:53656,48980875839186e08e12ebf0d9a2803b45206833@65.109.92.241:38026,358f13bd95d91517053a58f4d30205842672837f@104.37.187.214:60656,0b27217386756577e1eadf00c4169dc8f041e522@51.210.7.219:26656,ec4126b26336cd61b335345df4ff2a3fbb79338a@65.109.92.240:20026,88a407d4749e1ccbb630f98ca44f304744d97864@38.242.141.168:26656,106490318e51355bc6d72e7941a0080f8b8256b9@185.16.39.14:26656,3178ac8fffd269325500c95679d58d5e8ec61746@198.244.213.94:22956,3594b73f909a9c4b87cfe6a361ef8b2b51124dd5@65.109.69.59:15956,cdda30f407133027bf1322305e62ad968fad5348@96.69.133.222:26656,82ebb17ddac20928fb8107201dad9f5aea7f9132@198.244.200.3:26656,ff8f8c1b4cf70f38e1c370af05a40c1845022ae8@51.79.103.43:26656,8f4db549de62fbb96cf4cf477e2af9c52f74a3dd@51.91.64.170:19656,e627e9bbff303c96e859de00e5deaaf5104911cd@51.15.228.89:26656,d956d6180e96c62315a777b1a3ed8f1ebf873e80@38.242.232.202:29656,d43c09d1734e2135102621305aa3d15117b5d1b6@13.209.213.117:26656,28456ac1dded17760432c3f1d759c7d50ab6ed3e@51.250.83.54:26656,3950af34da35ce3ff8c50ff3c47a43f5dfc93947@195.3.220.154:19656,ed747c9e39fc04fdbc7ab5fc4a4a7f7a298ee329@65.144.145.234:26656,24b28cf013e6d7b5b88b6dba2701c5ddd2dd5ee1@65.109.58.225:28656,6bc9f80a5123d62c23aadb7b5d68b740a794b0c6@65.109.49.111:36656,593b8319d1d4b1958e7daba8c3bbb56795cb59ba@146.59.81.92:51656,26175f13ada3d61c93bca342819fd5dc797bced0@65.109.58.226:28656,51eaf493facf36754411baa4f7b89355bd9cb3e7@195.201.63.87:42666,fffcd8c41a92e24d67b6d026f556c5afd49db092@45.77.41.21:26656,46b7ae20e3cc4264076a91c3601f3894a021a80d@65.108.6.45:36656,b78dd48a9d34146f04801f479a82348a19a69ab7@51.159.185.141:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:19656,29b92a4020171c20fe70e5d60f9c5d07dc9f31f7@194.163.161.146:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.teritorid/config/config.toml
```
