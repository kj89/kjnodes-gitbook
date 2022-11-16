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

**live-peers** (9)
```
peers="2afdb9300c47e43e555fa572d033b2d68ac28506@65.109.70.68:26686,29b92a4020171c20fe70e5d60f9c5d07dc9f31f7@194.163.161.146:26656,a191006e50d3af40fd253c23dae715a45fdd7415@95.179.217.1:26656,92ad0e776634318bb99e99b968051f4463e98e5a@161.97.132.199:36656,f813a00f52de54a49aea3211b89a65ae6133eac2@88.99.167.148:26686,82ebb17ddac20928fb8107201dad9f5aea7f9132@198.244.200.3:26656,bbc594f0a8424368b869fef47a18d6e35965db2e@176.9.188.21:53656,26d6ee4138c7533c5541722c6e1ecc6d60d47a86@104.193.254.42:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:19656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.teritorid/config/config.toml
```
