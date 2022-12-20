# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/haqq.png" width="150" alt=""><figcaption></figcaption></figure>

Haqq is the blockchain network that issues Islamic Coin,  its native cryptocurrency. Haqq is fast, trusted and  compatible with thousands of applications around the world.

**Chain ID**: haqq_54211-3 | **Latest Version Tag**: v1.3.0 | **Wasm**: OFF

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
peers="23a1176c9911eac442d6d1bf15f92eeabb3981d5@34.91.81.33:26656,c932600aa633bb17e07dcb53ae982c834ba1b734@185.225.232.148:26656,5c11c697aaf2dabf96e3eb7e7e621c200bd309ee@65.21.225.58:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:35656,927a323649e7dd8d4c75da6e5edaee439652b46f@65.109.92.241:20116,ba56c564a5430632e59e2b08fc348735bc56b32f@154.12.232.140:26656,fed6ab9973f224f3b2334fd48fa835512d6311da@185.244.183.200:26656,47a269c3e30f70d8234a2afd8e9055e74129fde0@65.108.129.29:36656,6ce864d853904ebef9400528f129d8fefa6f1827@91.211.251.232:36656,9eb507f9365313dbe7f426050fec9648298f58ee@109.205.183.51:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.haqqd/config/config.toml
```
