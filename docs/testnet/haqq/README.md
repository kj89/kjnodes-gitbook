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
peers="ee0328492fd21eee29ecbde19b52dfde6bd5da54@176.9.146.72:46656,62d44513c7fd5aafa65773e5c015ca032f8eea4a@213.239.213.179:26656,99a8389c84625503c2b8d734dfd78035d28e4f15@65.109.30.117:26656,562a589b82682f695344bc4a9d7a2fcb5a5a4d80@65.21.60.82:26656,181c3ef9dba190c45ad8143550188d24e471b7a5@148.251.47.69:16656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:35656,cf3127b52249fce3859a42afeb4162d6788593e2@77.232.39.155:26656,b6554c65e24f46e2834b018ac1790f9c1bcd2c74@195.201.165.123:20116,ec8a285e36888bd3134266b8ba668b48c327e6bf@142.132.202.50:36656,47a269c3e30f70d8234a2afd8e9055e74129fde0@65.108.129.29:36656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.haqqd/config/config.toml
```
