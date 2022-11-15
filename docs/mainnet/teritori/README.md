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

**live-peers** (10)
```
peers="c7cd979a49bb288df19db750d8d15d975380e1cf@5.9.137.184:26656,8ac41af54dfd91c41de71cde222a55670f2f405d@141.95.65.73:15956,b98db7bf9182a12b6ff7b8efc9f80350ccc67045@23.88.69.167:26878,82ebb17ddac20928fb8107201dad9f5aea7f9132@198.244.200.3:26656,1f9293a286df733dac6303aad3c39240ad3b3796@178.211.139.24:46656,c6f9573f0b5b7f986ec121e584465f2c6cd53de3@51.159.0.207:36656,14d7bd76bdc691149b00d0301afb0393246f863d@212.227.73.190:26656,526d8c7c44f59be9a39d7463c576b68c0db23174@65.108.234.23:15956,722b63e6c65628b929f22013dcbcde980210cb44@176.9.127.54:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:19656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.teritorid/config/config.toml
```
