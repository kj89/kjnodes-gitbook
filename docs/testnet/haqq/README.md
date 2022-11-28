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
peers="0c0e74c0550f5c394537f81617a6fd8480381654@94.130.142.27:36656,ec8a285e36888bd3134266b8ba668b48c327e6bf@142.132.202.50:36656,5c11c697aaf2dabf96e3eb7e7e621c200bd309ee@65.21.225.58:26656,e8ace69c3fc4f372f003bc5d7472597006bb31bc@65.108.213.255:26656,99a8389c84625503c2b8d734dfd78035d28e4f15@65.109.30.117:26656,cf3127b52249fce3859a42afeb4162d6788593e2@77.232.39.155:26656,ce080696d69228597caf0e80920dfe1bae2dcd54@95.217.12.131:26656,b70802dd7c7705f1c7d5535f2ad529c66bdbdee1@95.217.236.79:12656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:35656,6ce864d853904ebef9400528f129d8fefa6f1827@91.211.251.232:36656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.haqqd/config/config.toml
```
