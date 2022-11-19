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

**live-peers** (11)
```
peers="7fb5a1a53f481f037487920ed08b0495158e2041@148.251.53.202:26796,ab03f6d2d469e0be5b7fd5cb7388c7feffc1deac@15.235.114.194:10656,82ebb17ddac20928fb8107201dad9f5aea7f9132@198.244.200.3:26656,574479abf5b0ed001519c60042bd88a97ce80a48@18.236.38.205:26656,ed090020aba4bb254ba1517644ab0d6c94c9461e@57.128.144.230:26656,2434c1dbf0c04bb50e17a39a77c317512b5c1dc4@65.109.35.66:51656,e3b906fefa58783395fcf72086c698707908a558@141.95.65.26:27736,2aab2f1c2c9b2a74c05ff53107f53b9b5cf75e6c@195.189.96.121:51656,28456ac1dded17760432c3f1d759c7d50ab6ed3e@51.250.83.54:26656,787a6b318ebc4167fefb1d5ef9f88af6cb5a8b29@173.212.222.167:35656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:19656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.teritorid/config/config.toml
```
