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
peers="a7ad9ae5d3eb66fa88c7167074c394e8663383f2@95.217.121.229:11074,3178ac8fffd269325500c95679d58d5e8ec61746@198.244.213.94:22956,8ac41af54dfd91c41de71cde222a55670f2f405d@141.95.65.73:15956,ff8f8c1b4cf70f38e1c370af05a40c1845022ae8@51.79.103.43:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:19656,d43c09d1734e2135102621305aa3d15117b5d1b6@13.209.213.117:26656,82ebb17ddac20928fb8107201dad9f5aea7f9132@198.244.200.3:26656,8206037aba2622c284b8b229583a18c909709266@195.3.223.204:10656,2b4f46e601fb4ede2a0c98976337e3afdaa50dac@65.108.238.102:15956"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.teritorid/config/config.toml
```
