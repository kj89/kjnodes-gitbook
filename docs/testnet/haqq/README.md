# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/haqq.png" width="150" alt=""><figcaption></figcaption></figure>

Haqq is the blockchain network that issues Islamic Coin,  its native cryptocurrency. Haqq is fast, trusted and  compatible with thousands of applications around the world.

**Chain ID**: haqq_54211-3 | **Latest Version Tag**: v1.2.1 | **Wasm**: OFF

Website: [https://islamiccoin.net](https://islamiccoin.net)


## Public endpoints

* rpc: [https://haqq-testnet.rpc.kjnodes.com](https://haqq-testnet.rpc.kjnodes.com)
* api: [https://haqq-testnet.api.kjnodes.com](https://haqq-testnet.api.kjnodes.com)

## Peering

**state-sync**

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@haqq-testnet.rpc.kjnodes.com:35656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@haqq-testnet.rpc.kjnodes.com:35659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/haqq-testnet/addrbook.json > $HOME/.haqqd/config/addrbook.json
```

**live-peers** (10)
```
peers="6fad54232f11a0306bd0d942c2ec5f9ba0ae2f1a@34.91.54.209:26656,35e1bf6fda8a37c9c4872527a30b1fe26b0a155f@45.13.59.201:26656,9eb507f9365313dbe7f426050fec9648298f58ee@109.205.183.51:26656,26a5bd6fb59f4dcd25f20bbc53b88860b2598f7d@65.21.91.50:35656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:35656,59af99085c961a6a5c8dc4bc8b3abffda16ddccb@135.181.38.62:26656,ee0328492fd21eee29ecbde19b52dfde6bd5da54@176.9.146.72:46656,9e288261ac5e42f25bd281f2564d756596aded6c@95.216.7.169:26656,7f4b4501af5f744210dcad95fb9b3915283fd0e9@185.244.182.203:26656,e576d332451c7c3c0c5c753b1bbd4e670b1ecfc7@5.161.97.83:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.haqqd/config/config.toml
```
