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
peers="0c0e74c0550f5c394537f81617a6fd8480381654@94.130.142.27:36656,ee0328492fd21eee29ecbde19b52dfde6bd5da54@176.9.146.72:46656,7f2828e3910a4b165a65e5bfb2465c1e809bad3b@65.108.48.182:26656,eba8c88bb316eb42deed201c84013d2a945537f4@135.181.133.93:30656,5c11c697aaf2dabf96e3eb7e7e621c200bd309ee@65.21.225.58:26656,ec8a285e36888bd3134266b8ba668b48c327e6bf@142.132.202.50:36656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:35656,f4442b1ed7f64504f44ed85c89e38cfb2b19ef91@65.108.77.250:26641,001eb7a3a03dc11539541737262c4ddc84dec283@91.195.101.98:26656,fed6ab9973f224f3b2334fd48fa835512d6311da@185.244.183.200:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.haqqd/config/config.toml
```
